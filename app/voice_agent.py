from .llm_client import LLMClient
from .stt import SpeechToText
from .text_to_speech import TextToSpeech


class VoiceAgent:
    def __init__(self, llm_client=None, stt_engine=None, tts_engine=None):
        self.llm_client = llm_client or LLMClient()
        self.stt_engine = stt_engine or SpeechToText()
        self.tts_engine = tts_engine or TextToSpeech()

    def listen_and_respond(self):
        text = self.stt_engine.listen_once()
        if not text:
            return "No speech detected."

        response = self.llm_client.generate(text)
        try:
            self.tts_engine.speak(response)
        except Exception as exc:  # pragma: no cover
            print(f"Playback failed: {exc}")
        return response

    def respond_text(self, user_input: str):
        response = self.llm_client.generate(user_input)
        try:
            self.tts_engine.speak(response)
        except Exception as exc:  # pragma: no cover
            print(f"Playback failed: {exc}")
        return response
