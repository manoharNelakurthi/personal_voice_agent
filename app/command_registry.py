from __future__ import annotations

import re
from typing import Optional

from app.system_actions import SystemActions


class CommandRegistry:
    def __init__(self, system_actions: Optional[SystemActions] = None):
        self.system_actions = system_actions or SystemActions()

    def handle(self, text: str) -> Optional[str]:
        if not text:
            return None

        lower = text.lower().strip()
        if not lower:
            return None

        if re.search(r"\b(open|launch|start|run)\b", lower):
            match = re.search(r"\b(open|launch|start|run)\s+(?:the\s+)?(.+)", lower)
            if match:
                app_name = match.group(2).strip()
                if app_name and app_name not in {"app", "application"}:
                    return self.system_actions.open_app(app_name)

        if re.search(r"\b(close|quit)\b", lower):
            match = re.search(r"\b(close|quit)\s+(?:the\s+)?(.+)", lower)
            if match:
                app_name = match.group(2).strip()
                return f"I can open apps, but closing apps will be added in a future update. Requested: {app_name}."

        for alias_key, aliases in self.system_actions.APP_ALIASES.items():
            for alias in aliases:
                if alias in lower:
                    return self.system_actions.open_app(alias)

        return None
