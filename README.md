# Personal Voice Agent

A starter project for a personal voice assistant that listens to your voice, sends the text to an LLM, and speaks the reply back.

## Features
- Text or voice interaction modes
- Speech-to-text via `SpeechRecognition`
- LLM-powered responses with OpenAI-compatible APIs
- Text-to-speech using `gTTS` with fallback support
- Demo mode when no API key is configured

## Project structure

```text
personal_voice_agent/
├── app/
│   ├── __init__.py
│   ├── audio_utils.py
│   ├── config.py
│   ├── llm_client.py
│   ├── main.py
│   ├── stt.py
│   ├── text_to_speech.py
│   └── voice_agent.py
├── .env.example
├── .gitignore
├── README.md
├── requirements.txt
├── tests/
│   └── test_import.py
└── venv/
```

## Quick start

1. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Copy the environment file:

```bash
cp .env.example .env
```

4. Add your API key (optional in demo mode):

```env
OPENAI_API_KEY=your_key_here
MODEL_NAME=gpt-4o-mini
SYSTEM_PROMPT=You are a helpful personal voice assistant.
TEXT_MODE=false
VOICE_ENABLED=true
```

5. Run the app in text mode:

```bash
python -m app.main --text
```

6. Run the app in voice mode:

```bash
python -m app.main --voice
```

## Demo mode

If `OPENAI_API_KEY` is not set, the app still runs and responds with a local demo message so you can test the conversation loop without an external API.

## Notes

- `pyaudio` may require OS-level dependencies on Linux/macOS.
- Ubuntu/Debian fix:

```bash
sudo apt-get install portaudio19-dev
```

- macOS fix:

```bash
brew install portaudio
```

## Next steps

- Add wake-word support
- Save chat history to SQLite
- Add custom personal commands
- Add a web UI or dashboard
- Add tool integrations for reminders and note-taking
