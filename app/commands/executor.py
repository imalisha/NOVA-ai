import subprocess
import os


from app.commands.router import CommandRouter


class CommandExecutor:

    def __init__(self):
        self.router = CommandRouter()

    def execute(self, command):

        if not command:
            return "I didn't hear a command."

        action = self.router.route(command)

        # ====================================================
        # OPEN VS CODE
        # ====================================================

        if action == "OPEN_VSCODE":
            return self.open_vscode()

        # ====================================================
        # CLOSE VS CODE
        # ====================================================

        if action == "CLOSE_VSCODE":
            return self.close_vscode()

        # ====================================================
        # OPEN CHROME
        # ====================================================

        if action == "OPEN_CHROME":
            return self.open_chrome()

        # ====================================================
        # CLOSE CHROME
        # ====================================================

        if action == "CLOSE_CHROME":
            return self.close_chrome()

        # ====================================================
        # OPEN CALCULATOR
        # ====================================================

        if action == "OPEN_CALCULATOR":
            return self.open_calculator()

        # ====================================================
        # CLOSE CALCULATOR
        # ====================================================

        if action == "CLOSE_CALCULATOR":
            return self.close_calculator()

        # ====================================================
        # OPEN NOTEPAD
        # ====================================================

        if action == "OPEN_NOTEPAD":
            return self.open_notepad()

        # ====================================================
        # CLOSE NOTEPAD
        # ====================================================

        if action == "CLOSE_NOTEPAD":
            return self.close_notepad()

        # ====================================================
        # OPEN FILE EXPLORER
        # ====================================================

        if action == "OPEN_EXPLORER":
            return self.open_explorer()

        # ====================================================
        # CLOSE FILE EXPLORER
        # ====================================================

        if action == "CLOSE_EXPLORER":
            return self.close_explorer()

        # ====================================================
        # UNKNOWN COMMAND
        # ====================================================

        return (
            "I heard you, but I don't know "
            "how to do that yet."
        )

    # ========================================================
    # OPEN VS CODE
    # ========================================================

    def open_vscode(self):

        vscode_path = os.path.expandvars(
            r"%LOCALAPPDATA%\Programs\Microsoft VS Code\Code.exe"
        )

        if os.path.exists(vscode_path):

            try:
                subprocess.Popen([vscode_path])

                return "Opening Visual Studio Code."

            except Exception as error:

                print(f"VS Code error: {error}")

                return "I couldn't open Visual Studio Code."

        return "I couldn't find Visual Studio Code."

    # ========================================================
    # CLOSE VS CODE
    # ========================================================

    def close_vscode(self):

        subprocess.run(
            ["taskkill", "/IM", "Code.exe", "/F"],
            capture_output=True
        )

        return "Closing Visual Studio Code."

    # ========================================================
    # OPEN CHROME
    # ========================================================

    def open_chrome(self):

        try:
            subprocess.Popen(
                ["cmd", "/c", "start", "", "chrome"]
            )

            return "Opening Google Chrome."

        except Exception as error:

            print(f"Chrome error: {error}")

            return "I couldn't open Google Chrome."

    # ========================================================
    # CLOSE CHROME
    # ========================================================

    def close_chrome(self):

        subprocess.run(
            ["taskkill", "/IM", "chrome.exe", "/F"],
            capture_output=True
        )

        return "Closing Google Chrome."

    # ========================================================
    # OPEN CALCULATOR
    # ========================================================

    def open_calculator(self):

        try:
            subprocess.Popen(
                ["calc.exe"]
            )

            return "Opening Calculator."

        except Exception as error:

            print(f"Calculator error: {error}")

            return "I couldn't open Calculator."

    # ========================================================
    # CLOSE CALCULATOR
    # ========================================================

    def close_calculator(self):

        subprocess.run(
            ["taskkill", "/IM", "CalculatorApp.exe", "/F"],
            capture_output=True
        )

        return "Closing Calculator."

    # ========================================================
    # OPEN NOTEPAD
    # ========================================================

    def open_notepad(self):

        try:
            subprocess.Popen(
                ["notepad.exe"]
            )

            return "Opening Notepad."

        except Exception as error:

            print(f"Notepad error: {error}")

            return "I couldn't open Notepad."

    # ========================================================
    # CLOSE NOTEPAD
    # ========================================================

    def close_notepad(self):

        subprocess.run(
            ["taskkill", "/IM", "notepad.exe", "/F"],
            capture_output=True
        )

        return "Closing Notepad."

    # ========================================================
    # OPEN FILE EXPLORER
    # ========================================================

    def open_explorer(self):

        try:
            subprocess.Popen(
                ["explorer.exe"]
            )

            return "Opening File Explorer."

        except Exception as error:

            print(f"File Explorer error: {error}")

            return "I couldn't open File Explorer."

    # ========================================================
    # CLOSE FILE EXPLORER
    # ========================================================

    def close_explorer(self):

        subprocess.run(
            ["taskkill", "/IM", "explorer.exe", "/F"],
            capture_output=True
        )

        return "Closing File Explorer."