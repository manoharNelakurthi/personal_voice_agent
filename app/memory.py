from __future__ import annotations

import sqlite3
from datetime import datetime
from pathlib import Path
from typing import Optional


class ConversationMemory:
    def __init__(self, db_path: str = "data/conversations.db"):
        self.db_path = db_path
        Path(self.db_path).parent.mkdir(parents=True, exist_ok=True)
        self._init_db()

    def _init_db(self) -> None:
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS conversations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_message TEXT NOT NULL,
                    assistant_response TEXT NOT NULL,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)
            conn.commit()

    def save_conversation(self, user_message: str, assistant_response: str) -> None:
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                "INSERT INTO conversations (user_message, assistant_response, timestamp) VALUES (?, ?, ?)",
                (user_message, assistant_response, datetime.now().isoformat()),
            )
            conn.commit()

    def get_recent_conversations(self, limit: int = 5) -> list[dict]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute(
                "SELECT user_message, assistant_response, timestamp FROM conversations ORDER BY id DESC LIMIT ?",
                (limit,),
            )
            rows = cursor.fetchall()
        return [
            {"user": row[0], "assistant": row[1], "timestamp": row[2]}
            for row in reversed(rows)
        ]

    def get_all_conversations(self) -> list[dict]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute(
                "SELECT user_message, assistant_response, timestamp FROM conversations ORDER BY id ASC"
            )
            rows = cursor.fetchall()
        return [
            {"user": row[0], "assistant": row[1], "timestamp": row[2]}
            for row in rows
        ]

    def clear_history(self) -> None:
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("DELETE FROM conversations")
            conn.commit()

    def get_history_summary(self) -> str:
        conversations = self.get_recent_conversations(limit=5)
        if not conversations:
            return "No previous conversations."
        summary = "Recent conversations:\n"
        for i, conv in enumerate(conversations, 1):
            summary += f"{i}. You: {conv['user'][:50]}...\n   Assistant: {conv['assistant'][:50]}...\n"
        return summary
