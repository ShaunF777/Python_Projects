# 📚 PDF-to-Voice Converter 🎧

<div align="center">
  <h2>🔊 Transform your scanned PDFs into beautiful audio experiences! 🎵</h2>
  <p><em>Advanced OCR + Multi-voice TTS = Amazing audiobooks from your PDFs!</em></p>
</div>

## 🚀 What This Project Does

This Python toolkit converts scanned PDF documents into high-quality audio files with intelligent voice variations:

- **📖 OCR Magic**: Extracts text from scanned PDFs with italic detection
- **🎭 Multi-Voice TTS**: Different voices for regular text, italics, and bracketed content
- **🎨 HTML Preview**: Creates formatted HTML files for review before audio generation
- **🔊 Smart Speech**: Uses SSML for natural pauses, emphasis, and pacing
- **⚡ Batch Processing**: Handle multiple PDFs automatically
- **🎵 Professional Audio**: Supports AWS Polly, Google Cloud TTS, ElevenLabs, and local TTS

## 📁 Project Structure

```
pdf-to-voice/
├── main.py              # Master program - orchestrates everything
├── pdf_processor.py     # PDF → HTML → structured text
├── audio_generator.py   # Text → audio with multiple voices
├── README.md           # This file
├── requirements.txt    # Python dependencies
├── input/              # Put your PDF files here
│   └── your-book.pdf
├── output/
│   ├── html/          # HTML preview files
│   └── audio/         # Generated MP3 files
└── config/
    └── credentials.json # API keys (create this)
```

## 🛠️ Installation & Setup

### Step 1: System Dependencies

**Ubuntu/Debian:**
```bash
sudo apt-get update
sudo apt-get install tesseract-ocr tesseract-ocr-eng
sudo apt-get install poppler-utils
sudo apt-get install ffmpeg  # For audio processing
```

**macOS:**
```bash
brew install tesseract
brew install poppler
brew install ffmpeg
```

**Windows:**
```bash
# Install Tesseract from: https://github.com/UB-Mannheim/tesseract/wiki
# Add tesseract to your PATH
# Install poppler from: https://github.com/oschwartz10612/poppler-windows
```

### Step 2: Python Dependencies

```bash
# Core dependencies
pip install pytesseract pdf2image pillow easyocr
pip install beautifulsoup4 lxml requests
pip install pydub pyttsx3

# Cloud TTS services (optional)
pip install boto3                    # AWS Polly
pip install google-cloud-texttospeech  # Google Cloud TTS
pip install elevenlabs              # ElevenLabs TTS

# Audio processing
pip install numpy scipy
```

**Or install everything at once:**
```bash
pip install -r requirements.txt
```

### Step 3: API Keys & Accounts (Optional)

The system works with local TTS by default, but cloud services provide better quality:

