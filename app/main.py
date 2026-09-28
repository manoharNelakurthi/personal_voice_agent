from __future__ import annotations

import argparse

from app.config import settings
from app.voice_agent import VoiceAgent


def print_banner():
    print("\n" + "="*50)
    print("Personal Voice Assistant")
    print("Type /help for commands")
    print("="*50 + "\n")


def run_text_mode():
    agent = VoiceAgent()
    print_banner()
    print("Text mode enabled. Type '/exit' to quit.\n")
    while True:
        try:
            user_input = input("You: ").strip()
            if not user_input:
                continue
            if user_input.lower() in {"exit", "quit", "bye", "/exit"}:
                print("\nGoodbye!")
                break
            response = agent.respond_text(user_input)
            print(f"Assistant: {response}\n")
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as exc:  # pragma: no cover
            print(f"Error: {exc}\n")


def run_voice_mode():
    agent = VoiceAgent()
    print_banner()
    print("Voice mode enabled. Press Ctrl+C to stop.\n")
    while True:
        try:
            response = agent.listen_and_respond()
            print(f"Assistant: {response}\n")
        except KeyboardInterrupt:
            print("\n\nStopping voice assistant. Goodbye!")
            break
        except Exception as exc:  # pragma: no cover
            print(f"Error: {exc}\n")


def main():
    parser = argparse.ArgumentParser(description="Run the personal voice agent")
    parser.add_argument("--text", action="store_true", help="Run in text input mode")
    parser.add_argument("--voice", action="store_true", help="Run in microphone voice mode")
    args = parser.parse_args()

    if args.text or settings.text_mode:
        run_text_mode()
        return

    if settings.voice_enabled and not args.text:
        try:
            run_voice_mode()
        except Exception as exc:  # pragma: no cover
            print(f"Voice mode unavailable: {exc}")
            print("Falling back to text mode.\n")
            run_text_mode()
        return

    run_text_mode()


if __name__ == "__main__":
    main()
