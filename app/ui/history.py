from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QFrame,
    QPushButton
)


class HistoryPage(QWidget):

    def __init__(self, history_service=None, parent=None):

        super().__init__(parent)

        self.history_service = history_service

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

        # -----------------------------------------------------
        # HEADER
        # -----------------------------------------------------

        header = QHBoxLayout()

        title = QLabel(
            "Command History"
        )

        title.setObjectName(
            "historyTitle"
        )

        header.addWidget(
            title
        )

        header.addStretch()

        clear_button = QPushButton(
            "CLEAR HISTORY"
        )

        clear_button.setObjectName(
            "clearButton"
        )

        clear_button.clicked.connect(
            self.clear_history
        )

        header.addWidget(
            clear_button
        )

        layout.addLayout(
            header
        )

        subtitle = QLabel(
            "Everything NOVA has executed."
        )

        subtitle.setObjectName(
            "historySubtitle"
        )

        layout.addWidget(
            subtitle
        )

        # -----------------------------------------------------
        # HISTORY LIST
        # -----------------------------------------------------

        self.list_container = QVBoxLayout()

        layout.addLayout(
            self.list_container
        )

        layout.addStretch()

        self.refresh()

        self.setStyleSheet("""

            QLabel#historyTitle {
                color: white;
                font-size: 30px;
                font-weight: 900;
            }

            QLabel#historySubtitle {
                color: #716879;
                font-size: 11px;
            }

            QFrame#historyItem {
                background: #0d0a14;
                border: 1px solid #251d37;
                border-radius: 14px;
            }

            QLabel#historyCommand {
                color: #dcd5e6;
                font-size: 10px;
                font-weight: 800;
            }

            QLabel#historyResponse {
                color: #746b80;
                font-size: 8px;
            }

            QLabel#historyTime {
                color: #625875;
                font-size: 7px;
            }

            QPushButton#clearButton {
                background: #120d1b;
                color: #8068c4;
                border: 1px solid #30234a;
                border-radius: 9px;
                padding: 9px 13px;
                font-size: 7px;
                font-weight: 900;
            }

            QPushButton#clearButton:hover {
                background: #1d142d;
                border: 1px solid #7658d8;
            }

        """)

    # =========================================================
    # REFRESH
    # =========================================================

    def refresh(self):

        while self.list_container.count():

            item = self.list_container.takeAt(0)

            widget = item.widget()

            if widget:

                widget.deleteLater()

        if not self.history_service:

            return

        history = self.history_service.get_all()

        if not history:

            empty = QLabel(
                "No commands yet.\nNOVA's activity will appear here."
            )

            empty.setStyleSheet(
                "color:#5e5668; font-size:10px;"
            )

            self.list_container.addWidget(
                empty
            )

            return

        for item in history:

            frame = QFrame()

            frame.setObjectName(
                "historyItem"
            )

            row = QHBoxLayout(
                frame
            )

            row.setContentsMargins(
                15,
                12,
                15,
                12
            )

            text = QVBoxLayout()

            command = QLabel(
                item["command"]
            )

            command.setObjectName(
                "historyCommand"
            )

            text.addWidget(
                command
            )

            response = QLabel(
                item["response"]
            )

            response.setObjectName(
                "historyResponse"
            )

            text.addWidget(
                response
            )

            row.addLayout(
                text
            )

            row.addStretch()

            time = QLabel(
                item["time"].strftime(
                    "%I:%M %p"
                )
            )

            time.setObjectName(
                "historyTime"
            )

            row.addWidget(
                time
            )

            self.list_container.addWidget(
                frame
            )

    # =========================================================
    # CLEAR
    # =========================================================

    def clear_history(self):

        if self.history_service:

            self.history_service.clear()

            self.refresh()