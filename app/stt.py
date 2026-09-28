from __future__ import annotations

import os
from typing import Optional

import speech_recognition as sr


class SpeechToText:
    def __init__(self, recognizer: Optional[sr.Recognizer] = None):
        self.recognizer = recognizer or sr.Recognizer()

    def listen_once(self) -> str:
        try:
            with sr.Microphone() as source:
                print("Listening...")
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = self.recognizer.listen(source, timeout=10, phrase_time_limit=15)
        except (OSError, AttributeError, TypeError) as exc:
            print(f"Microphone unavailable: {exc}")
            return ""
        except Exception as exc:  # pragma: no cover
            print(f"Unexpected microphone error: {exc}")
            return ""

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
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Audio file not found: {file_path}")

        with sr.AudioFile(file_path) as source:
            audio = self.recognizer.record(source)

        try:
            return self.recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            return ""
        except sr.RequestError as exc:
            print(f"Speech recognition error: {exc}")
            return ""
