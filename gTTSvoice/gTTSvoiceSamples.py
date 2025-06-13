"""
Text-to-Speech Voice Sample Generator using gTTS

Description:
-------------
This script uses the `gTTS` (Google Text-to-Speech) library to convert a sample text into speech.
It attempts to simulate different voices (like "Michael", "James", "Mateo") by using different
language or regional codes. However, **gTTS only provides one voice per language/accent**, typically
a female voice, so all audio outputs will sound very similar.

Dependencies:
-------------
- Python 3.x
- gTTS (Install with: `pip install gTTS`)
- Internet connection (gTTS sends requests to Google's TTS service)

Limitations:
-------------
- Only one voice per language/accent (usually female)
- Cannot choose gender, pitch, or unique named voices
- Limited to Google's preset voices

To get more advanced voice options (like male voices or expressive speech), consider:
- ElevenLabs: https://www.elevenlabs.io/
- Google Cloud Text-to-Speech API: https://cloud.google.com/text-to-speech/docs
- Amazon Polly: https://docs.aws.amazon.com/polly/

Use Cases:
-------------
- Generating basic speech output for text
- Simple voice feedback systems
- Language learning tools
- Rapid prototyping of spoken text features

"""

from gtts import gTTS  # Google Text-to-Speech library
import os              # For handling file paths

# Sample text that will be converted into speech
sample_text = (
    "Sound doctrine is not just about knowledge — "
    "it's about living in truth and unity. As we stand together in the gospel, "
    "our love for one another reflects our love for Christ."
)

# Dictionary of "simulated" voice names mapped to language/accent codes.
# Note: gTTS only actually changes pronunciation slightly based on locale; it doesn't change voice identity.
voices = {
    "Michael (American)": "en",       # US English (default)
    "James (British)": "en-uk",       # British English accent (voice won't change significantly)
    "Mateo (Spanish-accented English)": "en-us"  # Attempted accent simulation; not reliable
}

# List to keep track of generated file paths (optional, for logging or later use)
file_paths = []

# Loop through each simulated voice and create a corresponding MP3 file
for name, lang in voices.items():
    # Create the TTS object with selected language/accent
    tts = gTTS(text=sample_text, lang=lang, slow=False)

    # Clean up the filename and set the path in the current directory
    file_name = f"./{name.replace(' ', '_').replace('(', '').replace(')', '')}.mp3"

    # Save the generated audio to an MP3 file
    tts.save(file_name)

    # Log the file name for reference
    file_paths.append((name, file_name))

# Optional: print out the saved file paths (or log them elsewhere)
for voice_name, path in file_paths:
    print(f"Saved: {voice_name} → {path}")

