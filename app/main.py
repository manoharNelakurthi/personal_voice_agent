from __future__ import annotations

from app.voice_agent import VoiceAgent


def main():
    agent = VoiceAgent()
    while True:
        response = agent.listen_and_respond()
        print(f"Assistant: {response}")


if __name__ == "__main__":
    main()
