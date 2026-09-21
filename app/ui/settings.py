from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QFrame,
    QHBoxLayout,
    QComboBox,
    QCheckBox
)

from PySide6.QtCore import Signal, QSettings


class SettingsPage(QWidget):

    # ============================================================
    # SIGNALS
    # ============================================================

    hands_free_changed = Signal(bool)

    # ============================================================
    # INIT
    # ============================================================

    def __init__(self, parent=None):
        super().__init__(parent)

        # Save settings on Windows
        self.settings = QSettings("NOVA", "NOVA AI")

        self.setup_ui()

    # ============================================================
    # UI
    # ============================================================

    def setup_ui(self):

        layout = QVBoxLayout(self)

        layout.setContentsMargins(25, 25, 25, 25)
        layout.setSpacing(18)

        # ========================================================
        # TITLE
        # ========================================================

        title = QLabel("Settings")
        title.setObjectName("settingsTitle")

        layout.addWidget(title)

        # ========================================================
        # SUBTITLE
        # ========================================================

        subtitle = QLabel(
            "Configure how NOVA works."
        )

        subtitle.setObjectName("settingsSubtitle")

        layout.addWidget(subtitle)

        # ========================================================
        # VOICE ASSISTANT
        # ========================================================

        self.voice_checkbox = QCheckBox("Enabled")

        voice_enabled = self.settings.value(
            "voice_enabled",
            True,
            type=bool
        )

        self.voice_checkbox.setChecked(voice_enabled)

        self.voice_checkbox.stateChanged.connect(
            self.voice_setting_changed
        )

        layout.addWidget(
            self.setting_card(
                "VOICE ASSISTANT",
                "Enable NOVA voice interaction",
                self.voice_checkbox
            )
        )

        # ========================================================
        # HANDS-FREE MODE
        # ========================================================

        self.hands_free_checkbox = QCheckBox(
            'Enabled'
        )

        hands_free_enabled = self.settings.value(
            "hands_free_enabled",
            True,
            type=bool
        )

        self.hands_free_checkbox.setChecked(
            hands_free_enabled
        )

        self.hands_free_checkbox.stateChanged.connect(
            self.hands_free_setting_changed
        )

        layout.addWidget(
            self.setting_card(
                "HANDS-FREE MODE",
                'Wake NOVA by saying "Hello Nova"',
                self.hands_free_checkbox
            )
        )

        # ========================================================
        # LANGUAGE
        # ========================================================

        language = QComboBox()

        language.addItems([
            "English",
            "Urdu",
            "Punjabi",
            "Saraiki"
        ])

        saved_language = self.settings.value(
            "language",
            "English"
        )

        index = language.findText(saved_language)

        if index >= 0:
            language.setCurrentIndex(index)

        language.currentTextChanged.connect(
            self.language_changed
        )

        layout.addWidget(
            self.setting_card(
                "LANGUAGE",
                "Preferred NOVA language",
                language
            )
        )

        # ========================================================
        # STARTUP
        # ========================================================

        startup_checkbox = QCheckBox(
            "Launch on startup"
        )

        startup_enabled = self.settings.value(
            "startup_enabled",
            False,
            type=bool
        )

        startup_checkbox.setChecked(
            startup_enabled
        )

        startup_checkbox.stateChanged.connect(
            self.startup_changed
        )

        layout.addWidget(
            self.setting_card(
                "STARTUP",
                "Launch NOVA when Windows starts",
                startup_checkbox
            )
        )

        # ========================================================
        # COMMAND SAFETY
        # ========================================================

        safety_checkbox = QCheckBox(
            "Require confirmation"
        )

        safety_enabled = self.settings.value(
            "confirmation_enabled",
            False,
            type=bool
        )

        safety_checkbox.setChecked(
            safety_enabled
        )

        safety_checkbox.stateChanged.connect(
            self.safety_changed
        )

        layout.addWidget(
            self.setting_card(
                "COMMAND SAFETY",
                "Ask before executing sensitive commands",
                safety_checkbox
            )
        )

        layout.addStretch()

        # ========================================================
        # STYLE
        # ========================================================

        self.setStyleSheet("""
            QLabel#settingsTitle {
                color: #ffffff;
                font-size: 28px;
                font-weight: 700;
            }

            QLabel#settingsSubtitle {
                color: #8f8fa8;
                font-size: 14px;
                margin-bottom: 10px;
            }

            QFrame#settingCard {
                background-color: #151525;
                border: 1px solid #292943;
                border-radius: 14px;
            }

            QLabel#settingTitle {
                color: #ffffff;
                font-size: 15px;
                font-weight: 700;
            }

            QLabel#settingDescription {
                color: #85859c;
                font-size: 12px;
                margin-top: 3px;
            }

            QCheckBox {
                color: #ffffff;
                font-size: 13px;
                spacing: 8px;
            }

            QCheckBox::indicator {
                width: 18px;
                height: 18px;
            }

            QCheckBox::indicator:unchecked {
                background-color: #202036;
                border: 1px solid #454563;
                border-radius: 5px;
            }

            QCheckBox::indicator:checked {
                background-color: #7c3aed;
                border: 1px solid #9f67ff;
                border-radius: 5px;
            }

            QComboBox {
                background-color: #202036;
                color: #ffffff;
                border: 1px solid #454563;
                border-radius: 8px;
                padding: 7px 12px;
                min-width: 120px;
            }

            QComboBox:hover {
                border: 1px solid #7c3aed;
            }
        """)

    # ============================================================
    # SETTING CARD
    # ============================================================

    def setting_card(self, title, description, control):

        frame = QFrame()

        frame.setObjectName(
            "settingCard"
        )

        row = QHBoxLayout(frame)

        row.setContentsMargins(
            18,
            15,
            18,
            15
        )

        text = QVBoxLayout()

        title_label = QLabel(title)

        title_label.setObjectName(
            "settingTitle"
        )

        text.addWidget(
            title_label
        )

        description_label = QLabel(
            description
        )

        description_label.setObjectName(
            "settingDescription"
        )

        text.addWidget(
            description_label
        )

        row.addLayout(
            text
        )

        row.addStretch()

        row.addWidget(
            control
        )

        return frame

    # ============================================================
    # VOICE SETTING
    # ============================================================

    def voice_setting_changed(self, state):

        enabled = state != 0

        self.settings.setValue(
            "voice_enabled",
            enabled
        )

        print(
            f"NOVA SETTINGS: Voice enabled = {enabled}"
        )

    # ============================================================
    # HANDS-FREE SETTING
    # ============================================================

    def hands_free_setting_changed(self, state):

        enabled = state != 0

        self.settings.setValue(
            "hands_free_enabled",
            enabled
        )

        print(
            f"NOVA SETTINGS: Hands-free enabled = {enabled}"
        )

        self.hands_free_changed.emit(
            enabled
        )

    # ============================================================
    # LANGUAGE
    # ============================================================

    def language_changed(self, language):

        self.settings.setValue(
            "language",
            language
        )

        print(
            f"NOVA SETTINGS: Language = {language}"
        )

    # ============================================================
    # STARTUP
    # ============================================================

    def startup_changed(self, state):

        enabled = state != 0

        self.settings.setValue(
            "startup_enabled",
            enabled
        )

        print(
            f"NOVA SETTINGS: Startup = {enabled}"
        )

    # ============================================================
    # SAFETY
    # ============================================================

    def safety_changed(self, state):

        enabled = state != 0

        self.settings.setValue(
            "confirmation_enabled",
            enabled
        )

        print(
            f"NOVA SETTINGS: Confirmation = {enabled}"
        )