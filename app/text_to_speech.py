from __future__ import annotations

import os
import shutil
import subprocess
import tempfile

from gtts import gTTS
import pyttsx3


class TextToSpeech:
    def __init__(self, engine_name: str = "gtts"):
        self.engine_name = engine_name
        self._engine = None

        if engine_name == "pyttsx3":
            try:
                self._engine = pyttsx3.init()
            except Exception as exc:  # pragma: no cover
                print(f"pyttsx3 unavailable: {exc}")
                self._engine = None

    def speak(self, text: str) -> None:
        if not text:
            return

        if self.engine_name == "pyttsx3" and self._engine is not None:
            self._engine.say(text)
            self._engine.runAndWait()
            return

        try:
            tts = gTTS(text=text, lang="en")
            with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as temp_file:
                temp_path = temp_file.name
            tts.save(temp_path)

            if os.name == "nt":
                os.startfile(temp_path)
            elif os.uname().sysname == "Darwin":
                subprocess.run(["afplay", temp_path], check=False)
            else:
                if shutil.which("mpg123"):
                    subprocess.run(["mpg123", temp_path], check=False)
                elif shutil.which("play"):
                    subprocess.run(["play", temp_path], check=False)
                else:
                    print(f"TTS audio generated: {temp_path}")

            os.remove(temp_path)
        except Exception as exc:  # pragma: no cover
            print(f"Text-to-speech failed: {exc}")
