from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QGridLayout,
    QLabel,
    QPushButton,
    QFrame
)


class AppsPage(QWidget):

    def __init__(
        self,
        execute_command=None,
        parent=None
    ):

        super().__init__(parent)

        self.execute_command_callback = execute_command

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

        layout.setSpacing(15)

        # =====================================================
        # HEADER
        # =====================================================

        title = QLabel(
            "Applications"
        )

        title.setObjectName(
            "appsTitle"
        )

        layout.addWidget(title)

        subtitle = QLabel(
            "Control your favorite desktop applications with NOVA."
        )

        subtitle.setObjectName(
            "appsSubtitle"
        )

        layout.addWidget(subtitle)

        # =====================================================
        # APPLICATION GRID
        # =====================================================

        grid = QGridLayout()

        grid.setSpacing(15)

        applications = [

            (
                "VS CODE",
                "Code editor",
                "open vs code"
            ),

            (
                "CHROME",
                "Web browser",
                "open chrome"
            ),

            (
                "TERMINAL",
                "Command line",
                "open terminal"
            ),

            (
                "NOTEPAD",
                "Text editor",
                "open notepad"
            ),

            (
                "CALCULATOR",
                "Calculator",
                "open calculator"
            ),

            (
                "FILE EXPLORER",
                "Browse files",
                "open file explorer"
            ),

        ]

        for index, (
            name,
            description,
            command
        ) in enumerate(applications):

            card = QFrame()

            card.setObjectName(
                "appCard"
            )

            card_layout = QVBoxLayout(
                card
            )

            card_layout.setContentsMargins(
                18,
                18,
                18,
                18
            )

            # -------------------------------------------------
            # NAME
            # -------------------------------------------------

            app_name = QLabel(
                name
            )

            app_name.setObjectName(
                "appName"
            )

            card_layout.addWidget(
                app_name
            )

            # -------------------------------------------------
            # DESCRIPTION
            # -------------------------------------------------

            desc = QLabel(
                description
            )

            desc.setObjectName(
                "appDescription"
            )

            card_layout.addWidget(
                desc
            )

            card_layout.addSpacing(
                10
            )

            # -------------------------------------------------
            # OPEN BUTTON
            # -------------------------------------------------

            open_button = QPushButton(
                "OPEN"
            )

            open_button.setObjectName(
                "appButton"
            )

            open_button.setFixedHeight(
                38
            )

            open_button.clicked.connect(
                lambda checked=False, cmd=command:
                self.run_command(cmd)
            )

            card_layout.addWidget(
                open_button
            )

            # -------------------------------------------------
            # CLOSE BUTTON
            # -------------------------------------------------

            close_command = command.replace(
                "open ",
                "close "
            )

            close_button = QPushButton(
                "CLOSE"
            )

            close_button.setObjectName(
                "closeAppButton"
            )

            close_button.setFixedHeight(
                34
            )

            close_button.clicked.connect(
                lambda checked=False, cmd=close_command:
                self.run_command(cmd)
            )

            card_layout.addWidget(
                close_button
            )

            # -------------------------------------------------
            # GRID POSITION
            # -------------------------------------------------

            row = index // 3

            column = index % 3

            grid.addWidget(
                card,
                row,
                column
            )

        layout.addLayout(
            grid
        )

        layout.addStretch()

        # =====================================================
        # STYLE
        # =====================================================

        self.setStyleSheet("""

            QLabel#appsTitle {
                color: #F8FAFC;
                font-size: 30px;
                font-weight: 900;
            }

            QLabel#appsSubtitle {
                color: #94A3B8;
                font-size: 13px;
            }

            QFrame#appCard {
                background: #0D0A14;
                border: 1px solid #251D37;
                border-radius: 16px;
            }

            QFrame#appCard:hover {
                border: 1px solid #6249B9;
                background: #110D1B;
            }

            QLabel#appName {
                color: #DDD6E7;
                font-size: 13px;
                font-weight: 900;
                letter-spacing: 1px;
            }

            QLabel#appDescription {
                color: #756D80;
                font-size: 11px;
            }

            QPushButton#appButton {
                background: #7C3AED;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 8px;
                font-size: 11px;
                font-weight: 900;
            }

            QPushButton#appButton:hover {
                background: #8B5CF6;
            }

            QPushButton#closeAppButton {
                background: #120E1C;
                color: #9B8BB8;
                border: 1px solid #30244A;
                border-radius: 8px;
                padding: 7px;
                font-size: 10px;
                font-weight: 900;
            }

            QPushButton#closeAppButton:hover {
                background: #1C1530;
                color: #C4B5FD;
                border: 1px solid #7356D9;
            }

        """)

    # =========================================================
    # RUN COMMAND
    # =========================================================

    def run_command(
        self,
        command
    ):

        print(
            f"NOVA APPS: Running command = {command}"
        )

        if self.execute_command_callback:

            response = self.execute_command_callback(
                command
            )

            print(
                f"NOVA APPS: Response = {response}"
            )