#### 🔶 AWS Polly (Recommended)
1. **Create account**: [AWS Console](https://aws.amazon.com/console/)
2. **Create IAM user** with `AmazonPollyFullAccess` permission
3. **Get credentials**: Access Key ID + Secret Access Key
4. **Configure**:
   ```bash
   aws configure
   # OR set environment variables:
   export AWS_ACCESS_KEY_ID="your-key"
   export AWS_SECRET_ACCESS_KEY="your-secret"
   export AWS_DEFAULT_REGION="us-east-1"
   ```

#### 🔵 Google Cloud TTS
1. **Create project**: [Google Cloud Console](https://console.cloud.google.com/)
2. **Enable** Text-to-Speech API
3. **Create service account** and download JSON key
4. **Set environment variable**:
   ```bash
   export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/key.json"
   ```

#### 🟣 ElevenLabs (Premium)
1. **Sign up**: [ElevenLabs](https://elevenlabs.io/)
2. **Get API key** from dashboard
3. **Set environment variable**:
   ```bash
   export ELEVENLABS_API_KEY="your-api-key"
   ```

## 🎯 Quick Start

### Basic Usage (Local TTS)
```python
from pdf_processor import PDFProcessor
from audio_generator import AudioGenerator

# Initialize
processor = PDFProcessor()
audio_gen = AudioGenerator(tts_service='local')

# Process PDF
html_content, text_data = processor.process_pdf("input/your-book.pdf")

# Review HTML first
html_file = processor.save_html(html_content, "your-book")
print(f"📄 Review HTML: {html_file}")

# Create audio
audio_file = audio_gen.create_audio(text_data, "your-book")
print(f"🎵 Audio created: {audio_file}")
```

### Advanced Usage (Cloud TTS)
```python
# Use AWS Polly with custom voices
audio_gen = AudioGenerator(tts_service='polly')

# Custom voice configuration
custom_voices = {
    'normal_voice': 'Joanna',    # Main narrator
    'italic_voice': 'Matthew',   # For italic text
    'bracket_voice': 'Amy',      # For [bracketed] content
    'engine': 'neural'           # Better quality
}

audio_file = audio_gen.create_audio(
    text_data, 
    "your-book-premium", 
    voice_config=custom_voices
)
```

## 📚 Complete Function Reference

### PDFProcessor Class

#### Core Methods
- **`process_pdf(pdf_path)`** - Main processing function
  - Converts PDF → images → OCR → structured text
  - Returns: `(html_content, text_data)`

- **`save_html(html_content, filename)`** - Save HTML preview
  - Creates formatted HTML file for review
  - Returns: path to HTML file

#### Advanced Methods
- **`process_with_easyocr(pdf_path)`** - Alternative OCR engine
- **`extract_text_with_formatting(pdf_path)`** - Preserve formatting
- **`batch_process_directory(directory_path)`** - Process multiple PDFs

### AudioGenerator Class

#### Core Audio Creation
- **`create_audio(text_data, output_name, voice_config=None)`**
  - Basic audio generation
  - Returns: path to MP3 file

- **`create_multi_voice_audio(text_data, output_name)`**
  - Different voices for different text types
  - Uses italic_voice for italic text, bracket_voice for [bracketed] content

- **`create_audio_with_progress(text_data, output_name, progress_callback)`**
  - Audio generation with progress tracking
  - Useful for GUI applications

#### Audio Enhancement
- **`optimize_audio_quality(audio_file)`**
  - Normalizes volume, applies compression
  - Returns: path to optimized file

- **`create_chapter_markers(text_data, output_name)`**
  - Creates chapter markers for audio players
  - Generates JSON and WebVTT formats

#### Utility Functions
- **`estimate_audio_duration(text_data)`** - Estimate final audio length
- **`get_available_voices()`** - List available TTS voices
- **`preview_ssml(text_data)`** - Show generated SSML for debugging
- **`batch_process_pdfs(pdf_files, processor)`** - Process multiple PDFs

## 🧪 Testing Guide

### Test 1: System Dependencies
```bash
# Test Tesseract
tesseract --version

# Test Poppler
pdftoppm -h

# Test Python imports
python -c "import pytesseract, pdf2image, PIL; print('✅ All imports work')"
```

### Test 2: PDF Processing
```python
# Test with a simple PDF
from pdf_processor import PDFProcessor

processor = PDFProcessor()

# Test basic processing
html_content, text_data = processor.process_pdf("input/test.pdf")
print(f"📄 Extracted {len(text_data['pages'])} pages")
print(f"📝 First 100 chars: {text_data['pages'][0]['regular_text'][:100]}")

# Save HTML for review
html_file = processor.save_html(html_content, "test")
print(f"✅ HTML saved: {html_file}")
```

### Test 3: Audio Generation (Local)
```python
# Test local TTS
from audio_generator import AudioGenerator

audio_gen = AudioGenerator(tts_service='local')

# Test available voices
voices = audio_gen.get_available_voices()
print(f"🎤 Available voices: {voices}")

# Test audio creation
sample_data = {
    'pages': [
        {
            'regular_text': 'This is a test sentence with [bracketed content].',
            'italic_text': 'This is italic text that should sound different.'
        }
    ]
}

audio_file = audio_gen.create_audio(sample_data, "test_audio")
print(f"🎵 Test audio: {audio_file}")
```

### Test 4: Cloud TTS Services
```python
# Test AWS Polly
audio_gen_polly = AudioGenerator(tts_service='polly')
try:
    voices = audio_gen_polly.get_available_voices()
    print(f"✅ Polly voices: {voices[:5]}")
except Exception as e:
    print(f"❌ Polly test failed: {e}")

# Test Google Cloud TTS
audio_gen_google = AudioGenerator(tts_service='google')
try:
    voices = audio_gen_google.get_available_voices()
    print(f"✅ Google voices: {voices[:5]}")
except Exception as e:
    print(f"❌ Google test failed: {e}")
```

### Test 5: Complete Workflow
```python
# Full end-to-end test
from pdf_processor import PDFProcessor
from audio_generator import AudioGenerator

def test_complete_workflow():
    # Initialize
    processor = PDFProcessor()
    audio_gen = AudioGenerator(tts_service='local')  # Change to 'polly' if configured
    
    # Process PDF
    print("📄 Processing PDF...")
    html_content, text_data = processor.process_pdf("input/your-test.pdf")
    
    # Save HTML
    print("💾 Saving HTML preview...")
    html_file = processor.save_html(html_content, "complete_test")
    
    # Estimate duration
    duration = audio_gen.estimate_audio_duration(text_data)
    print(f"⏱️ Estimated audio duration: {duration/60:.1f} minutes")
    
    # Create audio
    print("🎵 Generating audio...")
    audio_file = audio_gen.create_audio(text_data, "complete_test")
    
    # Create chapter markers
    print("📑 Creating chapter markers...")
    markers_file = audio_gen.create_chapter_markers(text_data, "complete_test")
    
    print("✅ Complete workflow test successful!")
    print(f"   HTML: {html_file}")
    print(f"   Audio: {audio_file}")
    print(f"   Markers: {markers_file}")

# Run the test
test_complete_workflow()
```

## 🔧 Troubleshooting

### Common Issues

**"Tesseract not found"**
```bash
# Ubuntu/Debian
sudo apt-get install tesseract-ocr

# macOS
brew install tesseract

# Windows: Add tesseract to PATH
```

**"No module named 'pdf2image'"**
```bash
pip install pdf2image
# Also install poppler-utils (see system dependencies)
```

**"AWS credentials not found"**
```bash
aws configure
# OR set environment variables
export AWS_ACCESS_KEY_ID="your-key"
export AWS_SECRET_ACCESS_KEY="your-secret"
```

**"Google Cloud authentication failed"**
```bash
export GOOGLE_APPLICATION_CREDENTIALS="path/to/service-account.json"
```

**"Audio quality is poor"**
```python
# Use neural voices for better quality
voice_config = {
    'normal_voice': 'Joanna',
    'engine': 'neural'  # Much better than 'standard'
}

# Or optimize after generation
optimized_file = audio_gen.optimize_audio_quality(audio_file)
```

## 🎪 Advanced Features

### Custom Voice Configurations
```python
# Professional audiobook setup
audiobook_config = {
    'normal_voice': 'Joanna',      # Warm, professional narrator
    'italic_voice': 'Matthew',     # Distinct male voice for emphasis
    'bracket_voice': 'Amy',        # Clear voice for annotations
    'engine': 'neural',            # Best quality
    'rate': 'slow',                # Comfortable listening pace
    'pitch': 'medium',
    'volume': 'medium'
}
```

### Batch Processing
```python
# Process multiple PDFs
from pathlib import Path

pdf_files = list(Path("input").glob("*.pdf"))
audio_files = audio_gen.batch_process_pdfs(pdf_files, processor)
print(f"✅ Processed {len(audio_files)} files")
```

### Progress Tracking
```python
def progress_callback(percent, message):
    print(f"Progress: {percent}% - {message}")

audio_file = audio_gen.create_audio_with_progress(
    text_data, 
    "chapter_with_progress", 
    progress_callback
)
```

## 🎯 Best Practices

1. **Always review HTML output** before generating audio
2. **Test with small PDFs first** to verify OCR quality
3. **Use neural voices** for better audio quality
4. **Estimate duration** before long audio generation
5. **Optimize audio** for final production files
6. **Create chapter markers** for better navigation

## 📈 Performance Tips

- **PDF Quality**: Higher resolution PDFs = better OCR accuracy
- **Page Limits**: Process large books in chapters for better memory usage
- **Voice Selection**: Neural voices are slower but much higher quality
- **Batch Processing**: Use for multiple similar documents

## 🤝 Contributing

Found a bug? Want to add a feature? Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## 📜 License

MIT License - feel free to use this project for personal or commercial purposes.

---

<div align="center">
  <h3>🎉 Happy PDF-to-Voice Converting! 🎉</h3>
  <p>Made with ❤️ for audiobook lovers everywhere</p>
  <p><em>Now go turn those dusty PDFs into amazing audio experiences! 🎧</em></p>
</div>