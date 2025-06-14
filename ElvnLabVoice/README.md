# 🧠 ElevenLabs API - Text to Speech 🔊  
Welcome to your ElevenLabs integration project! This guide walks you through setting up the **ElevenLabs API key**, what it does, and how to configure access levels properly.

---

## 📌 What is ElevenLabs?

[ElevenLabs](https://www.elevenlabs.io/) is an AI voice platform that provides:

- 🎙️ **Text-to-Speech (TTS)**: Convert text into natural-sounding human speech.
- 🗣️ **Speech-to-Speech (STS)**: Modify existing speech with a different voice or style.
- 📄 **Speech-to-Text (STT)**: Convert audio recordings into written text (transcription).
- 🎧 **Sound Effects & Audio Isolation**: Advanced audio editing tools.
- 🌍 **Multilingual Dubbing**: Translate and revoice content in other languages with synced timing.

You can use it for:
- Audiobook narration
- Voice assistants
- Accessibility features
- YouTube narration or dubbing
- AI characters and chatbots

Official Docs: https://docs.elevenlabs.io/

---

## 🚀 Step-by-Step Setup

### ✅ 1. Sign In
Go to https://www.elevenlabs.io/ and sign in (or create an account).

---

### ✅ 2. Create an API Key
Go to [API Keys page](https://www.elevenlabs.io/app/api-keys) and click **"Create New Key"**.

#### 🔐 Name
> 🧾 **Q: It auto-generates a name like _"Menacing Anaconda"_ — can I change it?**  
> ✅ **Yes, you can rename it**, but it's optional.  
> ⚠️ **No**, you should not commit the API key **or the name** to a public GitHub repo. Store it in a `.env` file or use GitHub Secrets. Scroll down for more details on API key safety.



#### 💳 Credit Limit
> 📌 **Default: Unlimited**  
> ⚠️ This reflects usage within your account’s allowed quota. On a free plan, you have limited monthly credits.

---

## 🎛️ Permissions Explained

Choose what features your API key will have access to. You can keep most to **"no access"** if you're just doing basic TTS.

| Feature | What it Does | Access Option | Suggestion |
|--------|---------------|----------------|-------------|
| 🔊 **Text to Speech** | Converts written text to audio | `Has access` / `No access` | ✅ Enable this if you want to use TTS |
| 🗣️ **Speech to Speech** | Changes one voice to another | `Has access` / `No access` | ❌ Disable unless you need voice conversion |
| 🧾 **Speech to Text** | Transcribes spoken audio to text | `Has access` / `No access` | ❌ Disable if not transcribing audio |
| 💥 **Sound Effects** | Add effects to generated speech | `Has access` / `No access` | ❌ Optional |
| 🎚️ **Audio Isolation** | Remove background sounds, isolate vocals | `Has access` / `No access` | ❌ Optional |
| 🌐 **Dubbing** | Auto-translates and lipsyncs video/audio | `No access`, `Read only`, `Read & write` | ❌ Optional unless building multi-language tools |
| 📁 **Projects** | Manage project folders & metadata | `No access`, `Read only`, `Read & write` | ❌ Leave as `No access` unless needed |
| 🧬 **Audio Native** | Upload native audio samples for customization | `No access`, `Read only`, `Read & write` | ❌ Optional |
| 📖 **Pronunciation Dictionaries** | Custom word/phrase pronunciation | `No access`, `Read only`, `Read & write` | ❌ Optional unless using rare terms |
| 🧑‍🎤 **Voices** | View/create/edit custom voices | `No access`, `Read only`, `Read & write` | ✅ Use `Read only` or `Read & write` if you need voice control |
| 🧠 **Voice Generation** | Clone or create new voices | `Has access` / `No access` | ✅ Enable only if making new voices |
| 🧩 **Models** | Use or manage speech synthesis models | `No access`, `Read only`, `Read & write` | ❌ Leave off unless you're managing custom models |
| 🕓 **History** | Access logs of past generations | `No access`, `Read only`, `Read & write` | ✅ `Read only` is fine for most users |
| 👤 **User** | Access account-level info (email, usage, etc) | `No access`, `Read only`, `Read & write` | ❌ Usually unnecessary |
| 🏢 **Workspace** | Manage team workspaces | `No access`, `Read only`, `Read & write` | ❌ Skip unless using team plans |
| 📌 **Forced Alignment** | Align text with speech for precise timing | `Has access` / `No access` | ✅ Enable only if doing time-synced subtitles or dubbing |

---

## 🧪 Sample Use Case

```python
# Basic use in Python
import requests

API_KEY = "your_real_key_here"
voice_id = "TxGEqnHWrfWFTfGW9XjX"  # Example: "Rachel"

response = requests.post(
    f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}",
    headers={
        "xi-api-key": API_KEY,
        "Content-Type": "application/json"
    },
    json={
        "text": "Sound doctrine unites us in truth and love.",
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.7,
            "similarity_boost": 0.75
        }
    }
)

with open("output.mp3", "wb") as f:
    f.write(response.content)
```
🔐 Hiding API Keys (Best Practice for Python Projects)

To protect your sensitive information, like API keys, you should:

    Use a .env file to store secrets locally.

    Use a .gitignore file to exclude .env from version control (e.g. GitHub).

    Avoid committing sensitive data (e.g. API keys, passwords, personal info, logs).

🧾 What is a .env file?

A .env file stores environment variables like API keys. These are read at runtime by your program.

✅ Example .env file (create it in your project root)
```bash
# .env
ELEVENLABS_API_KEY=your_actual_api_key_here
```

    🔒 Never commit this file to GitHub!

🧾 What is a .gitignore file?

A .gitignore file tells Git which files/folders not to track or commit.

✅ Example .gitignore file
```bash
# .gitignore

# Hide secret keys
.env

# Hide Python cache
__pycache__/
*.py[cod]
*.pyo

# Hide virtual environment folder (if you're using one)
.venv/
env/
venv/

# Hide OS and editor files
.DS_Store
Thumbs.db
.vscode/
.idea/

# Hide logs or debug output
*.log
*.bak
```
✅ Suggested .env + Folder Strategy

Root Project Structure:
```bash
your-project/
├── .env               ← secrets here
├── .gitignore         ← excludes .env
├── ElvnLabVoice/
│   ├── eleven_api_script.py
│   ├── output/
│   └── README.md
├── other_folder/
├── requirements.txt
└── README.md
```
✅ How to Use .env in Your Python Code

Install python-dotenv: `pip install python-dotenv`

Then update your code like this:
```py
from dotenv import load_dotenv
import os

# Load .env file into environment
load_dotenv()

# Access the API key
api_key = os.getenv("ELEVENLABS_API_KEY")
```
