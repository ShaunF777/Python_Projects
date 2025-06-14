from pdf_processor import PDFProcessor
from audio_generator import AudioGenerator

processor = PDFProcessor()
audio_gen = AudioGenerator()

# Process PDF
html_content, text_data = processor.process_pdf("input/SoundDoctrineCh10.pdf")

# Save HTML
html_file = processor.save_html(html_content, "SoundDoctrineCh10")

# Generate audio
audio_file = audio_gen.create_audio(text_data, "SoundDoctrineCh10")