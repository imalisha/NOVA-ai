from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QFrame,
    QHBoxLayout,
    QComboBox,
    QCheckBox
)


class SettingsPage(QWidget):

    def __init__(self, parent=None):

        super().__init__(parent)

        self.setup_ui()

    # =========================================================
    # UI
    # =========================================================

    def setup_ui(self):

        layout = QVBoxLayout(self)

        layout.setContentsMargins(
            25,
            25,
            25,
            25
        )

        layout.setSpacing(18)

        title = QLabel(
            "Settings"
        )

        title.setObjectName(
            "settingsTitle"
        )

        layout.addWidget(
            title
        )

        subtitle = QLabel(
            "Configure how NOVA works."
        )

        subtitle.setObjectName(
            "settingsSubtitle"
        )

        layout.addWidget(
            subtitle
        )

        # -----------------------------------------------------
        # VOICE
        # -----------------------------------------------------

        layout.addWidget(
            self.setting_card(
                "VOICE ASSISTANT",
                "Enable NOVA voice interaction",
                QCheckBox("Enabled")
            )
        )

        # -----------------------------------------------------
        # LANGUAGE
        # -----------------------------------------------------

        language = QComboBox()

        language.addItems([
            "English",
            "Urdu",
            "Punjabi",
            "Saraiki"
        ])

        layout.addWidget(
            self.setting_card(
                "LANGUAGE",
                "Preferred NOVA language",
                language
            )
        )

        # -----------------------------------------------------
        # STARTUP
        # -----------------------------------------------------

        layout.addWidget(
            self.setting_card(
                "STARTUP",
                "Launch NOVA when Windows starts",
                QCheckBox("Launch on startup")
            )
        )

        # -----------------------------------------------------
        # CONFIRMATION
        # -----------------------------------------------------

        layout.addWidget(
            self.setting_card(
                "COMMAND SAFETY",
                "Ask before executing sensitive commands",
                QCheckBox("Require confirmation")
            )
        )

        layout.addStretch()

        self.setStyleSheet("""

            QLabel#settingsTitle {
                color: white;
                font-size: 30px;
                font-weight: 900;
            }

            QLabel#settingsSubtitle {
                color: #716879;
                font-size: 11px;
            }

            QFrame#settingCard {
                background: #0d0a14;
                border: 1px solid #251d37;
                border-radius: 16px;
            }

            QLabel#settingTitle {
                color: #ddd6e7;
                font-size: 10px;
                font-weight: 900;
                letter-spacing: 1px;
            }

            QLabel#settingDescription {
                color: #625a6b;
                font-size: 8px;
            }

            QComboBox {
                background: #100c18;
                color: #a997c4;
                border: 1px solid #30244a;
                border-radius: 8px;
                padding: 8px;
                min-width: 120px;
            }

            QCheckBox {
                color: #978ba6;
                font-size: 9px;
            }

            QCheckBox::indicator {
                width: 16px;
                height: 16px;
            }

        """)

    # =========================================================
    # SETTING CARD
    # =========================================================

    def setting_card(
        self,
        title,
        description,
        control
    ):

        frame = QFrame()

        frame.setObjectName(
            "settingCard"
        )

        row = QHBoxLayout(
            frame
        )

        row.setContentsMargins(
            18,
            15,
            18,
            15
        )

        text = QVBoxLayout()

        title_label = QLabel(
            title
        )

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