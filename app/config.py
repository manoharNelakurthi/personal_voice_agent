from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from dotenv import load_dotenv
import os


load_dotenv()


@dataclass
class Settings:
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")
    model_name: str = os.getenv("MODEL_NAME", "gpt-4o-mini")
    system_prompt: str = os.getenv(
        "SYSTEM_PROMPT",
        "You are a helpful personal voice assistant.",
    )


settings = Settings()
