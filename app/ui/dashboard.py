from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QFrame,
    QHBoxLayout,
    QPushButton
)
from PySide6.QtCore import Qt


class Dashboard(QWidget):

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

        layout.setSpacing(20)

        # -----------------------------------------------------
        # HEADER
        # -----------------------------------------------------

        title = QLabel(
            "Dashboard"
        )

        title.setObjectName(
            "dashboardTitle"
        )

        layout.addWidget(title)

        subtitle = QLabel(
            "Welcome back. NOVA is ready to assist you."
        )

        subtitle.setObjectName(
            "dashboardSubtitle"
        )

        layout.addWidget(subtitle)

        # -----------------------------------------------------
        # STATUS
        # -----------------------------------------------------

        status_card = QFrame()

        status_card.setObjectName(
            "dashboardCard"
        )

        status_layout = QHBoxLayout(
            status_card
        )

        status_layout.setContentsMargins(
            20,
            18,
            20,
            18
        )

        status_text = QVBoxLayout()

        status_title = QLabel(
            "NOVA STATUS"
        )

        status_title.setObjectName(
            "cardTitle"
        )

        status_text.addWidget(
            status_title
        )

        status_value = QLabel(
            "● ONLINE"
        )

        status_value.setObjectName(
            "statusValue"
        )

        status_text.addWidget(
            status_value
        )

        status_layout.addLayout(
            status_text
        )

        status_layout.addStretch()

        layout.addWidget(
            status_card
        )

        # -----------------------------------------------------
        # QUICK COMMANDS
        # -----------------------------------------------------

        commands_title = QLabel(
            "QUICK COMMANDS"
        )

        commands_title.setObjectName(
            "sectionTitle"
        )

        layout.addWidget(
            commands_title
        )

        command_row = QHBoxLayout()

        commands = [
            "OPEN VS CODE",
            "OPEN CHROME",
            "OPEN TERMINAL",
            "OPEN GALLERY"
        ]

        for command in commands:

            button = QPushButton(
                command
            )

            button.setObjectName(
                "dashboardButton"
            )

            command_row.addWidget(
                button
            )

        layout.addLayout(
            command_row
        )

        layout.addStretch()

        # -----------------------------------------------------
        # STYLE
        # -----------------------------------------------------

        self.setStyleSheet("""

            QLabel#dashboardTitle {
                color: white;
                font-size: 30px;
                font-weight: 900;
            }

            QLabel#dashboardSubtitle {
                color: #777080;
                font-size: 11px;
            }

            QFrame#dashboardCard {
                background: #0d0a14;
                border: 1px solid #28203c;
                border-radius: 18px;
            }

            QLabel#cardTitle {
                color: #625976;
                font-size: 8px;
                font-weight: 900;
                letter-spacing: 2px;
            }

            QLabel#statusValue {
                color: #9c83f5;
                font-size: 14px;
                font-weight: 900;
            }

            QLabel#sectionTitle {
                color: #ded7e8;
                font-size: 10px;
                font-weight: 900;
                letter-spacing: 2px;
            }

            QPushButton#dashboardButton {
                background: #100c19;
                color: #9181b0;
                border: 1px solid #29213d;
                border-radius: 12px;
                padding: 14px;
                font-size: 8px;
                font-weight: 900;
            }

            QPushButton#dashboardButton:hover {
                background: #19132a;
                color: #ad99ff;
                border: 1px solid #7255d9;
            }

        """)