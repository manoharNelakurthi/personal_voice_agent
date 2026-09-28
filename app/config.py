from __future__ import annotations

from dataclasses import dataclass, field
from dotenv import load_dotenv
import os


load_dotenv()


@dataclass
class Settings:
    openai_api_key: str = field(default_factory=lambda: os.getenv("OPENAI_API_KEY", ""))
    model_name: str = field(default_factory=lambda: os.getenv("MODEL_NAME", "gpt-4o-mini"))
    system_prompt: str = field(
        default_factory=lambda: os.getenv(
            "SYSTEM_PROMPT",
            "You are a helpful personal voice assistant.",
        )
    )
    text_mode: bool = field(
        default_factory=lambda: os.getenv("TEXT_MODE", "false").lower() in {"1", "true", "yes", "on"}
    )
    voice_enabled: bool = field(
        default_factory=lambda: os.getenv("VOICE_ENABLED", "true").lower() in {"1", "true", "yes", "on"}
    )


settings = Settings()
