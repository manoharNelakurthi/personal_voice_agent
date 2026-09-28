import os
from typing import Optional

import speech_recognition as sr


class SpeechToText:
    def __init__(self, recognizer: Optional[sr.Recognizer] = None):
        self.recognizer = recognizer or sr.Recognizer()

    def listen_once(self) -> str:
        with sr.Microphone() as source:
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source, timeout=10, phrase_time_limit=15)

        try:
            text = self.recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Could not understand the audio.")
            return ""
        except sr.RequestError as exc:
            print(f"Speech recognition error: {exc}")
            return ""

    def transcribe_file(self, file_path: str) -> str:
        with sr.AudioFile(file_path) as source:
            audio = self.recognizer.record(source)

        try:
            return self.recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            return ""
        except sr.RequestError as exc:
            print(f"Speech recognition error: {exc}")
            return ""
