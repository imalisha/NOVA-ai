# ============================================================
# NOVA COMMAND ROUTER
# ============================================================


class CommandRouter:

    def __init__(self):

        # ====================================================
        # APPLICATIONS
        # ====================================================

        self.open_vscode_phrases = [
            "open vs code",
            "open vscode",
            "open visual studio code",
            "vs code kholo",
            "vs code khol do",
            "vscode kholo",
            "vscode khol do",
            "وی ایس کوڈ کھولو",
            "وی ایس کوڈ کھول دو",
            "vs code khol de",
            "vs code khol deo",
            "vs code open kar",
            "vs code open kr",
        ]

        self.close_vscode_phrases = [
            "close vs code",
            "close vscode",
            "close visual studio code",
            "vs code band karo",
            "vs code band kar do",
            "vscode band karo",
            "vscode band kar do",
            "وی ایس کوڈ بند کرو",
            "وی ایس کوڈ بند کر دو",
            "vs code band kar de",
            "vs code band kar deo",
        ]

        self.open_chrome_phrases = [
            "open chrome",
            "open google chrome",
            "start chrome",
            "chrome kholo",
            "chrome khol do",
            "chrome kholna",
            "chrome khol de",
            "chrome khol deo",
            "کروم کھولو",
            "کروم کھول دو",
            "chrome open kar",
            "chrome open kr",
        ]

        self.close_chrome_phrases = [
            "close chrome",
            "close google chrome",
            "exit chrome",
            "chrome band karo",
            "chrome band kar do",
            "chrome band kar de",
            "chrome band kar deo",
            "کروم بند کرو",
            "کروم بند کر دو",
        ]

        # ====================================================
        # WEBSITES
        # ====================================================

        self.open_youtube_phrases = [
            "open youtube",
            "youtube kholo",
            "youtube khol do",
            "youtube open kar",
            "youtube open kr",
            "youtube chalao",
            "یوٹیوب کھولو",
            "یوٹیوب کھول دو",
        ]

        self.close_youtube_phrases = [
            "close youtube",
            "exit youtube",
            "youtube band karo",
            "youtube band kar do",
            "youtube band kar de",
            "youtube band kar deo",
            "یوٹیوب بند کرو",
            "یوٹیوب بند کر دو",
        ]

        self.open_facebook_phrases = [
            "open facebook",
            "facebook kholo",
            "facebook khol do",
            "facebook open kar",
            "facebook open kr",
            "فیس بک کھولو",
            "فیس بک کھول دو",
        ]

        self.close_facebook_phrases = [
            "close facebook",
            "exit facebook",
            "facebook band karo",
            "facebook band kar do",
            "facebook band kar de",
            "facebook band kar deo",
            "فیس بک بند کرو",
            "فیس بک بند کر دو",
        ]

        self.open_whatsapp_phrases = [
            "open whatsapp",
            "whatsapp kholo",
            "whatsapp khol do",
            "whatsapp open kar",
            "whatsapp open kr",
            "واٹس ایپ کھولو",
            "واٹس ایپ کھول دو",
        ]

        self.close_whatsapp_phrases = [
            "close whatsapp",
            "exit whatsapp",
            "whatsapp band karo",
            "whatsapp band kar do",
            "whatsapp band kar de",
            "whatsapp band kar deo",
            "واٹس ایپ بند کرو",
            "واٹس ایپ بند کر دو",
        ]
        # ====================================================
        # WHATSAPP CONTACT CHAT
        # ====================================================

        self.whatsapp_chat_phrases = [
            "chat with ",
            "whatsapp chat with ",
            "open chat with ",
            "chat karo ",
            "chat kar ",
            "whatsapp pe chat with ",
            "whatsapp par chat with ",
            "واٹس ایپ پر چیٹ ",
            "واٹس ایپ چیٹ "
        ]

        # ====================================================
        # CALCULATOR
        # ====================================================

        self.open_calculator_phrases = [
            "open calculator",
            "start calculator",
            "calculator kholo",
            "calculator khol do",
            "calculator kholna",
            "calculator khol de",
            "calculator khol deo",
            "کیلکولیٹر کھولو",
            "کیلکولیٹر کھول دو",
        ]

        self.close_calculator_phrases = [
            "close calculator",
            "exit calculator",
            "calculator band karo",
            "calculator band kar do",
            "calculator band kar de",
            "calculator band kar deo",
            "کیلکولیٹر بند کرو",
            "کیلکولیٹر بند کر دو",
        ]

        # ====================================================
        # NOTEPAD
        # ====================================================

        self.open_notepad_phrases = [
            "open notepad",
            "start notepad",
            "notepad kholo",
            "notepad khol do",
            "notepad kholna",
            "notepad khol de",
            "notepad khol deo",
            "نوٹ پیڈ کھولو",
            "نوٹ پیڈ کھول دو",
        ]

        self.close_notepad_phrases = [
            "close notepad",
            "exit notepad",
            "notepad band karo",
            "notepad band kar do",
            "notepad band kar de",
            "notepad band kar deo",
            "نوٹ پیڈ بند کرو",
            "نوٹ پیڈ بند کر دو",
        ]

        # ====================================================
        # FILE EXPLORER
        # ====================================================

        self.open_explorer_phrases = [
            "open file explorer",
            "open explorer",
            "open files",
            "file explorer kholo",
            "file explorer khol do",
            "files kholo",
            "file explorer khol de",
            "file explorer khol deo",
            "فائل ایکسپلورر کھولو",
            "فائل ایکسپلورر کھول دو",
        ]

        self.close_explorer_phrases = [
            "close file explorer",
            "close explorer",
            "file explorer band karo",
            "file explorer band kar do",
            "file explorer band kar de",
            "file explorer band kar deo",
            "فائل ایکسپلورر بند کرو",
            "فائل ایکسپلورر بند کر دو",
        ]

        # ====================================================
        # FOLDERS - DOWNLOADS
        # ====================================================

        self.open_downloads_phrases = [
            "open downloads",
            "open download",
            "downloads kholo",
            "downloads khol do",
            "download kholo",
            "download khol do",
            "downloads open kar",
            "downloads open kr",
            "ڈاؤن لوڈز کھولو",
            "ڈاؤن لوڈ کھولو",
        ]

        self.close_downloads_phrases = [
            "close downloads",
            "close download",
            "downloads band karo",
            "downloads band kar do",
            "downloads band kar de",
            "downloads band kar deo",
            "download band karo",
            "download band kar do",
            "ڈاؤن لوڈز بند کرو",
            "ڈاؤن لوڈ بند کرو",
        ]

        # ====================================================
        # FOLDERS - DESKTOP
        # ====================================================

        self.open_desktop_phrases = [
            "open desktop",
            "desktop kholo",
            "desktop khol do",
            "desktop open kar",
            "desktop open kr",
            "ڈیسک ٹاپ کھولو",
            "ڈیسک ٹاپ کھول دو",
        ]

        self.close_desktop_phrases = [
            "close desktop",
            "desktop band karo",
            "desktop band kar do",
            "desktop band kar de",
            "desktop band kar deo",
            "ڈیسک ٹاپ بند کرو",
            "ڈیسک ٹاپ بند کر دو",
        ]

        # ====================================================
        # FOLDERS - DOCUMENTS
        # ====================================================

        self.open_documents_phrases = [
            "open documents",
            "open document",
            "documents kholo",
            "documents khol do",
            "documents open kar",
            "documents open kr",
            "دستاویزات کھولو",
            "ڈاکومنٹس کھولو",
        ]

        self.close_documents_phrases = [
            "close documents",
            "close document",
            "documents band karo",
            "documents band kar do",
            "documents band kar de",
            "documents band kar deo",
            "document band karo",
            "document band kar do",
            "دستاویزات بند کرو",
            "ڈاکومنٹس بند کرو",
        ]

        # ====================================================
        # FOLDERS - PICTURES
        # ====================================================

        self.open_pictures_phrases = [
            "open pictures",
            "open picture folder",
            "pictures kholo",
            "pictures khol do",
            "pictures open kar",
            "pictures open kr",
            "تصاویر کھولو",
        ]

        self.close_pictures_phrases = [
            "close pictures",
            "close picture folder",
            "pictures band karo",
            "pictures band kar do",
            "pictures band kar de",
            "pictures band kar deo",
            "picture folder band karo",
            "تصاویر بند کرو",
        ]

        # ====================================================
        # SYSTEM
        # ====================================================

        self.lock_phrases = [
            "lock computer",
            "lock pc",
            "lock my computer",
            "computer lock karo",
            "pc lock karo",
            "computer lock kar do",
            "کمپیوٹر لاک کرو",
            "کمپیوٹر لاک کر دو",
        ]

        self.screenshot_phrases = [
            "take screenshot",
            "capture screenshot",
            "screenshot lo",
            "screenshot le lo",
            "screenshot lein",
            "screenshot bana do",
            "اسکرین شاٹ لو",
            "اسکرین شاٹ لے لو",
        ]

        self.volume_up_phrases = [
            "volume up",
            "increase volume",
            "volume increase",
            "volume tez karo",
            "volume teez karo",
            "volume barhao",
            "volume badhao",
            "awaz barhao",
            "awaz badhao",
            "آواز بڑھاؤ",
            "والیوم بڑھاؤ",
        ]

        self.volume_down_phrases = [
            "volume down",
            "decrease volume",
            "volume decrease",
            "volume kam karo",
            "awaz kam karo",
            "آواز کم کرو",
            "والیوم کم کرو",
        ]

        self.mute_phrases = [
            "mute",
            "mute volume",
            "sound mute karo",
            "awaz band karo",
            "آواز بند کرو",
            "میوٹ کرو",
        ]

        self.play_pause_phrases = [
            "play music",
            "pause music",
            "play pause",
            "play or pause",
            "music chalao",
            "music roko",
            "music pause karo",
            "میوزک چلاؤ",
            "میوزک روکو",
        ]

        # ====================================================
        # POWER
        # ====================================================

        self.shutdown_phrases = [
            "shutdown computer",
            "shutdown",
            "shutdown pc",
            "shut down computer",
            "shut down pc",
            "computer shutdown karo",
            "pc shutdown karo",
            "کمپیوٹر بند کرو",
            "کمپیوٹر شٹ ڈاؤن کرو",
        ]

        self.restart_phrases = [
            "restart",
            "restart computer",
            "restart pc",
            "reboot computer",
            "computer restart karo",
            "pc restart karo",
            "کمپیوٹر ری اسٹارٹ کرو",
            "کمپیوٹر دوبارہ شروع کرو",
        ]

    # ========================================================
    # ROUTE
    # ========================================================

    def route(self, command):

        if not command:
            return None

        command = command.lower().strip()

        # ====================================================
        # VS CODE
        # ====================================================

        if any(
            phrase in command
            for phrase in self.open_vscode_phrases
        ):
            return "OPEN_VSCODE"

        if any(
            phrase in command
            for phrase in self.close_vscode_phrases
        ):
            return "CLOSE_VSCODE"

        # ====================================================
        # CHROME
        # ====================================================

        if any(
            phrase in command
            for phrase in self.open_chrome_phrases
        ):
            return "OPEN_CHROME"

        if any(
            phrase in command
            for phrase in self.close_chrome_phrases
        ):
            return "CLOSE_CHROME"

        # ====================================================
        # WEBSITES
        # ====================================================

        if any(
            phrase in command
            for phrase in self.open_youtube_phrases
        ):
            return "OPEN_YOUTUBE"

        if any(
            phrase in command
            for phrase in self.close_youtube_phrases
        ):
            return "CLOSE_YOUTUBE"

        if any(
            phrase in command
            for phrase in self.open_facebook_phrases
        ):
            return "OPEN_FACEBOOK"

        if any(
            phrase in command
            for phrase in self.close_facebook_phrases
        ):
            return "CLOSE_FACEBOOK"

        if any(
            phrase in command
            for phrase in self.open_whatsapp_phrases
        ):
            return "OPEN_WHATSAPP"

        if any(
            phrase in command
            for phrase in self.close_whatsapp_phrases
        ):
            return "CLOSE_WHATSAPP"

        # ====================================================
        # WHATSAPP CONTACT CHAT
        # ====================================================

        for phrase in self.whatsapp_chat_phrases:

            if phrase in command:

                contact_name = command.split(
                    phrase,
                    1
                )[1].strip()

                if contact_name:

                    return (
                        "OPEN_WHATSAPP_CHAT",
                        contact_name
                    )
        # ====================================================
        # CALCULATOR
        # ====================================================

        if any(
            phrase in command
            for phrase in self.open_calculator_phrases
        ):
            return "OPEN_CALCULATOR"

        if any(
            phrase in command
            for phrase in self.close_calculator_phrases
        ):
            return "CLOSE_CALCULATOR"

        # ====================================================
        # NOTEPAD
        # ====================================================

        if any(
            phrase in command
            for phrase in self.open_notepad_phrases
        ):
            return "OPEN_NOTEPAD"

        if any(
            phrase in command
            for phrase in self.close_notepad_phrases
        ):
            return "CLOSE_NOTEPAD"

        # ====================================================
        # FILE EXPLORER
        # ====================================================

        if any(
            phrase in command
            for phrase in self.open_explorer_phrases
        ):
            return "OPEN_EXPLORER"

        if any(
            phrase in command
            for phrase in self.close_explorer_phrases
        ):
            return "CLOSE_EXPLORER"

        # ====================================================
        # DOWNLOADS
        # ====================================================

        if any(
            phrase in command
            for phrase in self.close_downloads_phrases
        ):
            return "CLOSE_DOWNLOADS"

        if any(
            phrase in command
            for phrase in self.open_downloads_phrases
        ):
            return "OPEN_DOWNLOADS"

        # ====================================================
        # DESKTOP
        # ====================================================

        if any(
            phrase in command
            for phrase in self.close_desktop_phrases
        ):
            return "CLOSE_DESKTOP"

        if any(
            phrase in command
            for phrase in self.open_desktop_phrases
        ):
            return "OPEN_DESKTOP"

        # ====================================================
        # DOCUMENTS
        # ====================================================

        if any(
            phrase in command
            for phrase in self.close_documents_phrases
        ):
            return "CLOSE_DOCUMENTS"

        if any(
            phrase in command
            for phrase in self.open_documents_phrases
        ):
            return "OPEN_DOCUMENTS"

        # ====================================================
        # PICTURES
        # ====================================================

        if any(
            phrase in command
            for phrase in self.close_pictures_phrases
        ):
            return "CLOSE_PICTURES"

        if any(
            phrase in command
            for phrase in self.open_pictures_phrases
        ):
            return "OPEN_PICTURES"

        # ====================================================
        # SYSTEM
        # ====================================================

        if any(
            phrase in command
            for phrase in self.lock_phrases
        ):
            return "LOCK_COMPUTER"

        if any(
            phrase in command
            for phrase in self.screenshot_phrases
        ):
            return "TAKE_SCREENSHOT"

        if any(
            phrase in command
            for phrase in self.volume_up_phrases
        ):
            return "VOLUME_UP"

        if any(
            phrase in command
            for phrase in self.volume_down_phrases
        ):
            return "VOLUME_DOWN"

        if any(
            phrase in command
            for phrase in self.mute_phrases
        ):
            return "MUTE"

        if any(
            phrase in command
            for phrase in self.play_pause_phrases
        ):
            return "PLAY_PAUSE"

        # ====================================================
        # POWER
        # ====================================================

        if any(
            phrase in command
            for phrase in self.shutdown_phrases
        ):
            return "SHUTDOWN"

        if any(
            phrase in command
            for phrase in self.restart_phrases
        ):
            return "RESTART"

        # ====================================================
        # UNKNOWN
        # ====================================================

        return None