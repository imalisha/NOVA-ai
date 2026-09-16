# ============================================================
# NOVA COMMAND ROUTER
# ============================================================


class CommandRouter:

    def __init__(self):

        # ====================================================
        # OPEN VS CODE
        # ====================================================

        self.open_vscode_phrases = [

            # English
            "open vs code",
            "open vscode",
            "open visual studio code",

            # Roman Urdu
            "vs code kholo",
            "vs code khol do",
            "vs code kholna",
            "vscode kholo",
            "vscode khol do",

            # Urdu
            "وی ایس کوڈ کھولو",
            "وی ایس کوڈ کھول دو",
            "وی ایس کوڈ کھولیں",

            # Punjabi
            "وی ایس کوڈ کھول دے",
            "وی ایس کوڈ کھول دیو",

            # Roman Punjabi
            "vs code khol de",
            "vs code khol deo",
            "vs code khol dyo",
            "vscode khol de",
            "vscode khol deo",

            # Saraiki
            "vs code open kar",
            "vs code open kr",
            "vs code open kar dai",
            "vscode open kr deo",
        ]

        # ====================================================
        # CLOSE VS CODE
        # ====================================================

        self.close_vscode_phrases = [

            # English
            "close vs code",
            "close vscode",
            "close visual studio code",

            # Roman Urdu
            "vs code band karo",
            "vs code band kar do",
            "vs code band karna",
            "vscode band karo",
            "vscode band kar do",

            # Urdu
            "وی ایس کوڈ بند کرو",
            "وی ایس کوڈ بند کر دو",
            "وی ایس کوڈ بند کریں",

            # Punjabi
            "وی ایس کوڈ بند کر دے",
            "وی ایس کوڈ بند کرو",

            # Roman Punjabi
            "vs code band kar de",
            "vs code band kar deo",
            "vs code band dyo",
            "vscode band kar de",
            "vscode band kar deo",

            # Saraiki
            "vs code band kr",
            "vs code band kar",
            "vs code band kro",
            "vscode band karo",
        ]

        # ====================================================
        # OPEN CHROME
        # ====================================================

        self.open_chrome_phrases = [

            # English
            "open chrome",
            "open google chrome",
            "start chrome",

            # Roman Urdu
            "chrome kholo",
            "chrome khol do",
            "chrome kholna",

            # Roman Punjabi
            "chrome khol de",
            "chrome khol deo",
            "chrome khol dyo",

            # Urdu
            "کروم کھولو",
            "کروم کھول دو",
            "کروم کھولیں",

            # Saraiki
            "chrome open kar",
            "chrome open kr",
            "chrome open kar dai",
        ]

        # ====================================================
        # CLOSE CHROME
        # ====================================================

        self.close_chrome_phrases = [

            # English
            "close chrome",
            "close google chrome",
            "exit chrome",

            # Roman Urdu
            "chrome band karo",
            "chrome band kar do",

            # Roman Punjabi
            "chrome band kar de",
            "chrome band kar deo",
            "chrome band dyo",

            # Urdu
            "کروم بند کرو",
            "کروم بند کر دو",
            "کروم بند کریں",

            # Saraiki
            "chrome band kr",
            "chrome band kar",
            "chrome band kro",
        ]

        # ====================================================
        # OPEN CALCULATOR
        # ====================================================

        self.open_calculator_phrases = [

            # English
            "open calculator",
            "start calculator",

            # Roman Urdu
            "calculator kholo",
            "calculator khol do",
            "calculator kholna",

            # Roman Punjabi
            "calculator khol de",
            "calculator khol deo",

            # Urdu
            "کیلکولیٹر کھولو",
            "کیلکولیٹر کھول دو",
            "کیلکولیٹر کھولیں",

            # Saraiki
            "calculator open kar",
            "calculator open kr",
        ]

        # ====================================================
        # CLOSE CALCULATOR
        # ====================================================

        self.close_calculator_phrases = [

            # English
            "close calculator",
            "exit calculator",

            # Roman Urdu
            "calculator band karo",
            "calculator band kar do",

            # Roman Punjabi
            "calculator band kar de",
            "calculator band kar deo",

            # Urdu
            "کیلکولیٹر بند کرو",
            "کیلکولیٹر بند کر دو",
            "کیلکولیٹر بند کریں",

            # Saraiki
            "calculator band kr",
            "calculator band kar",
        ]

        # ====================================================
        # OPEN NOTEPAD
        # ====================================================

        self.open_notepad_phrases = [

            # English
            "open notepad",
            "start notepad",

            # Roman Urdu
            "notepad kholo",
            "notepad khol do",
            "notepad kholna",

            # Roman Punjabi
            "notepad khol de",
            "notepad khol deo",

            # Urdu
            "نوٹ پیڈ کھولو",
            "نوٹ پیڈ کھول دو",
            "نوٹ پیڈ کھولیں",

            # Saraiki
            "notepad open kar",
            "notepad open kr",
        ]

        # ====================================================
        # CLOSE NOTEPAD
        # ====================================================

        self.close_notepad_phrases = [

            # English
            "close notepad",
            "exit notepad",

            # Roman Urdu
            "notepad band karo",
            "notepad band kar do",

            # Roman Punjabi
            "notepad band kar de",
            "notepad band kar deo",

            # Urdu
            "نوٹ پیڈ بند کرو",
            "نوٹ پیڈ بند کر دو",
            "نوٹ پیڈ بند کریں",

            # Saraiki
            "notepad band kr",
            "notepad band kar",
        ]

        # ====================================================
        # OPEN FILE EXPLORER
        # ====================================================

        self.open_explorer_phrases = [

            # English
            "open file explorer",
            "open explorer",
            "open files",

            # Roman Urdu
            "file explorer kholo",
            "file explorer khol do",
            "files kholo",

            # Roman Punjabi
            "file explorer khol de",
            "file explorer khol deo",

            # Urdu
            "فائل ایکسپلورر کھولو",
            "فائل ایکسپلورر کھول دو",

            # Saraiki
            "file explorer open kar",
            "file explorer open kr",
        ]

        # ====================================================
        # CLOSE FILE EXPLORER
        # ====================================================

        self.close_explorer_phrases = [

            # English
            "close file explorer",
            "close explorer",

            # Roman Urdu
            "file explorer band karo",
            "file explorer band kar do",

            # Roman Punjabi
            "file explorer band kar de",
            "file explorer band kar deo",

            # Urdu
            "فائل ایکسپلورر بند کرو",
            "فائل ایکسپلورر بند کر دو",

            # Saraiki
            "file explorer band kr",
            "file explorer band kar",
        ]

    # ========================================================
    # ROUTE COMMAND
    # ========================================================

    def route(self, command):

        if not command:
            return None

        command = command.lower().strip()

        # ----------------------------------------------------
        # OPEN VS CODE
        # ----------------------------------------------------

        if any(
            phrase in command
            for phrase in self.open_vscode_phrases
        ):
            return "OPEN_VSCODE"

        # ----------------------------------------------------
        # CLOSE VS CODE
        # ----------------------------------------------------

        if any(
            phrase in command
            for phrase in self.close_vscode_phrases
        ):
            return "CLOSE_VSCODE"

        # ----------------------------------------------------
        # OPEN CHROME
        # ----------------------------------------------------

        if any(
            phrase in command
            for phrase in self.open_chrome_phrases
        ):
            return "OPEN_CHROME"

        # ----------------------------------------------------
        # CLOSE CHROME
        # ----------------------------------------------------

        if any(
            phrase in command
            for phrase in self.close_chrome_phrases
        ):
            return "CLOSE_CHROME"

        # ----------------------------------------------------
        # OPEN CALCULATOR
        # ----------------------------------------------------

        if any(
            phrase in command
            for phrase in self.open_calculator_phrases
        ):
            return "OPEN_CALCULATOR"

        # ----------------------------------------------------
        # CLOSE CALCULATOR
        # ----------------------------------------------------

        if any(
            phrase in command
            for phrase in self.close_calculator_phrases
        ):
            return "CLOSE_CALCULATOR"

        # ----------------------------------------------------
        # OPEN NOTEPAD
        # ----------------------------------------------------

        if any(
            phrase in command
            for phrase in self.open_notepad_phrases
        ):
            return "OPEN_NOTEPAD"

        # ----------------------------------------------------
        # CLOSE NOTEPAD
        # ----------------------------------------------------

        if any(
            phrase in command
            for phrase in self.close_notepad_phrases
        ):
            return "CLOSE_NOTEPAD"

        # ----------------------------------------------------
        # OPEN FILE EXPLORER
        # ----------------------------------------------------

        if any(
            phrase in command
            for phrase in self.open_explorer_phrases
        ):
            return "OPEN_EXPLORER"

        # ----------------------------------------------------
        # CLOSE FILE EXPLORER
        # ----------------------------------------------------

        if any(
            phrase in command
            for phrase in self.close_explorer_phrases
        ):
            return "CLOSE_EXPLORER"

        # ----------------------------------------------------
        # UNKNOWN
        # ----------------------------------------------------

        return None