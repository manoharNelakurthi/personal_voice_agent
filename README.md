# Personal Voice Agent

A starter project for a personal voice assistant that listens to voice input, sends it to an LLM, and speaks the response back.

## Features
- Microphone input via Python
- Speech-to-text support
- LLM-powered responses
- Text-to-speech output
- Local project structure ready for extension

## Tech stack
- Python
- OpenAI-compatible LLM API
- SpeechRecognition
- gTTS / pyttsx3
- FastAPI (optional API layer)

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
└── tests/
```

## Quick start

1. Clone the repository
2. Create a virtual environment
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Copy the environment file:

```bash
cp .env.example .env
```

5. Update `.env` with your keys.
6. Run the app:

```bash
python -m app.main
```

## Environment variables

Example values:

```env
OPENAI_API_KEY=your_key_here
MODEL_NAME=gpt-4o-mini
```

## Notes
- Some audio libraries require system-level dependencies such as `portaudio`.
- For local Linux systems, install `portaudio19-dev` if `pyaudio` fails.
- You can replace the default LLM client with Azure OpenAI, Ollama, or another provider.

## Suggested next steps
- Add wake word support
- Save conversation history in SQLite
- Add command triggers for reminders and notes
- Create a web dashboard or voice UI
- Add testing for the voice pipeline
