from gtts import gTTS
import os

# Sample text to generate voice samples
sample_text = ("Sound doctrine is not just about knowledge — "
               "it's about living in truth and unity. As we stand together in the gospel, "
               "our love for one another reflects our love for Christ.")

# Voice samples (Note: gTTS only supports default Google voices; for variety, we'd need access to more advanced tools)
# We'll simulate different voices using different accents/languages supported by gTTS

# Simulated voice mappings
voices = {
    "Michael (American)": "en",
    "James (British)": "en-uk",
    "Mateo (Spanish-accented English)": "en-us"  # gTTS doesn't support Spanish-accented English directly
}

# Generate audio files
file_paths = []
for name, lang in voices.items():
    tts = gTTS(text=sample_text, lang=lang, slow=False)
    file_name = f"/mnt/data/{name.replace(' ', '_').replace('(', '').replace(')', '')}.mp3"
    tts.save(file_name)
    file_paths.append((name, file_name))

file_paths
