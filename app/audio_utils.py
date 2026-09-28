import wave

import sounddevice as sd
import numpy as np


def record_audio(duration: float = 5.0, sample_rate: int = 16000, channels: int = 1) -> np.ndarray:
    print(f"Recording for {duration} seconds...")
    audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=channels, dtype="float32")
    sd.wait()
    return audio


def save_wav(file_path: str, audio: np.ndarray, sample_rate: int = 16000) -> None:
    with wave.open(file_path, "wb") as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(sample_rate)
        wav_file.writeframes((audio * 32767).astype("int16").tobytes())
