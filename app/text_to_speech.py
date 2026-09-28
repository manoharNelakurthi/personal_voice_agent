from __future__ import annotations

import os
import tempfile

from gtts import gTTS
import pyttsx3


class TextToSpeech:
    def __init__(self, engine_name: str = "gtts"):
        self.engine_name = engine_name
        self._engine = None

        if self.engine_name == "pyttsx3":
            self._engine = pyttsx3.init()

    def speak(self, text: str) -> None:
        if not text:
            return

        if self.engine_name == "pyttsx3":
            self._engine.say(text)
            self._engine.runAndWait()
            return

        tts = gTTS(text=text, lang="en")
        temp_file = tempfile.NamedTemporaryFile(suffix=".mp3", delete=False)
        temp_file.close()
        tts.save(temp_file.name)
        os.system(f"afplay {temp_file.name}" if os.name == "posix" and os.uname().sysname == "Darwin" else f"start {temp_file.name}" if os.name == "nt" else f"mpg123 {temp_file.name}")

        os.remove(temp_file.name)
