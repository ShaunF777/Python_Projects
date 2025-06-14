#!/usr/bin/env python3
"""
PDF Processor - Extract text from scanned PDFs with OCR
Preserves italic formatting and creates HTML output
"""

import os
import re
from pathlib import Path
from typing import Tuple, List, Dict
import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import easyocr
from bs4 import BeautifulSoup
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class PDFProcessor:
    def __init__(self):
        """Initialize PDF processor with OCR settings"""
        self.output_dir = Path("output")
        self.html_dir = self.output_dir / "html"
        self.html_dir.mkdir(parents=True, exist_ok=True)
        
        # Initialize EasyOCR reader (supports multiple languages)
        self.reader = easyocr.Reader(['en'])
        
        # Tesseract configuration for better OCR
        self.tesseract_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
        
    def convert_pdf_to_images(self, pdf_path: str, dpi: int = 300) -> List[Image.Image]:
        """Convert PDF pages to high-quality images"""
        logger.info(f"Converting PDF to images: {pdf_path}")
        try:
            images = convert_from_path(pdf_path, dpi=dpi)
            logger.info(f"Successfully converted {len(images)} pages")
            return images
        except Exception as e:
            logger.error(f"Error converting PDF: {e}")
            raise
    
    def detect_italic_text(self, image: Image.Image) -> Dict[str, List]:
        """
        Detect italic text using multiple OCR approaches
        Returns dictionary with regular text and italic text segments
        """
        # Method 1: Use Tesseract with HOCR output
        hocr_data = pytesseract.image_to_pdf_or_hocr(
            image, extension='hocr', config=self.tesseract_config
        )
        
        # Method 2: Use EasyOCR for additional text detection
        easyocr_results = self.reader.readtext(image)
        
        # Parse HOCR for italic detection
        soup = BeautifulSoup(hocr_data, 'html.parser')
        
        text_segments = {
            'regular': [],
            'italic': [],
            'coordinates': []
        }
        
        # Extract text with formatting info from HOCR
        for word in soup.find_all('span', class_='ocrx_word'):
            word_text = word.get_text().strip()
            if word_text:
                # Check for italic indicators in the word's properties
                title = word.get('title', '')
                
                # Simple heuristic: check if the text appears slanted or has italic characteristics
                # This is a simplified approach - more sophisticated methods could be used
                is_italic = self._is_likely_italic(word_text, title)
                
                if is_italic:
                    text_segments['italic'].append(word_text)
                else:
                    text_segments['regular'].append(word_text)
        
        # Fallback: if no text detected via HOCR, use EasyOCR
        if not text_segments['regular'] and not text_segments['italic']:
            for (bbox, text, confidence) in easyocr_results:
                if confidence > 0.5:  # Only use high-confidence results
                    # Simple italic detection based on text patterns
                    if self._is_likely_italic_pattern(text):
                        text_segments['italic'].append(text)
                    else:
                        text_segments['regular'].append(text)
        
        return text_segments
    
    def _is_likely_italic(self, text: str, title: str) -> bool:
        """
        Heuristic to determine if text is likely italic
        This is a simplified approach - could be enhanced with ML models
        """
        # Check for common italic patterns
        italic_patterns = [
            r'^\*.*\*$',  # Surrounded by asterisks
            r'^_.*_$',    # Surrounded by underscores
            r'^\[.*\]$',  # Text in brackets (often emphasis)
        ]
        
        for pattern in italic_patterns:
            if re.match(pattern, text):
                return True
        
        # Check if title contains italic-related font information
        if 'italic' in title.lower() or 'oblique' in title.lower():
            return True
        
        return False
    
    def _is_likely_italic_pattern(self, text: str) -> bool:
        """Check if text matches common italic patterns"""
        # Common patterns that indicate italic text
        patterns = [
            r'^\*.*\*$',      # *italic*
            r'^_.*_$',        # _italic_
            r'^\[.*\]$',      # [bracketed text]
            r'^\(.*\)$',      # (parenthetical)
        ]
        
        for pattern in patterns:
            if re.match(pattern, text.strip()):
                return True
        
        # Check for common italic words/phrases
        italic_indicators = [
            'note:', 'important:', 'warning:', 'emphasis:',
            'see also', 'cf.', 'i.e.', 'e.g.', 'etc.'
        ]
        
        text_lower = text.lower().strip()
        for indicator in italic_indicators:
            if text_lower.startswith(indicator):
                return True
        
        return False
    
    def process_pdf(self, pdf_path: str) -> Tuple[str, Dict]:
        """
        Main processing function
        Returns HTML content and structured text data
        """
        logger.info(f"Processing PDF: {pdf_path}")
        
        # Convert PDF to images
        images = self.convert_pdf_to_images(pdf_path)
        
        all_text_data = {
            'regular': [],
            'italic': [],
            'pages': []
        }
        
        html_content = []
        html_content.append(self._get_html_header())
        
        # Process each page
        for page_num, image in enumerate(images, 1):
            logger.info(f"Processing page {page_num}/{len(images)}")
            
            # Extract text with formatting
            text_segments = self.detect_italic_text(image)
            
            # Add page data
            page_data = {
                'page_number': page_num,
                'regular_text': ' '.join(text_segments['regular']),
                'italic_text': ' '.join(text_segments['italic'])
            }
            all_text_data['pages'].append(page_data)
            all_text_data['regular'].extend(text_segments['regular'])
            all_text_data['italic'].extend(text_segments['italic'])
            
            # Create HTML for this page
            page_html = self._create_page_html(page_num, text_segments)
            html_content.append(page_html)
        
        html_content.append(self._get_html_footer())
        
        final_html = '\n'.join(html_content)
        
        logger.info("PDF processing completed successfully")
        return final_html, all_text_data
    
    def _get_html_header(self) -> str:
        """Generate HTML header with styling"""
        return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Extracted Text from PDF</title>
    <style>
        body {
            font-family: 'Georgia', serif;
            line-height: 1.6;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f9f9f9;
        }
        .page {
            background: white;
            padding: 30px;
            margin: 20px 0;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        .page-number {
            text-align: center;
            color: #666;
            font-size: 14px;
            margin-bottom: 20px;
            border-bottom: 1px solid #eee;
            padding-bottom: 10px;
        }
        .regular-text {
            font-size: 16px;
            color: #333;
            margin-bottom: 15px;
        }
        .italic-text {
            font-style: italic;
            color: #555;
            background-color: #f0f8ff;
            padding: 8px 12px;
            border-left: 4px solid #4a90e2;
            margin: 10px 0;
            border-radius: 4px;
        }
        .bracket-text {
            font-style: italic;
            color: #8B4513;
            background-color: #fff8dc;
            padding: 4px 8px;
            border-radius: 3px;
        }
        h1 {
            color: #2c3e50;
            text-align: center;
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
        }
    </style>
</head>
<body>
    <h1>📚 Extracted Text Document</h1>
"""
    
    def _create_page_html(self, page_num: int, text_segments: Dict) -> str:
        """Create HTML for a single page"""
        html = f"""
    <div class="page">
        <div class="page-number">— Page {page_num} —</div>
"""
        
        # Add regular text
        if text_segments['regular']:
            regular_text = ' '.join(text_segments['regular'])
            # Process for bracketed content
            regular_text = self._format_bracketed_text(regular_text)
            html += f'        <div class="regular-text">{regular_text}</div>\n'
        
        # Add italic text
        if text_segments['italic']:
            for italic_text in text_segments['italic']:
                html += f'        <div class="italic-text">{italic_text}</div>\n'
        
        html += "    </div>"
        return html
    
    def _format_bracketed_text(self, text: str) -> str:
        """Format text with special styling for bracketed content"""
        # Replace [bracketed] content with special styling
        text = re.sub(
            r'\[([^\]]+)\]',
            r'<span class="bracket-text">[\1]</span>',
            text
        )
        return text
    
    def _get_html_footer(self) -> str:
        """Generate HTML footer"""
        return """
    <div style="text-align: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid #eee; color: #666;">
        <p>📄 Document processed with PDF-to-Speech Converter</p>
        <p><em>Generated with OCR technology</em></p>
    </div>
</body>
</html>"""
    
    def save_html(self, html_content: str, filename: str) -> str:
        """Save HTML content to file"""
        output_path = self.html_dir / f"{filename}.html"
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        logger.info(f"HTML saved to: {output_path}")
        return str(output_path)
    
    def get_text_for_audio(self, text_data: Dict) -> str:
        """
        Convert extracted text data to format suitable for TTS
        Includes SSML markup for different voices
        """
        ssml_parts = []
        
        for page_data in text_data['pages']:
            # Regular text
            if page_data['regular_text'].strip():
                ssml_parts.append(f'<voice name="Joanna">{page_data["regular_text"]}</voice>')
            
            # Italic text with different voice
            if page_data['italic_text'].strip():
                ssml_parts.append(
                    f'<voice name="Matthew"><prosody rate="slow">'
                    f'<emphasis level="moderate">{page_data["italic_text"]}</emphasis>'
                    f'</prosody></voice>'
                )
            
            # Add pause between pages
            ssml_parts.append('<break time="2s"/>')
        
        # Wrap in SSML speak tags
        ssml_content = f'<speak>{"".join(ssml_parts)}</speak>'
        
        return ssml_content

# Example usage
if __name__ == "__main__":
    processor = PDFProcessor()
    
    # Example usage
    pdf_path = "input/SoundDoctrineCh10.pdf"  # Update with your PDF path
    
    if os.path.exists(pdf_path):
        try:
            html_content, text_data = processor.process_pdf(pdf_path)
            
            # Save HTML
            html_file = processor.save_html(html_content, "SoundDoctrineCh10")
            print(f"✅ HTML file created: {html_file}")
            
            # Get text ready for audio processing
            ssml_text = processor.get_text_for_audio(text_data)
            print(f"✅ Text prepared for audio generation")
            print(f"📊 Stats: {len(text_data['pages'])} pages processed")
            
        except Exception as e:
            print(f"❌ Error processing PDF: {e}")
    else:
        print(f"❌ PDF file not found: {pdf_path}")
        print("Please place your PDF file in the 'input' directory")