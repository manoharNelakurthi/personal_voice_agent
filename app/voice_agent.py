from __future__ import annotations

from app.config import settings
from app.llm_client import LLMClient
from app.memory import ConversationMemory
from app.stt import SpeechToText
from app.text_to_speech import TextToSpeech
from app.commands import CommandHandler


class VoiceAgent:
    def __init__(
        self,
        llm_client: LLMClient | None = None,
        stt_engine: SpeechToText | None = None,
        tts_engine: TextToSpeech | None = None,
        memory: ConversationMemory | None = None,
        command_handler: CommandHandler | None = None,
    ):
        self.llm_client = llm_client or LLMClient()
        self.stt_engine = stt_engine or SpeechToText()
        self.tts_engine = tts_engine or TextToSpeech()
        self.memory = memory or ConversationMemory()
        self.command_handler = command_handler or CommandHandler(self.memory)
        self.conversation_count = 0

    def listen_and_respond(self) -> str:
        text = self.stt_engine.listen_once()
        if not text:
            return "No speech detected."

        if self.command_handler.is_command(text):
            response = self.command_handler.handle_command(text)
            return response or "Command not recognized."

        response = self.llm_client.generate(text)
        self.memory.save_conversation(text, response)
        self.conversation_count += 1

        try:
            self.tts_engine.speak(response)
        except Exception as exc:  # pragma: no cover
            print(f"Playback failed: {exc}")
        return response

    def respond_text(self, user_input: str) -> str:
        if self.command_handler.is_command(user_input):
            response = self.command_handler.handle_command(user_input)
            return response or "Command not recognized."

        response = self.llm_client.generate(user_input)
        self.memory.save_conversation(user_input, response)
        self.conversation_count += 1

        try:
            self.tts_engine.speak(response)
        except Exception as exc:  # pragma: no cover
            print(f"Playback failed: {exc}")
        return response

    def get_stats(self) -> str:
        return f"Conversations this session: {self.conversation_count}"
