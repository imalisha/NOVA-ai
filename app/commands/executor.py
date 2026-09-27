import subprocess
import os

from app.commands.router import CommandRouter
from app.services.system import SystemService
from app.services.files import FileService
from app.services.whatsapp import WhatsappService


class CommandExecutor:

    def __init__(self):

        self.router = CommandRouter()

        self.system = SystemService()

        self.files = FileService()
        self.whatsapp = WhatsappService()

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

        if action == "OPEN_YOUTUBE":
            return self.open_youtube()

        if action == "OPEN_FACEBOOK":
            return self.open_facebook()

        if action == "OPEN_WHATSAPP":
            return self.open_whatsapp()

        if (
            isinstance(action,tuple)
            and action[0] == "OPEN_WHATSAPP_CHAT"
        ):
            contact_name = action[1]
            return self.whatsapp.open_chat(
                contact_name
            )

        if action == "CLOSE_WHATSAPP":
            return self.close_whatsapp()
        
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

        if action == "CLOSE_DOWNLOADS":
            return self.files.close_downloads()

        if action == "OPEN_DESKTOP":
            return self.files.open_desktop()

        if action == "CLOSE_DESKTOP":
            return self.files.close_desktop()

        if action == "OPEN_DOCUMENTS":
            return self.files.open_documents()

        if action == "CLOSE_DOCUMENTS":
            return self.files.close_documents()

        if action == "OPEN_PICTURES":
            return self.files.open_pictures()

        if action == "CLOSE_PICTURES":
            return self.files.close_pictures()

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

            return "CONFIRM_SHUTDOWN"

        if action == "RESTART":

            return "CONFIRM_RESTART"
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
    # WEBSITES
    # ========================================================

    def open_youtube(self):

        try:

            subprocess.Popen(
                [
                    "cmd",
                    "/c",
                    "start",
                    "",
                    "https://www.youtube.com"
                ]
            )

            return "Opening YouTube."

        except Exception as error:

            print(
                f"YouTube error: {error}"
            )

            return "I couldn't open YouTube."


    def open_facebook(self):

        try:

            subprocess.Popen(
                [
                    "cmd",
                    "/c",
                    "start",
                    "",
                    "https://www.facebook.com"
                ]
            )

            return "Opening Facebook."

        except Exception as error:

            print(
                f"Facebook error: {error}"
            )

            return "I couldn't open Facebook."

        # ========================================================
    # WHATSAPP
    # ========================================================

    def open_whatsapp(self):

        try:

            subprocess.Popen(
                [
                    "cmd",
                    "/c",
                    "start",
                    "",
                    "chrome",
                    "--app=https://web.whatsapp.com",
                    "--new-window"
                ]
            )

            return "Opening WhatsApp."

        except Exception as error:

            print(
                f"WhatsApp error: {error}"
            )

            return "I couldn't open WhatsApp."

    # ========================================================
    # CLOSE WHATSAPP
    # ========================================================

    def close_whatsapp(self):

        try:

            subprocess.run(
                [
                    "powershell",
                    "-Command",
                    "Get-Process chrome -ErrorAction SilentlyContinue | "
                    "Where-Object {$_.MainWindowTitle -like '*WhatsApp*'} | "
                    "Stop-Process -Force"
                ],
                capture_output=True,
                text=True
            )

            return "Closing WhatsApp."

        except Exception as error:

            print(
                f"WhatsApp close error: {error}"
            )

            return "I couldn't close WhatsApp."
      
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
