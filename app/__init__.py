from __future__ import annotations

from app.command_registry import CommandRegistry
from app.config import settings
from app.llm_client import LLMClient
from app.memory import ConversationMemory
from app.stt import SpeechToText
from app.text_to_speech import TextToSpeech


class VoiceAgent:
    def __init__(
        self,
        llm_client=None,
        stt_engine=None,
        tts_engine=None,
        memory=None,
        command_registry=None,
    ):
        self.llm_client = llm_client or LLMClient()
        self.stt_engine = stt_engine or SpeechToText()
        self.tts_engine = tts_engine or TextToSpeech()
        self.memory = memory or ConversationMemory()
        self.command_registry = command_registry or CommandRegistry()

    def _handle_system_command(self, text: str) -> str | None:
        if not settings.system_commands_enabled:
            return None
        return self.command_registry.handle(text)

    def listen_and_respond(self):
        text = self.stt_engine.listen_once()
        if not text:
            return "No speech detected."

        system_response = self._handle_system_command(text)
        if system_response:
            return system_response

        response = self.llm_client.generate(text)
        self.memory.save_conversation(text, response)
        try:
            self.tts_engine.speak(response)
        except Exception as exc:  # pragma: no cover
            print(f"Playback failed: {exc}")
        return response

    def respond_text(self, user_input: str):
        if not user_input:
            return "No input provided."

        system_response = self._handle_system_command(user_input)
        if system_response:
            return system_response

        response = self.llm_client.generate(user_input)
        self.memory.save_conversation(user_input, response)
        try:
            self.tts_engine.speak(response)
        except Exception as exc:  # pragma: no cover
            print(f"Playback failed: {exc}")
        return response
