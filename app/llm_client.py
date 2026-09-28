from __future__ import annotations

from app.config import settings


class LLMClient:
    def __init__(self, api_key: str | None = None, model_name: str | None = None):
        self.api_key = api_key or settings.openai_api_key
        self.model_name = model_name or settings.model_name

        if not self.api_key:
            raise ValueError("OPENAI_API_KEY is missing. Add it to .env")

        try:
            from openai import OpenAI
            self.client = OpenAI(api_key=self.api_key)
        except Exception as exc:  # pragma: no cover
            raise RuntimeError("OpenAI SDK not installed or misconfigured") from exc

    def generate(self, user_message: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[
                {"role": "system", "content": settings.system_prompt},
                {"role": "user", "content": user_message},
            ],
            temperature=0.7,
            max_tokens=500,
        )
        return response.choices[0].message.content.strip()
