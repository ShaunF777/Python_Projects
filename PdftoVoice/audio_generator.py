#!/usr/bin/env python3
"""
Audio Generator - Convert text to speech with different voices for formatting
Supports SSML and multiple TTS engines
"""

import os
import re
import json
import logging
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import requests
from pydub import AudioSegment
from io import BytesIO
import time

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class AudioGenerator:
    def __init__(self, tts_service: str = "polly"):
        """
        Initialize Audio Generator
        
        Args:
            tts_service: TTS service to use ('polly', 'google', 'elevenlabs', 'local')
        """
        self.tts_service = tts_service
        self.output_dir = Path("output")
        self.audio_dir = self.output_dir / "audio"
        self.audio_dir.mkdir(parents=True, exist_ok=True)
        
        # Voice configurations
        self.voice_configs = {
            'polly': {
                'normal_voice': 'Joanna',
                'italic_voice': 'Matthew',
                'bracket_voice': 'Amy',
                'engine': 'neural'
            },
            'google': {
                'normal_voice': 'en-US-Standard-C',
                'italic_voice': 'en-US-Standard-B',
                'bracket_voice': 'en-US-Standard-A'
            },
            'elevenlabs': {
                'normal_voice': 'Rachel',
                'italic_voice': 'Drew',
                'bracket_voice': 'Clyde'
            }
        }
        
        # Default speech settings
        self.speech_settings = {
            'rate': 'slow',        # slow, medium, fast
            'pitch': 'medium',     # low, medium, high
            'volume': 'medium',    # soft, medium, loud
            'pause_between_sections': '1s',
            'pause_between_pages': '2s'
        }
        
    def create_audio(self, text_data: Dict, output_name: str, 
                    voice_config: Optional[Dict] = None) -> str:
        """
        Create audio file from processed text data
        
        Args:
            text_data: Dictionary containing text segments and formatting
            output_name: Name for output file (without extension)
            voice_config: Custom voice configuration
            
        Returns:
            Path to generated audio file
        """
        logger.info(f"Creating audio file: {output_name}")
        
        # Use custom voice config if provided
        if voice_config:
            current_config = voice_config
        else:
            current_config = self.voice_configs.get(self.tts_service, self.voice_configs['polly'])
        
        # Generate SSML content
        ssml_content = self._create_ssml_content(text_data, current_config)
        
        # Create audio based on selected TTS service
        if self.tts_service == 'polly':
            audio_file = self._create_audio_polly(ssml_content, output_name, current_config)
        elif self.tts_service == 'google':
            audio_file = self._create_audio_google(ssml_content, output_name, current_config)
        elif self.tts_service == 'elevenlabs':
            audio_file = self._create_audio_elevenlabs(ssml_content, output_name, current_config)
        else:
            # Fallback to local TTS
            audio_file = self._create_audio_local(ssml_content, output_name, current_config)
        
        logger.info(f"Audio file created: {audio_file}")
        return audio_file
    
    def _create_ssml_content(self, text_data: Dict, voice_config: Dict) -> str:
        """Create SSML content with different voices for different text types"""
        ssml_parts = ['<speak>']
        
        # Add introduction pause
        ssml_parts.append('<break time="1s"/>')
        
        for page_num, page_data in enumerate(text_data['pages'], 1):
            # Page announcement (optional)
            if len(text_data['pages']) > 1:
                ssml_parts.append(
                    f'<voice name="{voice_config["normal_voice"]}">'
                    f'<break time="0.5s"/>Page {page_num}<break time="1s"/>'
                    f'</voice>'
                )
            
            # Process regular text
            regular_text = page_data.get('regular_text', '').strip()
            if regular_text:
                # Handle bracketed content in regular text
                regular_text = self._process_bracketed_content(regular_text, voice_config)
                
                ssml_parts.append(
                    f'<voice name="{voice_config["normal_voice"]}">'
                    f'<prosody rate="{self.speech_settings["rate"]}" '
                    f'pitch="{self.speech_settings["pitch"]}">'
                    f'{regular_text}'
                    f'</prosody></voice>'
                )
                ssml_parts.append(f'<break time="{self.speech_settings["pause_between_sections"]}"/>')
            
            # Process italic text with different voice
            italic_text = page_data.get('italic_text', '').strip()
            if italic_text:
                ssml_parts.append(
                    f'<voice name="{voice_config["italic_voice"]}">'
                    f'<prosody rate="slow" pitch="low">'
                    f'<emphasis level="moderate">{italic_text}</emphasis>'
                    f'</prosody></voice>'
                )
                ssml_parts.append(f'<break time="{self.speech_settings["pause_between_sections"]}"/>')
            
            # Add pause between pages
            if page_num < len(text_data['pages']):
                ssml_parts.append(f'<break time="{self.speech_settings["pause_between_pages"]}"/>')
        
        ssml_parts.append('</speak>')
        
        ssml_content = ''.join(ssml_parts)
        
        # Clean up the SSML
        ssml_content = self._clean_ssml(ssml_content)
        
        return ssml_content
    
    def _process_bracketed_content(self, text: str, voice_config: Dict) -> str:
        """Process text to handle bracketed content with different voice"""
        # Find all bracketed content [like this]
        bracket_pattern = r'\[([^\]]+)\]'
        
        def replace_bracket(match):
            bracket_content = match.group(1)
            return (f'</prosody></voice>'
                   f'<voice name="{voice_config["bracket_voice"]}">'
                   f'<prosody rate="slow" pitch="high">'
                   f'<emphasis level="strong">{bracket_content}</emphasis>'
                   f'</prosody></voice>'
                   f'<voice name="{voice_config["normal_voice"]}">'
                   f'<prosody rate="{self.speech_settings["rate"]}" '
                   f'pitch="{self.speech_settings["pitch"]}">')
        
        processed_text = re.sub(bracket_pattern, replace_bracket, text)
        return processed_text
    
    def _clean_ssml(self, ssml: str) -> str:
        """Clean up SSML content"""
        # Remove empty voice tags
        ssml = re.sub(r'<voice[^>]*></voice>', '', ssml)
        
        # Remove empty prosody tags
        ssml = re.sub(r'<prosody[^>]*></prosody>', '', ssml)
        
        # Remove multiple consecutive breaks
        ssml = re.sub(r'(<break[^>]*/>[\s]*){2,}', r'<break time="2s"/>', ssml)
        
        # Clean up whitespace
        ssml = re.sub(r'\s+', ' ', ssml)
        
        return ssml.strip()
    
    def _create_audio_polly(self, ssml_content: str, output_name: str, 
                           voice_config: Dict) -> str:
        """Create audio using Amazon Polly (requires AWS credentials)"""
        try:
            import boto3
            
            # Initialize Polly client
            polly = boto3.client('polly')
            
            # Generate speech
            response = polly.synthesize_speech(
                Text=ssml_content,
                OutputFormat='mp3',
                VoiceId=voice_config['normal_voice'],
                Engine=voice_config.get('engine', 'neural'),
                TextType='ssml'
            )
            
            # Save audio file
            output_path = self.audio_dir / f"{output_name}.mp3"
            with open(output_path, 'wb') as file:
                file.write(response['AudioStream'].read())
            
            return str(output_path)
            
        except ImportError:
            logger.warning("boto3 not installed. Falling back to local TTS.")
            return self._create_audio_local(ssml_content, output_name, voice_config)
        except Exception as e:
            logger.error(f"Polly TTS failed: {e}")
            return self._create_audio_local(ssml_content, output_name, voice_config)
    
    def _create_audio_google(self, ssml_content: str, output_name: str, 
                            voice_config: Dict) -> str:
        """Create audio using Google Cloud TTS (requires API key)"""
        try:
            from google.cloud import texttospeech
            
            # Initialize client
            client = texttospeech.TextToSpeechClient()
            
            # Configure synthesis input
            synthesis_input = texttospeech.SynthesisInput(ssml=ssml_content)
            
            # Configure voice
            voice = texttospeech.VoiceSelectionParams(
                language_code="en-US",
                name=voice_config['normal_voice']
            )
            
            # Configure audio
            audio_config = texttospeech.AudioConfig(
                audio_encoding=texttospeech.AudioEncoding.MP3