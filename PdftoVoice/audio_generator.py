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
from typing import Dict, List, Optional, Tuple, Callable
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
            },
            'local': {
                'normal_voice': 'default',
                'italic_voice': 'default',
                'bracket_voice': 'default'
            }
        }
        
        # Default speech settings
        self.speech_settings = {
            'rate': 'slow',
            'pitch': 'medium',
            'volume': 'medium',
            'pause_between_sections': '1s',
            'pause_between_pages': '2s'
        }
        
    def create_audio(self, text_data: Dict, output_name: str, 
                    voice_config: Optional[Dict] = None) -> str:
        """Create audio file from processed text data"""
        logger.info(f"Creating audio file: {output_name}")
        
        if voice_config:
            current_config = voice_config
        else:
            current_config = self.voice_configs.get(self.tts_service, self.voice_configs['local'])
        
        ssml_content = self._create_ssml_content(text_data, current_config)
        
        if self.tts_service == 'polly':
            audio_file = self._create_audio_polly(ssml_content, output_name, current_config)
        elif self.tts_service == 'google':
            audio_file = self._create_audio_google(ssml_content, output_name, current_config)
        elif self.tts_service == 'elevenlabs':
            audio_file = self._create_audio_elevenlabs(ssml_content, output_name, current_config)
        else:
            audio_file = self._create_audio_local(ssml_content, output_name, current_config)
        
        logger.info(f"Audio file created: {audio_file}")
        return audio_file
    
    def create_multi_voice_audio(self, text_data: Dict, output_name: str) -> str:
        """Create audio with multiple voices for different text types"""
        return self.create_audio(text_data, output_name)
    
    def create_audio_with_progress(self, text_data: Dict, output_name: str, 
                                 progress_callback: Callable[[int, str], None]) -> str:
        """Create audio with progress tracking"""
        progress_callback(10, "Generating SSML content...")
        
        current_config = self.voice_configs.get(self.tts_service, self.voice_configs['local'])
        ssml_content = self._create_ssml_content(text_data, current_config)
        
        progress_callback(50, "Converting text to speech...")
        
        if self.tts_service == 'polly':
            audio_file = self._create_audio_polly(ssml_content, output_name, current_config)
        elif self.tts_service == 'google':
            audio_file = self._create_audio_google(ssml_content, output_name, current_config)
        elif self.tts_service == 'elevenlabs':
            audio_file = self._create_audio_elevenlabs(ssml_content, output_name, current_config)
        else:
            audio_file = self._create_audio_local(ssml_content, output_name, current_config)
        
        progress_callback(100, "Audio generation complete!")
        return audio_file
    
    def optimize_audio_quality(self, audio_file: str) -> str:
        """Optimize audio quality with normalization and compression"""
        try:
            from pydub import AudioSegment
            from pydub.effects import normalize, compress_dynamic_range
            
            logger.info(f"Optimizing audio quality for: {audio_file}")
            
            # Load audio
            audio = AudioSegment.from_mp3(audio_file)
            
            # Normalize volume
            audio = normalize(audio)
            
            # Apply light compression
            audio = compress_dynamic_range(audio, threshold=-20.0, ratio=4.0, attack=5.0, release=50.0)
            
            # Export optimized version
            optimized_path = audio_file.replace('.mp3', '_optimized.mp3')
            audio.export(optimized_path, format="mp3", bitrate="128k")
            
            logger.info(f"Optimized audio saved: {optimized_path}")
            return optimized_path
            
        except ImportError:
            logger.warning("pydub not installed. Cannot optimize audio quality.")
            return audio_file
        except Exception as e:
            logger.error(f"Audio optimization failed: {e}")
            return audio_file
    
    def estimate_audio_duration(self, text_data: Dict) -> float:
        """Estimate audio duration in seconds based on text length"""
        total_chars = 0
        for page_data in text_data['pages']:
            total_chars += len(page_data.get('regular_text', ''))
            total_chars += len(page_data.get('italic_text', ''))
        
        # Average reading speed: ~150 words per minute, ~5 chars per word
        chars_per_minute = 150 * 5
        estimated_minutes = total_chars / chars_per_minute
        
        # Add time for pauses and slower speech
        estimated_seconds = estimated_minutes * 60 * 1.3  # 30% longer for natural speech
        
        return estimated_seconds
    
    def get_available_voices(self) -> List[str]:
        """Get list of available voices for current TTS service"""
        if self.tts_service == 'polly':
            return self._get_polly_voices()
        elif self.tts_service == 'google':
            return self._get_google_voices()
        elif self.tts_service == 'elevenlabs':
            return self._get_elevenlabs_voices()
        else:
            return self._get_local_voices()
    
    def preview_ssml(self, text_data: Dict) -> str:
        """Preview the generated SSML content"""
        current_config = self.voice_configs.get(self.tts_service, self.voice_configs['local'])
        return self._create_ssml_content(text_data, current_config)
    
    def create_chapter_markers(self, text_data: Dict, output_name: str) -> str:
        """Create chapter markers for audio players"""
        markers = []
        current_time = 0.0
        
        for page_num, page_data in enumerate(text_data['pages'], 1):
            regular_text = page_data.get('regular_text', '')
            italic_text = page_data.get('italic_text', '')
            
            if regular_text or italic_text:
                # Estimate time for this page
                page_chars = len(regular_text) + len(italic_text)
                page_duration = (page_chars / (150 * 5)) * 60 * 1.3
                
                markers.append({
                    'time': current_time,
                    'title': f'Page {page_num}',
                    'text_preview': (regular_text[:50] + '...') if len(regular_text) > 50 else regular_text
                })
                
                current_time += page_duration
        
        # Save markers as JSON
        markers_file = self.audio_dir / f"{output_name}_chapters.json"
        with open(markers_file, 'w', encoding='utf-8') as f:
            json.dump(markers, f, indent=2, ensure_ascii=False)
        
        # Save as WebVTT for web players
        vtt_file = self.audio_dir / f"{output_name}_chapters.vtt"
        with open(vtt_file, 'w', encoding='utf-8') as f:
            f.write("WEBVTT\n\n")
            for i, marker in enumerate(markers):
                start_time = self._seconds_to_vtt_time(marker['time'])
                end_time = self._seconds_to_vtt_time(marker['time'] + 30)  # 30-second chapters
                f.write(f"{i+1}\n{start_time} --> {end_time}\n{marker['title']}\n\n")
        
        logger.info(f"Chapter markers saved: {markers_file}")
        return str(markers_file)
    
    def batch_process_pdfs(self, pdf_files: List[str], processor) -> List[str]:
        """Process multiple PDFs in batch"""
        audio_files = []
        
        for pdf_file in pdf_files:
            try:
                logger.info(f"Processing: {pdf_file}")
                
                # Process PDF
                html_content, text_data = processor.process_pdf(pdf_file)
                
                # Generate audio
                output_name = Path(pdf_file).stem
                audio_file = self.create_audio(text_data, output_name)
                audio_files.append(audio_file)
                
            except Exception as e:
                logger.error(f"Failed to process {pdf_file}: {e}")
                
        return audio_files
    
    def _create_ssml_content(self, text_data: Dict, voice_config: Dict) -> str:
        """Create SSML content with different voices for different text types"""
        ssml_parts = ['<speak>']
        ssml_parts.append('<break time="1s"/>')
        
        for page_num, page_data in enumerate(text_data['pages'], 1):
            if len(text_data['pages']) > 1:
                ssml_parts.append(
                    f'<voice name="{voice_config["normal_voice"]}">'
                    f'<break time="0.5s"/>Page {page_num}<break time="1s"/>'
                    f'</voice>'
                )
            
            regular_text = page_data.get('regular_text', '').strip()
            if regular_text:
                regular_text = self._process_bracketed_content(regular_text, voice_config)
                ssml_parts.append(
                    f'<voice name="{voice_config["normal_voice"]}">'
                    f'<prosody rate="{self.speech_settings["rate"]}" '
                    f'pitch="{self.speech_settings["pitch"]}">'
                    f'{regular_text}'
                    f'</prosody></voice>'
                )
                ssml_parts.append(f'<break time="{self.speech_settings["pause_between_sections"]}"/>')
            
            italic_text = page_data.get('italic_text', '').strip()
            if italic_text:
                ssml_parts.append(
                    f'<voice name="{voice_config["italic_voice"]}">'
                    f'<prosody rate="slow" pitch="low">'
                    f'<emphasis level="moderate">{italic_text}</emphasis>'
                    f'</prosody></voice>'
                )
                ssml_parts.append(f'<break time="{self.speech_settings["pause_between_sections"]}"/>')
            
            if page_num < len(text_data['pages']):
                ssml_parts.append(f'<break time="{self.speech_settings["pause_between_pages"]}"/>')
        
        ssml_parts.append('</speak>')
        ssml_content = ''.join(ssml_parts)
        return self._clean_ssml(ssml_content)
    
    def _process_bracketed_content(self, text: str, voice_config: Dict) -> str:
        """Process text to handle bracketed content with different voice"""
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
        
        return re.sub(bracket_pattern, replace_bracket, text)
    
    def _clean_ssml(self, ssml: str) -> str:
        """Clean up SSML content"""
        ssml = re.sub(r'<voice[^>]*></voice>', '', ssml)
        ssml = re.sub(r'<prosody[^>]*></prosody>', '', ssml)
        ssml = re.sub(r'(<break[^>]*/>[\s]*){2,}', r'<break time="2s"/>', ssml)
        ssml = re.sub(r'\s+', ' ', ssml)
        return ssml.strip()
    
    def _create_audio_polly(self, ssml_content: str, output_name: str, voice_config: Dict) -> str:
        """Create audio using Amazon Polly"""
        try:
            import boto3
            polly = boto3.client('polly')
            
            response = polly.synthesize_speech(
                Text=ssml_content,
                OutputFormat='mp3',
                VoiceId=voice_config['normal_voice'],
                Engine=voice_config.get('engine', 'neural'),
                TextType='ssml'
            )
            
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
    
    def _create_audio_google(self, ssml_content: str, output_name: str, voice_config: Dict) -> str:
        """Create audio using Google Cloud TTS"""
        try:
            from google.cloud import texttospeech
            
            client = texttospeech.TextToSpeechClient()
            synthesis_input = texttospeech.SynthesisInput(ssml=ssml_content)
            
            voice = texttospeech.VoiceSelectionParams(
                language_code="en-US",
                name=voice_config['normal_voice']
            )
            
            audio_config = texttospeech.AudioConfig(
                audio_encoding=texttospeech.AudioEncoding.MP3
            )
            
            response = client.synthesize_speech(
                input=synthesis_input,
                voice=voice,
                audio_config=audio_config
            )
            
            output_path = self.audio_dir / f"{output_name}.mp3"
            with open(output_path, 'wb') as file:
                file.write(response.audio_content)
            
            return str(output_path)
            
        except ImportError:
            logger.warning("Google Cloud TTS not available. Falling back to local TTS.")
            return self._create_audio_local(ssml_content, output_name, voice_config)
        except Exception as e:
            logger.error(f"Google TTS failed: {e}")
            return self._create_audio_local(ssml_content, output_name, voice_config)
    
    def _create_audio_elevenlabs(self, ssml_content: str, output_name: str, voice_config: Dict) -> str:
        """Create audio using ElevenLabs TTS"""
        try:
            import requests
            
            # Convert SSML to plain text for ElevenLabs
            plain_text = self._ssml_to_plain_text(ssml_content)
            
            # ElevenLabs API call would go here
            # For now, fall back to local TTS
            logger.warning("ElevenLabs TTS not fully implemented. Using local TTS.")
            return self._create_audio_local(ssml_content, output_name, voice_config)
            
        except Exception as e:
            logger.error(f"ElevenLabs TTS failed: {e}")
            return self._create_audio_local(ssml_content, output_name, voice_config)
    
    def _create_audio_local(self, ssml_content: str, output_name: str, voice_config: Dict) -> str:
        """Create audio using local TTS (pyttsx3 or espeak)"""
        try:
            import pyttsx3
            
            # Convert SSML to plain text
            plain_text = self._ssml_to_plain_text(ssml_content)
            
            # Initialize TTS engine
            engine = pyttsx3.init()
            
            # Configure voice settings
            voices = engine.getProperty('voices')
            if voices:
                engine.setProperty('voice', voices[0].id)
            
            engine.setProperty('rate', 150)  # Speed
            engine.setProperty('volume', 0.9)  # Volume
            
            # Save to file
            output_path = self.audio_dir / f"{output_name}.mp3"
            engine.save_to_file(plain_text, str(output_path))
            engine.runAndWait()
            
            return str(output_path)
            
        except ImportError:
            logger.error("pyttsx3 not installed. Cannot create local TTS.")
            # Create a placeholder file
            output_path = self.audio_dir / f"{output_name}_placeholder.txt"
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write("TTS audio would be generated here.\n")
                f.write(f"Text content:\n{self._ssml_to_plain_text(ssml_content)}")
            return str(output_path)
        except Exception as e:
            logger.error(f"Local TTS failed: {e}")
            # Create a placeholder file
            output_path = self.audio_dir / f"{output_name}_error.txt"
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(f"TTS generation failed: {e}\n")
                f.write(f"Text content:\n{self._ssml_to_plain_text(ssml_content)}")
            return str(output_path)
    
    def _ssml_to_plain_text(self, ssml_content: str) -> str:
        """Convert SSML to plain text by removing tags"""
        # Remove SSML tags
        plain_text = re.sub(r'<[^>]+>', '', ssml_content)
        # Clean up whitespace
        plain_text = re.sub(r'\s+', ' ', plain_text)
        return plain_text.strip()
    
    def _get_polly_voices(self) -> List[str]:
        """Get available Polly voices"""
        try:
            import boto3
            polly = boto3.client('polly')
            response = polly.describe_voices()
            return [voice['Id'] for voice in response['Voices'] if voice['LanguageCode'].startswith('en')]
        except Exception:
            return ['Joanna', 'Matthew', 'Amy', 'Brian', 'Emma']
    
    def _get_google_voices(self) -> List[str]:
        """Get available Google voices"""
        return ['en-US-Standard-A', 'en-US-Standard-B', 'en-US-Standard-C', 'en-US-Standard-D']
    
    def _get_elevenlabs_voices(self) -> List[str]:
        """Get available ElevenLabs voices"""
        return ['Rachel', 'Drew', 'Clyde', 'Paul', 'Domi']
    
    def _get_local_voices(self) -> List[str]:
        """Get available local voices"""
        try:
            import pyttsx3
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')
            return [voice.id for voice in voices] if voices else ['default']
        except Exception:
            return ['default']
    
    def _seconds_to_vtt_time(self, seconds: float) -> str:
        """Convert seconds to VTT time format"""
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = seconds % 60
        return f"{hours:02d}:{minutes:02d}:{secs:06.3f}"


# Test the AudioGenerator
if __name__ == "__main__":
    print("🎵 Testing Audio Generator...")
    
    # Test data
    sample_text_data = {
        'pages': [
            {
                'regular_text': 'This is regular text with [bracketed content] for testing.',
                'italic_text': 'This is italic text that should be spoken differently.'
            }
        ]
    }
    
    # Initialize generator
    audio_gen = AudioGenerator(tts_service='local')
    
    # Test available voices
    print(f"📢 Available voices: {audio_gen.get_available_voices()[:3]}")
    
    # Test SSML preview
    ssml = audio_gen.preview_ssml(sample_text_data)
    print(f"📝 SSML preview (first 200 chars): {ssml[:200]}...")
    
    # Test duration estimation
    duration = audio_gen.estimate_audio_duration(sample_text_data)
    print(f"⏱️ Estimated duration: {duration:.1f} seconds")
    
    # Test audio creation
    audio_file = audio_gen.create_audio(sample_text_data, "test_audio")
    print(f"🎵 Audio file created: {audio_file}")
    
    # Test chapter markers
    markers_file = audio_gen.create_chapter_markers(sample_text_data, "test_chapters")
    print(f"📑 Chapter markers: {markers_file}")
    
    print("✅ Audio Generator test complete!")