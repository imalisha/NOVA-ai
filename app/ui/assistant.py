from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QFrame
)

from PySide6.QtCore import Qt


class AssistantPage(QWidget):

    def __init__(
        self,
        start_listening=None,
        execute_command=None,
        parent=None
    ):

        super().__init__(parent)

        self.start_listening_callback = start_listening
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

        title = QLabel("NOVA Assistant")
        title.setObjectName("assistantTitle")

        layout.addWidget(title)

        subtitle = QLabel(
            "Talk to NOVA or give it a command."
        )

        subtitle.setObjectName(
            "assistantSubtitle"
        )

        layout.addWidget(subtitle)

        # =====================================================
        # CONVERSATION
        # =====================================================

        conversation = QFrame()

        conversation.setObjectName(
            "conversation"
        )

        conversation_layout = QVBoxLayout(
            conversation
        )

        conversation_layout.setContentsMargins(
            20,
            20,
            20,
            20
        )

        # YOU

        self.you_message = QLabel(
            "YOU\nWaiting for your command..."
        )

        self.you_message.setObjectName(
            "userMessage"
        )

        self.you_message.setWordWrap(True)

        conversation_layout.addWidget(
            self.you_message
        )

        # NOVA

        self.nova_message = QLabel(
            "NOVA\nI'm ready. What would you like me to do?"
        )

        self.nova_message.setObjectName(
            "novaMessage"
        )

        self.nova_message.setWordWrap(True)

        conversation_layout.addWidget(
            self.nova_message
        )

        conversation_layout.addStretch()

        layout.addWidget(
            conversation,
            1
        )

        # =====================================================
        # INPUT
        # =====================================================

        input_row = QHBoxLayout()

        # TEXT INPUT

        self.input_box = QLineEdit()

        self.input_box.setPlaceholderText(
            "Type a command..."
        )

        self.input_box.setObjectName(
            "commandInput"
        )

        input_row.addWidget(
            self.input_box
        )

        # =====================================================
        # MICROPHONE
        # =====================================================

        self.mic = QPushButton("🎙")

        self.mic.setObjectName(
            "assistantMic"
        )

        self.mic.setFixedSize(
            52,
            52
        )

        self.mic.clicked.connect(
            self.on_mic_clicked
        )

        input_row.addWidget(
            self.mic
        )

        # =====================================================
        # SEND
        # =====================================================

        self.send = QPushButton("SEND")

        self.send.setObjectName(
            "sendButton"
        )

        self.send.setFixedHeight(
            52
        )

        self.send.clicked.connect(
            self.send_command
        )

        input_row.addWidget(
            self.send
        )

        self.input_box.returnPressed.connect(
            self.send_command
        )

        layout.addLayout(
            input_row
        )

        # =====================================================
        # STYLE
        # =====================================================

        self.setStyleSheet("""

            QLabel#assistantTitle {
                color: #F8FAFC;
                font-size: 30px;
                font-weight: 900;
            }

            QLabel#assistantSubtitle {
                color: #CBD5E1;
                font-size: 14px;
            }

            QFrame#conversation {
                background: #1E293B;
                border: 1px solid #334155;
                border-radius: 20px;
            }

            QLabel#userMessage {
                background: #263550;
                color: #F8FAFC;
                border: 1px solid #475569;
                border-radius: 13px;
                padding: 15px;
                font-size: 15px;
            }

            QLabel#novaMessage {
                background: #172033;
                color: #E2E8F0;
                border: 1px solid #334155;
                border-radius: 13px;
                padding: 15px;
                font-size: 15px;
            }

            QLineEdit#commandInput {
                background: #1E293B;
                color: #F8FAFC;
                border: 1px solid #475569;
                border-radius: 12px;
                padding: 14px;
                font-size: 15px;
            }

            QLineEdit#commandInput:focus {
                border: 1px solid #8B5CF6;
            }

            QPushButton#assistantMic {
                background: #263550;
                color: #C4B5FD;
                border: 1px solid #8B5CF6;
                border-radius: 12px;
                font-size: 22px;
            }

            QPushButton#assistantMic:hover {
                background: #334155;
                color: #A78BFA;
            }

            QPushButton#assistantMic:disabled {
                background: #172033;
                color: #64748B;
                border: 1px solid #475569;
            }

            QPushButton#sendButton {
                background: #7C3AED;
                color: white;
                border: none;
                border-radius: 12px;
                padding: 0 20px;
                font-size: 14px;
                font-weight: 900;
            }

            QPushButton#sendButton:hover {
                background: #8B5CF6;
            }

            QPushButton#sendButton:disabled {
                background: #475569;
                color: #94A3B8;
            }

        """)

    # =========================================================
    # MICROPHONE CLICK
    # =========================================================

    def on_mic_clicked(self):

        print("NOVA UI: Microphone button clicked")

        self.mic.setText("⏳")
        self.mic.setEnabled(False)

        self.send.setEnabled(False)

        self.nova_message.setText(
            "NOVA\nListening... Speak now."
        )

        if self.start_listening_callback:

            self.start_listening_callback()

    # =========================================================
    # VOICE RESULT
    # =========================================================

    def voice_result(
        self,
        command,
        response
    ):

        self.mic.setText("🎙")
        self.mic.setEnabled(True)

        self.send.setEnabled(True)

        if command:

            self.you_message.setText(
                f"YOU\n{command}"
            )

            self.nova_message.setText(
                f"NOVA\n{response}"
            )

        else:

            self.nova_message.setText(
                "NOVA\nI couldn't understand that. Please try again."
            )

    # =========================================================
    # SEND TEXT COMMAND
    # =========================================================

    def send_command(self):

        command = self.input_box.text().strip()

        if not command:
            return

        self.you_message.setText(
            f"YOU\n{command}"
        )

        if self.execute_command_callback:

            response = self.execute_command_callback(
                command
            )

            self.nova_message.setText(
                f"NOVA\n{response}"
            )

        self.input_box.clear()