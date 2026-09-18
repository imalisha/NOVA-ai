from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QFrame
)


class Sidebar(QWidget):

    def __init__(
        self,
        page_changed=None,
        parent=None
    ):

        super().__init__(parent)

        self.page_changed = page_changed

        self.setup_ui()

    # =========================================================
    # UI
    # =========================================================

    def setup_ui(self):

        self.setFixedWidth(
            235
        )

        layout = QVBoxLayout(self)

        layout.setContentsMargins(
            18,
            22,
            18,
            18
        )

        layout.setSpacing(
            8
        )

        # -----------------------------------------------------
        # LOGO
        # -----------------------------------------------------

        logo = QLabel(
            "✦  NOVA"
        )

        logo.setObjectName(
            "sidebarLogo"
        )

        layout.addWidget(
            logo
        )

        version = QLabel(
            "PERSONAL AI SYSTEM  •  BUILD 01"
        )

        version.setObjectName(
            "sidebarVersion"
        )

        layout.addWidget(
            version
        )

        layout.addSpacing(
            25
        )

        # -----------------------------------------------------
        # NAVIGATION
        # -----------------------------------------------------

        self.dashboard_button = self.nav_button(
            "⌂   DASHBOARD",
            "dashboard"
        )

        self.assistant_button = self.nav_button(
            "◉   ASSISTANT",
            "assistant"
        )

        self.apps_button = self.nav_button(
            "▣   APPLICATIONS",
            "apps"
        )

        self.history_button = self.nav_button(
            "◷   HISTORY",
            "history"
        )

        layout.addWidget(
            self.dashboard_button
        )

        layout.addWidget(
            self.assistant_button
        )

        layout.addWidget(
            self.apps_button
        )

        layout.addWidget(
            self.history_button
        )

        layout.addSpacing(
            20
        )

        line = QFrame()

        line.setFrameShape(
            QFrame.Shape.HLine
        )

        line.setStyleSheet(
            "color:#211a30;"
        )

        layout.addWidget(
            line
        )

        layout.addSpacing(
            10
        )

        self.settings_button = self.nav_button(
            "⚙   SETTINGS",
            "settings"
        )

        layout.addWidget(
            self.settings_button
        )

        layout.addStretch()

        # -----------------------------------------------------
        # STATUS
        # -----------------------------------------------------

        status = QFrame()

        status.setObjectName(
            "sidebarStatus"
        )

        status_layout = QVBoxLayout(
            status
        )

        status_layout.setContentsMargins(
            13,
            12,
            13,
            12
        )

        status_title = QLabel(
            "NOVA CORE"
        )

        status_title.setObjectName(
            "sidebarStatusTitle"
        )

        status_layout.addWidget(
            status_title
        )

        status_value = QLabel(
            "● SYSTEM ONLINE"
        )

        status_value.setObjectName(
            "sidebarStatusValue"
        )

        status_layout.addWidget(
            status_value
        )

        layout.addWidget(
            status
        )

        # -----------------------------------------------------
        # STYLE
        # -----------------------------------------------------

        self.setStyleSheet("""

            QWidget {
                background: #09070e;
            }

            QLabel#sidebarLogo {
                color: white;
                font-size: 23px;
                font-weight: 900;
                letter-spacing: 3px;
            }

            QLabel#sidebarVersion {
                color: #4e4759;
                font-size: 6px;
                font-weight: 800;
                letter-spacing: 1px;
            }

            QPushButton#navButton {
                background: transparent;
                color: #6d6577;
                border: 1px solid transparent;
                border-radius: 10px;
                padding: 12px;
                text-align: left;
                font-size: 8px;
                font-weight: 900;
                letter-spacing: 1px;
            }

            QPushButton#navButton:hover {
                background: #130e1e;
                color: #a38df0;
                border: 1px solid #251c3b;
            }

            QFrame#sidebarStatus {
                background: #0e0a16;
                border: 1px solid #241b36;
                border-radius: 12px;
            }

            QLabel#sidebarStatusTitle {
                color: #4e475a;
                font-size: 6px;
                font-weight: 900;
                letter-spacing: 1px;
            }

            QLabel#sidebarStatusValue {
                color: #9078e4;
                font-size: 7px;
                font-weight: 900;
            }

        """)

    # =========================================================
    # NAV BUTTON
    # =========================================================

    def nav_button(
        self,
        text,
        page
    ):

        button = QPushButton(
            text
        )

        button.setObjectName(
            "navButton"
        )

        button.setFixedHeight(
            43
        )

        if self.page_changed:

            button.clicked.connect(
                lambda: self.page_changed(page)
            )

        return button