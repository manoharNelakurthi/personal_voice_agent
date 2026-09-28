# Personal Voice Agent

A personal voice assistant that can answer questions and also open apps by voice commands like "open chrome" or "launch vs code".

## Features

- Voice and text interaction
- Open desktop apps through voice commands
- Open common apps like Chrome, VS Code, Finder/Explorer, Spotify, Terminal, Calculator, and more
- LLM support via OpenAI-compatible APIs
- Conversation memory stored in SQLite
- Streamlit dashboard for history and stats
- Demo mode when API keys are not configured

## Supported app examples

- chrome
- firefox
- edge
- vscode / code
- notepad
- terminal / cmd / powershell
- calculator
- spotify
- explorer / file explorer
- browser

## Quick start

1. Clone the repo
2. Create a virtual environment
3. Install dependencies
4. Copy `.env.example` to `.env`
5. Add your OpenAI key if you want live LLM responses

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
```

Edit `.env`:

```env
OPENAI_API_KEY=your_key_here
MODEL_NAME=gpt-4o-mini
SYSTEM_PROMPT=You are a helpful personal voice assistant.
TEXT_MODE=false
VOICE_ENABLED=true
SYSTEM_COMMANDS_ENABLED=true
```

## Run text mode

```bash
python -m app.main --text
```

Example:

```text
You: hello
Assistant: Hello! How can I help you today?

You: open chrome
Assistant: Opened chrome.
```

## Run voice mode

```bash
python -m app.main --voice
```

Then say things like:
- "hi"
- "open chrome"
- "launch vscode"
- "open calculator"
- "what is the weather"

## Run web dashboard

```bash
streamlit run web/app.py
```

## Notes

- If no OpenAI key is configured, the app still works in demo mode.
- Voice command execution depends on the app being installed on your system.
- On Linux/macOS, some apps may require installation or an exact executable name.

## Supported actions

This version supports app launch commands such as:

- open chrome
- start firefox
- launch vscode
- open terminal
- open calculator
- open spotify

## Future enhancements

- close apps by voice
- open files by voice
- custom app shortcuts
- wake word support
- more advanced automation
