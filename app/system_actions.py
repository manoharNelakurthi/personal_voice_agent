from __future__ import annotations

import os
import shutil
import subprocess
import sys
from typing import Dict, List


class SystemActions:
    """Open common desktop apps and programs via voice commands."""

    APP_ALIASES: Dict[str, List[str]] = {
        "chrome": ["chrome", "google chrome", "google-chrome"],
        "firefox": ["firefox", "mozilla firefox"],
        "edge": ["edge", "microsoft edge"],
        "vscode": ["vscode", "visual studio code", "code"],
        "notepad": ["notepad", "notepad++"],
        "terminal": ["terminal", "command prompt", "cmd", "powershell", "pwsh"],
        "calculator": ["calculator", "calc"],
        "spotify": ["spotify"],
        "explorer": ["explorer", "file explorer"],
        "browser": ["browser", "web browser"],
    }

    def open_app(self, app_name: str) -> str:
        normalized = app_name.strip()
        if not normalized:
            return "No app name was provided."

        alias_key = self._resolve_alias(normalized)
        if alias_key:
            target = alias_key
        else:
            target = normalized

        try:
            if self._run_system_command(target):
                return f"Opened {normalized}."
            return f"I couldn't find or open '{normalized}'."
        except Exception as exc:  # pragma: no cover
            return f"I couldn't open '{normalized}' because: {exc}"

    def _resolve_alias(self, app_name: str) -> str | None:
        lower = app_name.lower().strip()
        for key, aliases in self.APP_ALIASES.items():
            if lower in aliases:
                return key
            if lower.replace("-", " ") in aliases:
                return key
        return None

    def _run_system_command(self, target: str) -> bool:
        if sys.platform.startswith("win"):
            return self._run_windows(target)
        if sys.platform == "darwin":
            return self._run_macos(target)
        return self._run_linux(target)

    def _run_windows(self, target: str) -> bool:
        executable = self._resolve_windows_executable(target)
        if executable:
            subprocess.Popen(executable, shell=True)
            return True

        try:
            subprocess.Popen(["cmd", "/c", "start", "", target], shell=True)
            return True
        except Exception:
            return False

    def _run_macos(self, target: str) -> bool:
        app_name = target
        if not self._is_builtin_app(target):
            app_name = self._maybe_find_macos_app(target)

        try:
            if app_name:
                subprocess.Popen(["open", "-a", app_name])
                return True
            subprocess.Popen(["open", target])
            return True
        except Exception:
            return False

    def _run_linux(self, target: str) -> bool:
        command = self._resolve_linux_command(target)
        if command:
            subprocess.Popen(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            return True
        return False

    def _resolve_windows_executable(self, target: str) -> list[str] | None:
        candidates = [
            target,
            self.APP_ALIASES.get(target, [target])[0],
            target.replace(" ", ""),
        ]
        for candidate in candidates:
            resolved = shutil.which(candidate)
            if resolved:
                return [resolved]
        return None

    def _maybe_find_macos_app(self, name: str) -> str | None:
        candidates = [
            name,
            name.replace(" ", ""),
            f"{name}.app",
            f"{name.replace(' ', '')}.app",
        ]
        for candidate in candidates:
            if os.path.exists(f"/Applications/{candidate}") or os.path.exists(f"/Applications/{candidate}"):
                return candidate
        return None

    def _is_builtin_app(self, target: str) -> bool:
        return target.lower() in {"chrome", "firefox", "safari", "terminal", "calculator", "spotify"}

    def _resolve_linux_command(self, target: str) -> list[str] | None:
        executable = shutil.which(target)
        if executable:
            return [executable]

        candidate_names = [
            target,
            target.replace(" ", "-"),
            target.replace(" ", "_"),
            (target + "-beta").replace(" ", "-"),
        ]
        for candidate in candidate_names:
            exe = shutil.which(candidate)
            if exe:
                return [exe]
        return None
