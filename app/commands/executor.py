import subprocess
import os

from app.commands.router import CommandRouter
from app.services.system import SystemService
from app.services.files import FileService


class CommandExecutor:

    def __init__(self):

        self.router = CommandRouter()

        self.system = SystemService()

        self.files = FileService()

    # ========================================================
    # MAIN EXECUTOR
    # ========================================================

    def execute(self, command):

        if not command:

            return "I didn't hear a command."

        action = self.router.route(
            command
        )

        print(
            f"NOVA EXECUTOR: Command = {command}"
        )

        print(
            f"NOVA EXECUTOR: Action = {action}"
        )

        # ====================================================
        # APPLICATIONS
        # ====================================================

        if action == "OPEN_VSCODE":
            return self.open_vscode()

        if action == "CLOSE_VSCODE":
            return self.close_vscode()

        if action == "OPEN_CHROME":
            return self.open_chrome()

        if action == "CLOSE_CHROME":
            return self.close_chrome()

        if action == "OPEN_CALCULATOR":
            return self.open_calculator()

        if action == "CLOSE_CALCULATOR":
            return self.close_calculator()

        if action == "OPEN_NOTEPAD":
            return self.open_notepad()

        if action == "CLOSE_NOTEPAD":
            return self.close_notepad()

        if action == "OPEN_EXPLORER":
            return self.open_explorer()

        if action == "CLOSE_EXPLORER":
            return self.close_explorer()

        # ====================================================
        # FOLDERS
        # ====================================================

        if action == "OPEN_DOWNLOADS":
            return self.files.open_downloads()

        if action == "OPEN_DESKTOP":
            return self.files.open_desktop()

        if action == "OPEN_DOCUMENTS":
            return self.files.open_documents()

        if action == "OPEN_PICTURES":
            return self.files.open_pictures()

        # ====================================================
        # SYSTEM
        # ====================================================

        if action == "LOCK_COMPUTER":
            return self.system.lock_computer()

        if action == "TAKE_SCREENSHOT":
            return self.system.take_screenshot()

        if action == "VOLUME_UP":
            return self.system.volume_up()

        if action == "VOLUME_DOWN":
            return self.system.volume_down()

        if action == "MUTE":
            return self.system.mute()

        if action == "PLAY_PAUSE":
            return self.system.play_pause()

        # ====================================================
        # POWER
        # ====================================================

        if action == "SHUTDOWN":

            return (
                "Shutdown command recognized. "
                "Confirmation will be required."
            )

        if action == "RESTART":

            return (
                "Restart command recognized. "
                "Confirmation will be required."
            )

        # ====================================================
        # UNKNOWN
        # ====================================================

        return (
            "I heard you, but I don't know "
            "how to do that yet."
        )

    # ========================================================
    # VS CODE
    # ========================================================

    def open_vscode(self):

        vscode_path = os.path.expandvars(
            r"%LOCALAPPDATA%\Programs\Microsoft VS Code\Code.exe"
        )

        if os.path.exists(vscode_path):

            try:

                subprocess.Popen(
                    [vscode_path]
                )

                return (
                    "Opening Visual Studio Code."
                )

            except Exception as error:

                print(
                    f"VS Code error: {error}"
                )

                return (
                    "I couldn't open "
                    "Visual Studio Code."
                )

        return (
            "I couldn't find "
            "Visual Studio Code."
        )

    # ========================================================
    # CLOSE VS CODE
    # ========================================================

    def close_vscode(self):

        subprocess.run(
            [
                "taskkill",
                "/IM",
                "Code.exe",
                "/F"
            ],
            capture_output=True
        )

        return (
            "Closing Visual Studio Code."
        )

    # ========================================================
    # CHROME
    # ========================================================

    def open_chrome(self):

        try:

            subprocess.Popen(
                [
                    "cmd",
                    "/c",
                    "start",
                    "",
                    "chrome"
                ]
            )

            return (
                "Opening Google Chrome."
            )

        except Exception as error:

            print(
                f"Chrome error: {error}"
            )

            return (
                "I couldn't open "
                "Google Chrome."
            )

    def close_chrome(self):

        subprocess.run(
            [
                "taskkill",
                "/IM",
                "chrome.exe",
                "/F"
            ],
            capture_output=True
        )

        return (
            "Closing Google Chrome."
        )

    # ========================================================
    # CALCULATOR
    # ========================================================

    def open_calculator(self):

        try:

            subprocess.Popen(
                ["calc.exe"]
            )

            return (
                "Opening Calculator."
            )

        except Exception as error:

            print(
                f"Calculator error: {error}"
            )

            return (
                "I couldn't open Calculator."
            )

    def close_calculator(self):

        subprocess.run(
            [
                "taskkill",
                "/IM",
                "CalculatorApp.exe",
                "/F"
            ],
            capture_output=True
        )

        return (
            "Closing Calculator."
        )

    # ========================================================
    # NOTEPAD
    # ========================================================

    def open_notepad(self):

        try:

            subprocess.Popen(
                ["notepad.exe"]
            )

            return (
                "Opening Notepad."
            )

        except Exception as error:

            print(
                f"Notepad error: {error}"
            )

            return (
                "I couldn't open Notepad."
            )

    def close_notepad(self):

        subprocess.run(
            [
                "taskkill",
                "/IM",
                "notepad.exe",
                "/F"
            ],
            capture_output=True
        )

        return (
            "Closing Notepad."
        )

    # ========================================================
    # FILE EXPLORER
    # ========================================================

    def open_explorer(self):

        try:

            subprocess.Popen(
                ["explorer.exe"]
            )

            return (
                "Opening File Explorer."
            )

        except Exception as error:

            print(
                f"File Explorer error: {error}"
            )

            return (
                "I couldn't open "
                "File Explorer."
            )

    def close_explorer(self):

        subprocess.run(
            [
                "taskkill",
                "/IM",
                "explorer.exe",
                "/F"
            ],
            capture_output=True
        )

        return (
            "Closing File Explorer."
        )