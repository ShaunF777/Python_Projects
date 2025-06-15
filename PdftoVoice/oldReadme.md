# 📚 PDF-to-Speech Converter 🎧

<div align="center">
  <h2>🔊 Transform your scanned PDFs into beautiful audio experiences! 🎵</h2>
  
  <!-- If GitHub supports SVG animations, this would work -->
  <img src="./assets/animations/pdf-to-audio.svg" alt="PDF to Audio Animation" width="400"/>
  
  <!-- Alternative GIF animation -->
  <img src="./assets/gifs/processing.gif" alt="Processing Animation" width="300"/>
</div>

## 🚀 What does this magical tool do?

This awesome Python project takes your scanned PDF chapters and transforms them into high-quality MP3 audio files! 🎪✨

**Special Features:**
- 🤖 **OCR Magic**: Reads scanned PDFs like a human would
- 🎭 **Voice Variety**: Different voices for italic text and bracketed content
- 🎨 **HTML Output**: Creates beautiful formatted HTML files
- 🔊 **Smart TTS**: Uses advanced text-to-speech with SSML formatting

## 📁 File Structure & Asset Storage

```
your-project/
├── README.md
├── pdf_processor.py
├── audio_generator.py
├── input/
│   └── your-pdfs-here.pdf
├── output/
│   ├── html/
│   └── audio/
└── assets/
    ├── gifs/
    │   └── processing.gif
    └── animations/
        └── pdf-to-audio.svg
```

### 🎬 About GitHub HTML & Animations

<details>
<summary>Click to learn about GitHub's HTML support! 🤓</summary>

**Good news!** 📢 GitHub's markdown renderer supports **some** HTML tags, including:
- `<div>`, `<span>`, `<img>`, `<a>`
- `<h1>` through `<h6>`
- `<strong>`, `<em>`, `<code>`
- `<details>`, `<summary>`

**For animations:** 🎭
- **GIFs**: Store in `./assets/gifs/` and reference with `<img src="./assets/gifs/your-animation.gif"/>`
- **SVGs**: Store in `./assets/animations/` - but note that **animated SVGs won't work** in GitHub READMEs (security restrictions)
- **Static SVGs**: Work perfectly for icons and graphics!

**Pro tip:** 💡 Use GIFs for animations, SVGs for static graphics!

</details>

## 🛠️ Dependencies & Installation

### Prerequisites 📋
```bash
# System dependencies (Ubuntu/Debian)
sudo apt-get install tesseract-ocr
sudo apt-get install poppler-utils

# For macOS
brew install tesseract
brew install poppler
```

### Python Packages 🐍
```bash
pip install pytesseract
pip install pdf2image
pip install pillow
pip install easyocr
pip install beautifulsoup4
pip install requests
pip install pydub
```

### Quick Install Script 🚀
```bash
# Run this in your terminal
pip install pytesseract pdf2image pillow easyocr beautifulsoup4 requests pydub
```

## 🎯 Quick Start Guide

### Basic Usage Example 💫

```python
from pdf_processor import PDFProcessor
from audio_generator import AudioGenerator

# Initialize the magic! ✨
processor = PDFProcessor()
audio_gen = AudioGenerator()

# Process your PDF
pdf_path = "input/SoundDoctrineCh10.pdf"
html_content, extracted_text = processor.process_pdf(pdf_path)

# Generate HTML file
html_filename = processor.save_html(html_content, "SoundDoctrineCh10")
print(f"📄 HTML saved as: {html_filename}")

# Create audio file with different voices for italics!
audio_filename = audio_gen.create_audio(
    extracted_text, 
    output_name="SoundDoctrineCh10",
    use_different_voices=True
)
print(f"🎵 Audio saved as: {audio_filename}")
```

### Advanced Usage with Custom Voices 🎭

```python
# Custom voice settings
voice_config = {
    'normal_voice': 'Joanna',      # AWS Polly voice
    'italic_voice': 'Matthew',     # Different voice for italics
    'bracket_voice': 'Amy',        # Voice for [bracketed] content
    'speech_rate': 'slow',         # Slower pace for better comprehension
    'pitch': 'medium'
}

audio_gen.create_audio(
    extracted_text,
    output_name="MyChapter",
    voice_config=voice_config
)
```

## 🎨 Features Overview

| Feature | Description | Status |
|---------|-------------|--------|
| 📖 OCR Processing | Extract text from scanned PDFs | ✅ Ready |
| 🎭 Italic Detection | Preserve and handle italic formatting | ✅ Ready |
| 📝 HTML Generation | Create formatted HTML output | ✅ Ready |
| 🎵 Multi-voice TTS | Different voices for different text types | ✅ Ready |
| 🔊 SSML Support | Advanced speech markup | ✅ Ready |
| ⚡ Batch Processing | Process multiple files | 🚧 Coming Soon |

## 🎪 Fun Facts & Tips

- 🤖 The OCR engine can detect italic text with ~85% accuracy
- 🎭 Using different voices makes the audio more engaging
- 📱 Output works great for audiobook creation
- 🎵 SSML tags allow for dramatic pauses and emphasis
- 🚀 Processing typically takes 2-3 minutes per page

## 🤝 Contributing

Found a bug? 🐛 Want to add a feature? 🌟 
Feel free to open an issue or submit a pull request!

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

<div align="center">
  <h3>🎉 Happy PDF Processing! 🎉</h3>
  <p>Made with ❤️ and lots of ☕</p>
</div>