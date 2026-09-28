from __future__ import annotations

from app.config import settings


class LLMClient:
    def __init__(self, api_key: str | None = None, model_name: str | None = None):
        self.api_key = api_key or settings.openai_api_key
        self.model_name = model_name or settings.model_name
        self.client = None

        if self.api_key:
            try:
                from openai import OpenAI
                self.client = OpenAI(api_key=self.api_key)
            except Exception as exc:  # pragma: no cover
                print(f"OpenAI SDK could not be initialized: {exc}")

    def _fallback_response(self, user_message: str) -> str:
        message = user_message.strip()
        if not message:
            return "I did not hear anything. Please say something again."

        return (
            f"You said: '{message}'. "
            "This is a demo response because no valid OpenAI key is configured. "
            "Add OPENAI_API_KEY in your .env file to enable live LLM responses."
        )

    def generate(self, user_message: str) -> str:
        if self.client is None:
            return self._fallback_response(user_message)

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
