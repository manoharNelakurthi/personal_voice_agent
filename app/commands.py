from __future__ import annotations

from app.config import settings
from app.memory import ConversationMemory


class CommandHandler:
    def __init__(self, memory: ConversationMemory | None = None):
        self.memory = memory or ConversationMemory()
        self.commands = {
            "help": self.handle_help,
            "history": self.handle_history,
            "clear": self.handle_clear,
            "status": self.handle_status,
            "mode": self.handle_mode,
        }

    def is_command(self, text: str) -> bool:
        return text.strip().lower().startswith("/")

    def handle_command(self, text: str) -> str | None:
        command_text = text.strip().lower()
        for cmd, handler in self.commands.items():
            if command_text.startswith(f"/{cmd}"):
                return handler(command_text)
        return f"Unknown command. Type '/help' for available commands."

    def handle_help(self, command: str) -> str:
        return (
            "Available commands:\n"
            "/help - Show this help message\n"
            "/history - Show recent conversations\n"
            "/clear - Clear all conversation history\n"
            "/status - Show app status\n"
            "/exit - Exit the application\n"
        )

    def handle_history(self, command: str) -> str:
        return self.memory.get_history_summary()

    def handle_clear(self, command: str) -> str:
        self.memory.clear_history()
        return "Conversation history cleared."

    def handle_status(self, command: str) -> str:
        model = settings.model_name
        voice = "enabled" if settings.voice_enabled else "disabled"
        api_status = "configured" if settings.openai_api_key else "not configured"
        return f"Status: Model={model}, Voice={voice}, API={api_status}"

    def handle_mode(self, command: str) -> str:
        return "Current mode: Text input. Use /exit to quit."
