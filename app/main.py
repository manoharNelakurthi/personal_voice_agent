from __future__ import annotations

import argparse

from app.config import settings
from app.voice_agent import VoiceAgent


def run_text_mode():
    agent = VoiceAgent()
    print("Text mode enabled. Type 'exit' to quit.")
    while True:
        user_input = input("You: ").strip()
        if not user_input:
            continue
        if user_input.lower() in {"exit", "quit", "bye"}:
            print("Goodbye!")
            break
        response = agent.respond_text(user_input)
        print(f"Assistant: {response}")


def run_voice_mode():
    agent = VoiceAgent()
    while True:
        try:
            response = agent.listen_and_respond()
            print(f"Assistant: {response}")
        except KeyboardInterrupt:
            print("\nStopping voice assistant.")
            break


def main():
    parser = argparse.ArgumentParser(description="Run the personal voice agent")
    parser.add_argument("--text", action="store_true", help="Run in text input mode")
    parser.add_argument("--voice", action="store_true", help="Run in microphone voice mode")
    args = parser.parse_args()

    if args.text or settings.text_mode:
        run_text_mode()
        return

    if settings.voice_enabled and not args.text:
        run_voice_mode()
        return

    run_text_mode()


if __name__ == "__main__":
    main()
