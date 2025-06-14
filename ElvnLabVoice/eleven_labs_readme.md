# 🧠 ElevenLabs API - Text to Speech 🔊

Welcome to your ElevenLabs integration project! This guide walks you through setting up the **ElevenLabs API key**, what it does, how to configure access levels properly, and how to keep your project clean and secure.

---

## 📌 What is ElevenLabs?

[ElevenLabs](https://www.elevenlabs.io/) is an AI voice platform that provides:

- 🎧 **Text-to-Speech (TTS)**: Convert text into natural-sounding human speech.
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

📚 Official Docs: [https://docs.elevenlabs.io/](https://docs.elevenlabs.io/)

---

## 🚀 Getting Started (Step-by-Step)

### ✅ 1. Clone the Repo

```bash
git clone https://github.com/yourname/yourproject.git
cd yourproject
```

### ✅ 2. Create Environment Files

#### 📟 `.env` (local secrets)

Create a file named `.env` in your project root:

```bash
# .env
ELEVENLABS_API_KEY=your_actual_api_key_here
```

✅ This file contains your **real API key**. ❌ **Never commit this file!**

#### 🧪 `.env.example` (template for others)

Create a file named `.env.example` to share with others:

```bash
# .env.example
ELEVENLABS_API_KEY=your_api_key_here
```

✅ Commit this file so collaborators know what environment variables to define.

---

### ✅ 3. Create an API Key

Go to [API Keys page](https://www.elevenlabs.io/app/api-keys) and click **"Create New Key"**.

#### 🔐 Name

> 📟 **Q: It auto-generates a name like *****"Menacing Anaconda"***** — can I change it?**\
> ✅ **Yes**, you can rename it.\
> ⚠️ **No**, you should not commit the API key **or the name** to a public GitHub repo.

#### 💳 Credit Limit

> 📌 **Default: Unlimited**\
> ⚠️ This reflects usage within your plan’s quota. The free tier includes limited monthly credits.

---

## 🎛️ Permissions Explained

Choose what features your API key can access. You can keep most at **"no access"** if you're just doing basic TTS.

| Feature                           | What it Does                   | Access Option                              | Suggestion                   |
| --------------------------------- | ------------------------------ | ------------------------------------------ | ---------------------------- |
| 🔊 **Text to Speech**             | Converts written text to audio | `Has access` / `No access`                 | ✅ Enable for TTS usage       |
| 🗣️ **Speech to Speech**          | Changes one voice to another   | `Has access` / `No access`                 | ❌ Skip unless needed         |
| 📟 **Speech to Text**             | Transcribes audio to text      | `Has access` / `No access`                 | ❌ Skip if not transcribing   |
| 💥 **Sound Effects**              | Adds effects to audio          | `Has access` / `No access`                 | ❌ Optional                   |
| 🎚️ **Audio Isolation**           | Removes background noise       | `Has access` / `No access`                 | ❌ Optional                   |
| 🌐 **Dubbing**                    | Translate/lipsync audio        | `No access` / `Read only` / `Read & write` | ❌ Enable later if needed     |
| 📁 **Projects**                   | Manage project folders         | `No access` / `Read only` / `Read & write` | ❌ Skip unless needed         |
| 🧚 **Audio Native**               | Upload native audio            | `No access` / `Read only` / `Read & write` | ❌ Optional                   |
| 📖 **Pronunciation Dictionaries** | Custom pronunciations          | `No access` / `Read only` / `Read & write` | ❌ Optional                   |
| 🦱 **Voices**                     | Manage voices                  | `No access` / `Read only` / `Read & write` | ✅ Enable if needed           |
| 🧠 **Voice Generation**           | Clone voices                   | `Has access` / `No access`                 | ✅ Optional for custom voices |
| 🧹 **Models**                     | Speech synthesis models        | `No access` / `Read only` / `Read & write` | ❌ Skip unless advanced user  |
| 🕒 **History**                    | View past generations          | `No access` / `Read only` / `Read & write` | ✅ `Read only` is fine        |
| 👤 **User**                       | Access account info            | `No access` / `Read only` / `Read & write` | ❌ Unnecessary for TTS        |
| 🏢 **Workspace**                  | Team workspace info            | `No access` / `Read only` / `Read & write` | ❌ Skip unless using teams    |
| 📌 **Forced Alignment**           | Time-sync text/audio           | `Has access` / `No access`                 | ✅ Optional for subtitles     |

---

## 🧪 Sample Use Case

```python
# Basic use in Python
import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("ELEVENLABS_API_KEY")
voice_id = "TxGEqnHWrfWFTfGW9XjX"  # Rachel

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

---

## 🔐 Hiding API Keys (Best Practices)

### 📟 What is a `.env` file?

A `.env` file stores environment variables like API keys. These are read at runtime.

📌 Example `.env`:

```bash
ELEVENLABS_API_KEY=your_real_key_here
```

### 📟 What is a `.env.example` file?

A public-safe template showing required keys for collaborators. This should be committed.

📈 Example `.env.example`:

```bash
ELEVENLABS_API_KEY=your_api_key_here
```

### 📟 What is `.gitignore`?

Tells Git what files/folders **not** to track.

📈 Example `.gitignore`:

```bash
# .gitignore
.env
__pycache__/
*.py[cod]
*.pyo
.venv/
venv/
env/
.DS_Store
Thumbs.db
.vscode/
.idea/
*.log
*.bak
```

✅ Suggested Folder Layout:

```bash
your-project/
├── .env               ← your private secrets
├── .env.example       ← template to share safely
├── .gitignore         ← excludes secrets & clutter
├── ElvnLabVoice/
│   ├── eleven_api_script.py
│   ├── output/
│   └── README.md
├── requirements.txt
└── README.md
```

---

