# Personal Voice Agent

A personal voice assistant that listens to your voice, processes it with an LLM, and speaks the response back. Features conversation memory, command handling, and a web dashboard.

## Features

- **Voice & Text Modes**: Interact via microphone or keyboard
- **Conversation Memory**: SQLite-based storage of all conversations
- **Command System**: Built-in commands like `/history`, `/clear`, `/help`, `/status`
- **Web Dashboard**: Streamlit-based UI for chat, history, and statistics
- **Demo Mode**: Works without an API key for testing
- **Error Handling**: Graceful fallbacks for missing dependencies

## Project structure

```text
personal_voice_agent/
├── app/
│   ├── __init__.py
│   ├── audio_utils.py
│   ├── commands.py          (NEW: Command handler)
│   ├── config.py
│   ├── llm_client.py
│   ├── main.py
│   ├── memory.py            (NEW: SQLite conversation storage)
│   ├── stt.py
│   ├── text_to_speech.py
│   └── voice_agent.py
├── web/
│   └── app.py               (NEW: Streamlit dashboard)
├── data/                    (NEW: SQLite database)
│   └── conversations.db
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt
```

## Quick start

### 1. Setup

```bash
git clone https://github.com/manoharNelakurthi/personal_voice_agent.git
cd personal_voice_agent
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
```

### 2. Configure

Edit `.env`:

```env
OPENAI_API_KEY=your_key_here  # Optional in demo mode
MODEL_NAME=gpt-4o-mini
SYSTEM_PROMPT=You are a helpful personal voice assistant.
TEXT_MODE=false
VOICE_ENABLED=true
```

### 3. Run

**Text mode:**

```bash
python -m app.main --text
```

**Voice mode:**

```bash
python -m app.main --voice
```

**Web dashboard:**

```bash
streamlit run web/app.py
```

## Commands (Text Mode)

- `/help` - Show available commands
- `/history` - Display recent conversations
- `/clear` - Delete all conversation history
- `/status` - Show app configuration status
- `/exit` - Quit the application

## Example interactions

### Text mode:

```text
==================================================
Personal Voice Assistant
Type /help for commands
==================================================

Text mode enabled. Type '/exit' to quit.

You: hello
Assistant: Hello! How can I help you today?

You: /history
Assistant: Recent conversations:
1. You: hello
   Assistant: Hello! How can I help you today?

You: /exit
Goodbye!
```

### Web dashboard:

- Visit `http://localhost:8501` after running `streamlit run web/app.py`
- Chat tab: Send messages and get responses
- History tab: Browse all past conversations
- Statistics tab: View session and overall stats

## Setup troubleshooting

### Issue: `pyaudio` installation fails

**Ubuntu/Debian:**

```bash
sudo apt-get install portaudio19-dev
pip install pyaudio
```

**macOS:**

```bash
brew install portaudio
pip install pyaudio
```

### Issue: Microphone not detected

- Check system audio settings
- Verify microphone permissions
- Try text mode instead

### Issue: gTTS playback fails

**Linux:**

```bash
sudo apt-get install mpg123
```

## Architecture

- **VoiceAgent**: Main orchestrator
- **LLMClient**: OpenAI API integration
- **SpeechToText**: Microphone input processing
- **TextToSpeech**: Audio output generation
- **ConversationMemory**: SQLite persistence
- **CommandHandler**: Command parsing and execution

## Next steps

- Add wake-word detection
- Add reminders and notes features
- Add local LLM support (Ollama, LM Studio)
- Add voice profiles and personalization
- Deploy as a standalone application

## License

MIT License
