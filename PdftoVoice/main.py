"""
This is the main script that orchestrates the entire PDF-to-voice workflow by importing and using both other modules:

pdf_processor.py (handles PDF → HTML → structured text)
audio_generator.py (handles text → audio with various options)

Quick Setup:

Make sure your folder structure looks like:
your_project/
├── main.py
├── pdf_processor.py
├── audio_generator.py
├── input/
│   └── SoundDoctrineCh10.pdf
└── output/ (will be created automatically)

The master program will:

1. Process your PDF into structured text
2. Generate an HTML preview file for you to review
3. Create multiple audio versions (standard, multi-voice, optimized)
4. Show progress and estimated duration
5. Generate chapter markers

You can comment out any audio generation options you don't need to save time during testing. 
Start with just the basic create_audio() call first to make sure everything works!

"""
from pdf_processor import PDFProcessor
from audio_generator import AudioGenerator
# Initialize
processor = PDFProcessor()
audio_gen = AudioGenerator(tts_service='local')  # or 'polly', 'google', 'elevenlabs'
# Process your PDF
html_content, text_data = processor.process_pdf("input/SoundDoctrineCh10.pdf")
# Save HTML (review this first!)
html_file = processor.save_html(html_content, "SoundDoctrineCh10")
print(f"📄 Review HTML file: {html_file}")
# Check estimated audio duration
duration = audio_gen.estimate_audio_duration(text_data)
print(f"⏱️ Estimated audio duration: {duration/60:.1f} minutes")
# Create audio with different options:
# Option 1: Standard single-voice audio
audio_file = audio_gen.create_audio(text_data, "SoundDoctrineCh10")
# Option 2: Multi-voice audio (different voices for italic/bracketed text)
multi_voice_file = audio_gen.create_multi_voice_audio(text_data, "SoundDoctrineCh10_MultiVoice")
# Option 3: Audio with progress tracking
def progress_callback(percent, message):
    print(f"Progress: {percent}% - {message}")
progress_audio = audio_gen.create_audio_with_progress(
    text_data, "SoundDoctrineCh10_Progress", progress_callback
)
# Optimize audio quality
optimized_file = audio_gen.optimize_audio_quality(audio_file)
# Create chapter markers for audio players
markers_file = audio_gen.create_chapter_markers(text_data, "SoundDoctrineCh10")
# Custom voice settings
custom_voices = {
    'normal_voice': 'Joanna',     # AWS Polly voice names
    'italic_voice': 'Matthew',    # Different voice for italics
    'bracket_voice': 'Amy',       # Voice for [bracketed] content
    'engine': 'neural'            # Use neural engine for better quality
}
audio_file = audio_gen.create_audio(
    text_data, 
    "CustomVoices", 
    voice_config=custom_voices
)