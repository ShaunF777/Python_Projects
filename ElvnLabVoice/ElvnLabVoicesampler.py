"""
ElevenLabs Text-to-Speech: Basic Voice Generator

Description:
-------------
This script uses the ElevenLabs Text-to-Speech API to convert a short sentence into a realistic
spoken audio file using a selected voice. ElevenLabs provides high-quality, natural-sounding
voices (male and female) and allows voice customization.

Dependencies:
-------------
- Python 3.x
- `requests` module (Install with: `pip install requests`)
- Internet connection
- A valid ElevenLabs API key

Limitations:
-------------
- API key required (free and paid tiers available at https://www.elevenlabs.io/)
- Rate limits apply depending on your subscription
- Voice list must be fetched or manually selected from available voice IDs

How to Change the Voice:
-------------
1. Visit: https://api.elevenlabs.io/docs to explore available voices
2. Log in to your ElevenLabs account and get your API key
3. Use the `/v1/voices` endpoint to list all voice IDs and names
4. Replace the `voice_id` in the script below with your desired one

More Resources:
-------------
- Official Docs: https://docs.elevenlabs.io/
- Voice List API: https://docs.elevenlabs.io/api-reference/voices/get-voices
- Signup: https://www.elevenlabs.io/

Use Cases:
-------------
- Realistic audiobook narration
- Accessibility tools
- Voiceovers for media
- Chatbot or app voices

"""

import requests
import os
from dotenv import load_dotenv

load_dotenv()  # 🔺 Add this before reading from os.getenv

# Your ElevenLabs API key (keep this secure!)
API_KEY = os.getenv("ELEVENLABS_API_KEY")  # Make sure to set this in your environment variables
# Get your own API key from https://www.elevenlabs.io/

print(f"API Key loaded: {API_KEY}")  # 👈 For debugging only

# The sentence to convert to speech
text_to_speak = "Sound doctrine unites us in truth and love."

# Choose a voice ID — you can get this from the ElevenLabs dashboard or voice list API
voice_id = "iP95p4xoKVk53GoZ742B"  # Example: "Chris" voice ID; replace with your desired voice ID

# Set up API endpoint and headers
url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
headers = {
    "xi-api-key": API_KEY,
    "Content-Type": "application/json"
}

# Configure voice settings and payload
payload = {
    "text": text_to_speak,
    "model_id": "eleven_monolingual_v1",  # Default model; see docs for multilingual or others
    "voice_settings": {
        "stability": 0.7,   # Lower = more variation, Higher = more consistent
        "similarity_boost": 0.75  # Voice likeness accuracy
    }
}

# Send the request to ElevenLabs API
response = requests.post(url, headers=headers, json=payload)

# Check for errors
if response.status_code != 200:
    print(f"Error: {response.status_code} - {response.text}")
    exit()

# Save the audio content to an MP3 file
output_filename = "output_elevenlabs.mp3"
with open(output_filename, "wb") as f:
    f.write(response.content)

print(f"✅ Audio saved as: {output_filename}")
