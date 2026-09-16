import sys
from datetime import datetime

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QScrollArea,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QLabel,
    QPushButton,
    QFrame,
    QGraphicsDropShadowEffect,
)
from PySide6.QtCore import (
    Qt,
    QThread,
    Signal,
    QTimer,
)
from PySide6.QtGui import QColor

from app.services.speech import SpeechService
from app.ui.ai_core import AICore
from app.commands.executor import CommandExecutor


# ============================================================
# VOICE WORKER
# ============================================================

class VoiceWorker(QThread):

    finished = Signal(object)

    def __init__(self):
        super().__init__()

        self.speech = SpeechService()
        self.executor = CommandExecutor()

    def run(self):

        command = self.speech.listen()

        if command:

            response = self.executor.execute(command)

            self.finished.emit(
                (command, response)
            )

        else:

            self.finished.emit(
                (None, "I couldn't understand that.")
            )


# ============================================================
# NOVA WINDOW
# ============================================================

class NovaWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("NOVA AI")

        self.resize(
            1450,
            920
        )

        self.setMinimumSize(
            900,
            650
        )

        self.voice_worker = None

        self.executor = CommandExecutor()

        self.setup_ui()

        self.start_clock()

    # ========================================================
    # SHADOW
    # ========================================================

    def add_shadow(
        self,
        widget,
        blur=35,
        alpha=130
    ):

        shadow = QGraphicsDropShadowEffect()

        shadow.setBlurRadius(
            blur
        )

        shadow.setOffset(
            0,
            8
        )

        shadow.setColor(
            QColor(
                0,
                0,
                0,
                alpha
            )
        )

        widget.setGraphicsEffect(
            shadow
        )

    # ========================================================
    # CLOCK
    # ========================================================

    def start_clock(self):

        self.clock_timer = QTimer(
            self
        )

        self.clock_timer.timeout.connect(
            self.update_clock
        )

        self.clock_timer.start(
            1000
        )

        self.update_clock()

    def update_clock(self):

        now = datetime.now()

        self.time_label.setText(
            now.strftime("%I:%M %p")
        )

        self.date_label.setText(
            now.strftime("%A  •  %d %B %Y")
        )

    # ========================================================
    # MAIN UI
    # ========================================================

    def setup_ui(self):

        # ====================================================
        # SCROLL AREA
        # ====================================================

        scroll = QScrollArea()

        scroll.setWidgetResizable(
            True
        )

        scroll.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )

        scroll.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAsNeeded
        )

        scroll.setFrameShape(
            QFrame.Shape.NoFrame
        )

        self.setCentralWidget(
            scroll
        )

        # ====================================================
        # SCROLL CONTENT
        # ====================================================

        central = QWidget()

        central.setObjectName(
            "central"
        )

        # Prevent the dashboard from becoming
        # too narrow on small windows.

        central.setMinimumWidth(
            900
        )

        scroll.setWidget(
            central
        )

        root = QVBoxLayout(
            central
        )

        root.setContentsMargins(
            30,
            24,
            30,
            18
        )

        root.setSpacing(
            0
        )

        # ====================================================
        # TOP BAR
        # ====================================================

        header = QHBoxLayout()

        header.setSpacing(
            10
        )

        # ----------------------------------------------------
        # BRAND
        # ----------------------------------------------------

        brand_icon = QLabel(
            "✦"
        )

        brand_icon.setObjectName(
            "brandIcon"
        )

        header.addWidget(
            brand_icon
        )

        brand = QLabel(
            "NOVA"
        )

        brand.setObjectName(
            "brand"
        )

        header.addWidget(
            brand
        )

        brand_ai = QLabel(
            "AI"
        )

        brand_ai.setObjectName(
            "brandAI"
        )

        header.addWidget(
            brand_ai
        )

        header.addSpacing(
            20
        )

        command_center = QLabel(
            "COMMAND CENTER"
        )

        command_center.setObjectName(
            "commandCenter"
        )

        header.addWidget(
            command_center
        )

        header.addStretch()

        # ----------------------------------------------------
        # TIME
        # ----------------------------------------------------

        time_box = QFrame()

        time_box.setObjectName(
            "timeBox"
        )

        time_layout = QVBoxLayout(
            time_box
        )

        time_layout.setContentsMargins(
            14,
            7,
            14,
            7
        )

        time_layout.setSpacing(
            1
        )

        self.time_label = QLabel(
            "--:--"
        )

        self.time_label.setObjectName(
            "timeLabel"
        )

        self.time_label.setAlignment(
            Qt.AlignmentFlag.AlignRight
        )

        time_layout.addWidget(
            self.time_label
        )

        self.date_label = QLabel(
            "Loading..."
        )

        self.date_label.setObjectName(
            "dateLabel"
        )

        self.date_label.setAlignment(
            Qt.AlignmentFlag.AlignRight
        )

        time_layout.addWidget(
            self.date_label
        )

        header.addWidget(
            time_box
        )

        # ----------------------------------------------------
        # LANGUAGE
        # ----------------------------------------------------

        language = QFrame()

        language.setObjectName(
            "topPill"
        )

        language_layout = QHBoxLayout(
            language
        )

        language_layout.setContentsMargins(
            13,
            8,
            13,
            8
        )

        language_label = QLabel(
            "EN  •  اردو  •  ਪੰਜਾਬੀ"
        )

        language_label.setObjectName(
            "pillText"
        )

        language_layout.addWidget(
            language_label
        )

        header.addWidget(
            language
        )

        # ----------------------------------------------------
        # ONLINE
        # ----------------------------------------------------

        online = QFrame()

        online.setObjectName(
            "onlinePill"
        )

        online_layout = QHBoxLayout(
            online
        )

        online_layout.setContentsMargins(
            13,
            8,
            13,
            8
        )

        online_label = QLabel(
            "●  ONLINE"
        )

        online_label.setObjectName(
            "onlineText"
        )

        online_layout.addWidget(
            online_label
        )

        header.addWidget(
            online
        )

        # ----------------------------------------------------
        # SETTINGS
        # ----------------------------------------------------

        settings = QPushButton(
            "⚙"
        )

        settings.setObjectName(
            "settings"
        )

        settings.setFixedSize(
            43,
            43
        )

        header.addWidget(
            settings
        )

        root.addLayout(
            header
        )

        root.addSpacing(
            24
        )

        # ====================================================
        # MAIN AREA
        # ====================================================

        main_grid = QGridLayout()

        main_grid.setHorizontalSpacing(
            18
        )

        main_grid.setVerticalSpacing(
            18
        )

        # ====================================================
        # HERO PANEL
        # ====================================================

        hero = QFrame()

        hero.setObjectName(
            "hero"
        )

        hero_layout = QVBoxLayout(
            hero
        )

        hero_layout.setContentsMargins(
            30,
            26,
            30,
            24
        )

        hero_layout.setSpacing(
            0
        )

        # ----------------------------------------------------
        # HERO TAG
        # ----------------------------------------------------

        tag = QLabel(
            "PERSONAL DESKTOP INTELLIGENCE"
        )

        tag.setObjectName(
            "heroTag"
        )

        tag.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        hero_layout.addWidget(
            tag
        )

        hero_layout.addSpacing(
            8
        )

        # ----------------------------------------------------
        # TITLE
        # ----------------------------------------------------

        title = QLabel(
            "Good Evening"
        )

        title.setObjectName(
            "heroTitle"
        )

        title.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        hero_layout.addWidget(
            title
        )

        subtitle = QLabel(
            "Your computer is listening."
        )

        subtitle.setObjectName(
            "heroSubtitle"
        )

        subtitle.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        hero_layout.addWidget(
            subtitle
        )

        hero_layout.addSpacing(
            14
        )

        # ----------------------------------------------------
        # AI CORE
        # ----------------------------------------------------

        core_container = QFrame()

        core_container.setObjectName(
            "coreContainer"
        )

        core_layout = QVBoxLayout(
            core_container
        )

        core_layout.setContentsMargins(
            0,
            0,
            0,
            0
        )

        self.ai_core = AICore()

        core_layout.addWidget(
            self.ai_core,
            alignment=Qt.AlignmentFlag.AlignCenter
        )

        hero_layout.addWidget(
            core_container
        )

        hero_layout.addSpacing(
            2
        )

        # ----------------------------------------------------
        # NOVA NAME
        # ----------------------------------------------------

        nova_name = QLabel(
            "N  O  V  A"
        )

        nova_name.setObjectName(
            "novaName"
        )

        nova_name.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        hero_layout.addWidget(
            nova_name
        )

        description = QLabel(
            "VOICE  •  INTELLIGENCE  •  AUTOMATION"
        )

        description.setObjectName(
            "coreDescription"
        )

        description.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        hero_layout.addWidget(
            description
        )

        hero_layout.addSpacing(
            15
        )

        # ----------------------------------------------------
        # STATUS
        # ----------------------------------------------------

        self.status = QLabel(
            "●  READY"
        )

        self.status.setObjectName(
            "status"
        )

        self.status.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        hero_layout.addWidget(
            self.status
        )

        hero_layout.addSpacing(
            10
        )

        # ----------------------------------------------------
        # MICROPHONE
        # ----------------------------------------------------

        self.microphone = QPushButton(
            "🎙"
        )

        self.microphone.setObjectName(
            "microphone"
        )

        self.microphone.setFixedSize(
            70,
            70
        )

        self.microphone.clicked.connect(
            self.start_listening
        )

        hero_layout.addWidget(
            self.microphone,
            alignment=Qt.AlignmentFlag.AlignCenter
        )

        hero_layout.addSpacing(
            6
        )

        hint = QLabel(
            "Click to speak"
        )

        hint.setObjectName(
            "hint"
        )

        hint.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        hero_layout.addWidget(
            hint
        )

        hero_layout.addSpacing(
            15
        )

        # ----------------------------------------------------
        # QUICK COMMANDS
        # ----------------------------------------------------

        quick_title = QLabel(
            "QUICK COMMANDS"
        )

        quick_title.setObjectName(
            "quickTitle"
        )

        quick_title.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        hero_layout.addWidget(
            quick_title
        )

        hero_layout.addSpacing(
            7
        )

        quick_row = QHBoxLayout()

        quick_row.setSpacing(
            7
        )

        open_button = QPushButton(
            "OPEN VS CODE"
        )

        open_button.setObjectName(
            "quickButton"
        )

        open_button.clicked.connect(
            lambda: self.execute_quick_command(
                "open vs code"
            )
        )

        quick_row.addWidget(
            open_button
        )

        close_button = QPushButton(
            "CLOSE VS CODE"
        )

        close_button.setObjectName(
            "quickButton"
        )

        close_button.clicked.connect(
            lambda: self.execute_quick_command(
                "close vs code"
            )
        )

        quick_row.addWidget(
            close_button
        )

        hero_layout.addLayout(
            quick_row
        )

        main_grid.addWidget(
            hero,
            0,
            0,
            2,
            1
        )

        self.add_shadow(
            hero,
            45,
            150
        )

        # ====================================================
        # RIGHT SIDE GRID
        # ====================================================

        right_grid = QGridLayout()

        right_grid.setVerticalSpacing(
            18
        )

        # ====================================================
        # CONVERSATION
        # ====================================================

        conversation = QFrame()

        conversation.setObjectName(
            "panel"
        )

        conversation_layout = QVBoxLayout(
            conversation
        )

        conversation_layout.setContentsMargins(
            22,
            20,
            22,
            20
        )

        header_row = QHBoxLayout()

        conversation_title = QLabel(
            "CONVERSATION"
        )

        conversation_title.setObjectName(
            "panelTitle"
        )

        header_row.addWidget(
            conversation_title
        )

        header_row.addStretch()

        live = QLabel(
            "● LIVE"
        )

        live.setObjectName(
            "liveBadge"
        )

        header_row.addWidget(
            live
        )

        conversation_layout.addLayout(
            header_row
        )

        conversation_subtitle = QLabel(
            "Your latest interaction"
        )

        conversation_subtitle.setObjectName(
            "panelSubtitle"
        )

        conversation_layout.addWidget(
            conversation_subtitle
        )

        conversation_layout.addSpacing(
            13
        )

        you_label = QLabel(
            "YOU"
        )

        you_label.setObjectName(
            "messageLabel"
        )

        conversation_layout.addWidget(
            you_label
        )

        self.you_message = QLabel(
            "Waiting for your command..."
        )

        self.you_message.setObjectName(
            "userBubble"
        )

        self.you_message.setWordWrap(
            True
        )

        conversation_layout.addWidget(
            self.you_message
        )

        conversation_layout.addSpacing(
            10
        )

        nova_label = QLabel(
            "NOVA"
        )

        nova_label.setObjectName(
            "messageLabel"
        )

        conversation_layout.addWidget(
            nova_label
        )

        self.nova_message = QLabel(
            "I'm ready when you are."
        )

        self.nova_message.setObjectName(
            "novaBubble"
        )

        self.nova_message.setWordWrap(
            True
        )

        conversation_layout.addWidget(
            self.nova_message
        )

        right_grid.addWidget(
            conversation,
            0,
            0
        )

        self.add_shadow(
            conversation
        )

        # ====================================================
        # SYSTEM MONITOR
        # ====================================================

        system = QFrame()

        system.setObjectName(
            "panel"
        )

        system_layout = QVBoxLayout(
            system
        )

        system_layout.setContentsMargins(
            22,
            20,
            22,
            20
        )

        system_title = QLabel(
            "SYSTEM MONITOR"
        )

        system_title.setObjectName(
            "panelTitle"
        )

        system_layout.addWidget(
            system_title
        )

        system_subtitle = QLabel(
            "NOVA environment status"
        )

        system_subtitle.setObjectName(
            "panelSubtitle"
        )

        system_layout.addWidget(
            system_subtitle
        )

        system_layout.addSpacing(
            12
        )

        monitor_grid = QGridLayout()

        monitor_grid.setHorizontalSpacing(
            10
        )

        monitor_grid.setVerticalSpacing(
            10
        )

        monitor_grid.addWidget(
            self.status_box(
                "PROCESSOR",
                "READY",
                "CPU"
            ),
            0,
            0
        )

        monitor_grid.addWidget(
            self.status_box(
                "MEMORY",
                "READY",
                "RAM"
            ),
            0,
            1
        )

        monitor_grid.addWidget(
            self.status_box(
                "MICROPHONE",
                "READY",
                "MIC"
            ),
            1,
            0
        )

        monitor_grid.addWidget(
            self.status_box(
                "NETWORK",
                "ONLINE",
                "NET"
            ),
            1,
            1
        )

        system_layout.addLayout(
            monitor_grid
        )

        right_grid.addWidget(
            system,
            1,
            0
        )

        self.add_shadow(
            system
        )

        main_grid.addLayout(
            right_grid,
            0,
            1,
            2,
            1
        )

        main_grid.setColumnStretch(
            0,
            4
        )

        main_grid.setColumnStretch(
            1,
            6
        )

        root.addLayout(
            main_grid,
            1
        )

        root.addSpacing(
            18
        )

        # ====================================================
        # NOVA INTELLIGENCE
        # ====================================================

        intelligence_header = QHBoxLayout()

        intelligence_title = QLabel(
            "NOVA INTELLIGENCE"
        )

        intelligence_title.setObjectName(
            "sectionTitle"
        )

        intelligence_header.addWidget(
            intelligence_title
        )

        intelligence_header.addStretch()

        intelligence_status = QLabel(
            "● MODULES ACTIVE"
        )

        intelligence_status.setObjectName(
            "sectionStatus"
        )

        intelligence_header.addWidget(
            intelligence_status
        )

        root.addLayout(
            intelligence_header
        )

        root.addSpacing(
            9
        )

        intelligence_row = QHBoxLayout()

        intelligence_row.setSpacing(
            10
        )

        intelligence_row.addWidget(
            self.capability_card(
                "MIC",
                "VOICE CONTROL",
                "Speech interaction"
            )
        )

        intelligence_row.addWidget(
            self.capability_card(
                "LANG",
                "MULTILINGUAL",
                "English • Urdu • Punjabi"
            )
        )

        intelligence_row.addWidget(
            self.capability_card(
                "PC",
                "PC AUTOMATION",
                "Desktop control"
            )
        )

        intelligence_row.addWidget(
            self.capability_card(
                "AI",
                "AI CORE",
                "Command intelligence"
            )
        )

        root.addLayout(
            intelligence_row
        )

        root.addSpacing(
            14
        )

        # ====================================================
        # RECENT ACTIVITY
        # ====================================================

        activity_header = QHBoxLayout()

        activity_title = QLabel(
            "RECENT ACTIVITY"
        )

        activity_title.setObjectName(
            "sectionTitle"
        )

        activity_header.addWidget(
            activity_title
        )

        activity_header.addStretch()

        activity_build = QLabel(
            "BUILD 01"
        )

        activity_build.setObjectName(
            "sectionStatus"
        )

        activity_header.addWidget(
            activity_build
        )

        root.addLayout(
            activity_header
        )

        root.addSpacing(
            9
        )

        activity_row = QHBoxLayout()

        activity_row.setSpacing(
            10
        )

        activity_row.addWidget(
            self.activity_card(
                "01",
                "COMMAND",
                "VS Code opened"
            )
        )

        activity_row.addWidget(
            self.activity_card(
                "02",
                "COMMAND",
                "VS Code closed"
            )
        )

        activity_row.addWidget(
            self.activity_card(
                "03",
                "LANGUAGE",
                "Multilingual ready"
            )
        )

        activity_row.addWidget(
            self.activity_card(
                "04",
                "SYSTEM",
                "NOVA initialized"
            )
        )

        root.addLayout(
            activity_row
        )

        root.addSpacing(
            12
        )

        # ====================================================
        # FOOTER
        # ====================================================

        footer = QHBoxLayout()

        footer_left = QLabel(
            "✦  NOVA AI  •  INTELLIGENT DESKTOP ASSISTANT"
        )

        footer_left.setObjectName(
            "footer"
        )

        footer.addWidget(
            footer_left
        )

        footer.addStretch()

        footer_right = QLabel(
            "PYTHON  •  PYSIDE6  •  VOICE AUTOMATION"
        )

        footer_right.setObjectName(
            "footer"
        )

        footer.addWidget(
            footer_right
        )

        root.addLayout(
            footer
        )

        # ====================================================
        # STYLE SHEET
        # ====================================================

        self.setStyleSheet("""

        /* ==================================================
           SCROLL AREA
           ================================================== */

        QScrollArea {
            background: #06050a;
            border: none;
        }

        QScrollBar:vertical {
            background: #08070d;
            width: 10px;
            margin: 4px 2px 4px 2px;
            border-radius: 5px;
        }

        QScrollBar::handle:vertical {
            background: #302450;
            min-height: 70px;
            border-radius: 5px;
        }

        QScrollBar::handle:vertical:hover {
            background: #6f52d0;
        }

        QScrollBar::add-line:vertical,
        QScrollBar::sub-line:vertical {
            height: 0px;
        }

        QScrollBar::add-page:vertical,
        QScrollBar::sub-page:vertical {
            background: transparent;
        }

        /* ==================================================
           BASE
           ================================================== */

        QMainWindow {
            background: #06050a;
        }

        QWidget#central {
            background:
                qlineargradient(
                    x1: 0,
                    y1: 0,
                    x2: 1,
                    y2: 1,
                    stop: 0 #06050a,
                    stop: 0.5 #090711,
                    stop: 1 #06050a
                );
        }

        QLabel {
            background: transparent;
        }

        /* ==================================================
           BRAND
           ================================================== */

        QLabel#brandIcon {
            color: #9575ff;
            font-size: 27px;
            font-weight: 900;
        }

        QLabel#brand {
            color: #ffffff;
            font-size: 25px;
            font-weight: 900;
            letter-spacing: 4px;
        }

        QLabel#brandAI {
            color: #8062e7;
            font-size: 11px;
            font-weight: 900;
            letter-spacing: 2px;
            padding-top: 8px;
        }

        QLabel#commandCenter {
            color: #4e475e;
            font-size: 8px;
            font-weight: 900;
            letter-spacing: 2px;
        }

        /* ==================================================
           TIME
           ================================================== */

        QFrame#timeBox {
            background: #0b0911;
            border: 1px solid #1e1930;
            border-radius: 12px;
        }

        QLabel#timeLabel {
            color: #a08bea;
            font-size: 10px;
            font-weight: 900;
        }

        QLabel#dateLabel {
            color: #4d4658;
            font-size: 6px;
            font-weight: 700;
        }

        /* ==================================================
           TOP PILLS
           ================================================== */

        QFrame#topPill {
            background: #0c0a12;
            border: 1px solid #211c32;
            border-radius: 13px;
        }

        QLabel#pillText {
            color: #71697d;
            font-size: 8px;
            font-weight: 800;
        }

        QFrame#onlinePill {
            background: #0e0b16;
            border: 1px solid #2c2344;
            border-radius: 13px;
        }

        QLabel#onlineText {
            color: #9880ee;
            font-size: 8px;
            font-weight: 900;
            letter-spacing: 1px;
        }

        QPushButton#settings {
            background: #0d0a13;
            color: #9582d9;
            border: 1px solid #27203a;
            border-radius: 13px;
            font-size: 17px;
        }

        QPushButton#settings:hover {
            background: #18122a;
            border: 1px solid #7253dc;
        }

        /* ==================================================
           HERO
           ================================================== */

        QFrame#hero {
            background:
                qlineargradient(
                    x1: 0,
                    y1: 0,
                    x2: 1,
                    y2: 1,
                    stop: 0 #0d0a14,
                    stop: 0.5 #0b0912,
                    stop: 1 #100b19
                );

            border: 1px solid #261e3a;
            border-radius: 26px;
        }

        QLabel#heroTag {
            color: #6c58a3;
            font-size: 7px;
            font-weight: 900;
            letter-spacing: 2px;
        }

        QLabel#heroTitle {
            color: #ffffff;
            font-size: 29px;
            font-weight: 900;
        }

        QLabel#heroSubtitle {
            color: #6d6578;
            font-size: 10px;
        }

        QFrame#coreContainer {
            background: transparent;
            border: none;
        }

        QLabel#novaName {
            color: #ffffff;
            font-size: 19px;
            font-weight: 900;
            letter-spacing: 8px;
        }

        QLabel#coreDescription {
            color: #554d62;
            font-size: 7px;
            font-weight: 900;
            letter-spacing: 2px;
        }

        QLabel#status {
            color: #9b82f4;
            font-size: 9px;
            font-weight: 900;
            letter-spacing: 2px;
        }

        QPushButton#microphone {
            background:
                qradialgradient(
                    cx: 0.5,
                    cy: 0.5,
                    radius: 0.7,
                    stop: 0 #1b1432,
                    stop: 1 #0e0a17
                );

            color: #aa94ff;
            border: 2px solid #7354e3;
            border-radius: 35px;
            font-size: 25px;
        }

        QPushButton#microphone:hover {
            background: #201743;
            border: 2px solid #a18aff;
        }

        QPushButton#microphone:pressed {
            background: #2b2050;
        }

        QLabel#hint {
            color: #504957;
            font-size: 8px;
            font-weight: 700;
        }

        QLabel#quickTitle {
            color: #514a5d;
            font-size: 7px;
            font-weight: 900;
            letter-spacing: 1.5px;
        }

        QPushButton#quickButton {
            background: #100d18;
            color: #74659b;
            border: 1px solid #27203a;
            border-radius: 8px;
            padding: 7px 8px;
            font-size: 6px;
            font-weight: 900;
            letter-spacing: 0.5px;
        }

        QPushButton#quickButton:hover {
            background: #18122a;
            color: #a48cff;
            border: 1px solid #6247c5;
        }

        /* ==================================================
           PANELS
           ================================================== */

        QFrame#panel {
            background:
                qlineargradient(
                    x1: 0,
                    y1: 0,
                    x2: 1,
                    y2: 1,
                    stop: 0 #0c0a12,
                    stop: 1 #0a0810
                );

            border: 1px solid #211b31;
            border-radius: 20px;
        }

        QFrame#panel:hover {
            border: 1px solid #30254a;
        }

        QLabel#panelTitle {
            color: #e8e2f2;
            font-size: 10px;
            font-weight: 900;
            letter-spacing: 1.5px;
        }

        QLabel#panelSubtitle {
            color: #575061;
            font-size: 8px;
        }

        QLabel#liveBadge {
            color: #8d75dc;
            background: #151025;
            border: 1px solid #302552;
            border-radius: 7px;
            padding: 4px 8px;
            font-size: 6px;
            font-weight: 900;
            letter-spacing: 1px;
        }

        QLabel#messageLabel {
            color: #514a5e;
            font-size: 7px;
            font-weight: 900;
            letter-spacing: 1.5px;
        }

        QLabel#userBubble {
            background: #151025;
            color: #bcb2cf;
            border: 1px solid #2b2143;
            border-radius: 11px;
            padding: 12px;
            font-size: 9px;
        }

        QLabel#novaBubble {
            background: #0f0c16;
            color: #978ca9;
            border: 1px solid #211b2e;
            border-radius: 11px;
            padding: 12px;
            font-size: 9px;
        }

        /* ==================================================
           STATUS BOXES
           ================================================== */

        QFrame#statusBox {
            background: #0f0c16;
            border: 1px solid #211b30;
            border-radius: 10px;
        }

        QFrame#statusBox:hover {
            background: #13101c;
            border: 1px solid #30254a;
        }

        QLabel#statusIcon {
            color: #8f77e8;
            font-size: 8px;
            font-weight: 900;
        }

        QLabel#statusBoxTitle {
            color: #504958;
            font-size: 6px;
            font-weight: 900;
            letter-spacing: 1px;
        }

        QLabel#statusBoxValue {
            color: #9380e3;
            font-size: 9px;
            font-weight: 900;
        }

        /* ==================================================
           SECTION
           ================================================== */

        QLabel#sectionTitle {
            color: #e3ddec;
            font-size: 9px;
            font-weight: 900;
            letter-spacing: 1.5px;
        }

        QLabel#sectionStatus {
            color: #514a5d;
            font-size: 6px;
            font-weight: 900;
            letter-spacing: 1px;
        }

        /* ==================================================
           INTELLIGENCE
           ================================================== */

        QFrame#capabilityCard {
            background:
                qlineargradient(
                    x1: 0,
                    y1: 0,
                    x2: 1,
                    y2: 0,
                    stop: 0 #0d0a13,
                    stop: 1 #0a0810
                );

            border: 1px solid #201a2d;
            border-radius: 13px;
        }

        QFrame#capabilityCard:hover {
            background: #120e1c;
            border: 1px solid #352950;
        }

        QLabel#capabilityIcon {
            color: #967ce9;
            font-size: 7px;
            font-weight: 900;
        }

        QLabel#capabilityTitle {
            color: #a39ab4;
            font-size: 7px;
            font-weight: 900;
            letter-spacing: 1px;
        }

        QLabel#capabilityDescription {
            color: #514a5b;
            font-size: 6px;
        }

        /* ==================================================
           ACTIVITY
           ================================================== */

        QFrame#activityCard {
            background: #0b0911;
            border: 1px solid #201a2d;
            border-radius: 12px;
        }

        QFrame#activityCard:hover {
            background: #110d19;
            border: 1px solid #30254a;
        }

        QLabel#activityIcon {
            color: #9279e7;
            font-size: 7px;
            font-weight: 900;
        }

        QLabel#activityCategory {
            color: #514a5c;
            font-size: 6px;
            font-weight: 900;
            letter-spacing: 1px;
        }

        QLabel#activityText {
            color: #92889f;
            font-size: 8px;
            font-weight: 700;
        }

        /* ==================================================
           FOOTER
           ================================================== */

        QLabel#footer {
            color: #3e3947;
            font-size: 6px;
            font-weight: 800;
            letter-spacing: 1px;
        }

        """)

    # ========================================================
    # STATUS BOX
    # ========================================================

    def status_box(
        self,
        title,
        value,
        icon
    ):

        frame = QFrame()

        frame.setObjectName(
            "statusBox"
        )

        layout = QHBoxLayout(
            frame
        )

        layout.setContentsMargins(
            10,
            9,
            10,
            9
        )

        layout.setSpacing(
            9
        )

        icon_label = QLabel(
            icon
        )

        icon_label.setObjectName(
            "statusIcon"
        )

        icon_label.setFixedWidth(
            25
        )

        icon_label.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        layout.addWidget(
            icon_label
        )

        text_layout = QVBoxLayout()

        text_layout.setSpacing(
            2
        )

        title_label = QLabel(
            title
        )

        title_label.setObjectName(
            "statusBoxTitle"
        )

        text_layout.addWidget(
            title_label
        )

        value_label = QLabel(
            value
        )

        value_label.setObjectName(
            "statusBoxValue"
        )

        text_layout.addWidget(
            value_label
        )

        layout.addLayout(
            text_layout
        )

        return frame

    # ========================================================
    # CAPABILITY CARD
    # ========================================================

    def capability_card(
        self,
        icon,
        title,
        description
    ):

        frame = QFrame()

        frame.setObjectName(
            "capabilityCard"
        )

        layout = QHBoxLayout(
            frame
        )

        layout.setContentsMargins(
            12,
            10,
            12,
            10
        )

        layout.setSpacing(
            9
        )

        icon_label = QLabel(
            icon
        )

        icon_label.setObjectName(
            "capabilityIcon"
        )

        icon_label.setFixedWidth(
            28
        )

        icon_label.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        layout.addWidget(
            icon_label
        )

        text_layout = QVBoxLayout()

        text_layout.setSpacing(
            2
        )

        title_label = QLabel(
            title
        )

        title_label.setObjectName(
            "capabilityTitle"
        )

        text_layout.addWidget(
            title_label
        )

        description_label = QLabel(
            description
        )

        description_label.setObjectName(
            "capabilityDescription"
        )

        text_layout.addWidget(
            description_label
        )

        layout.addLayout(
            text_layout
        )

        return frame

    # ========================================================
    # ACTIVITY CARD
    # ========================================================

    def activity_card(
        self,
        number,
        category,
        text
    ):

        frame = QFrame()

        frame.setObjectName(
            "activityCard"
        )

        layout = QHBoxLayout(
            frame
        )

        layout.setContentsMargins(
            12,
            9,
            12,
            9
        )

        layout.setSpacing(
            9
        )

        icon = QLabel(
            number
        )

        icon.setObjectName(
            "activityIcon"
        )

        icon.setFixedWidth(
            22
        )

        icon.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        layout.addWidget(
            icon
        )

        text_layout = QVBoxLayout()

        text_layout.setSpacing(
            2
        )

        category_label = QLabel(
            category
        )

        category_label.setObjectName(
            "activityCategory"
        )

        text_layout.addWidget(
            category_label
        )

        text_label = QLabel(
            text
        )

        text_label.setObjectName(
            "activityText"
        )

        text_layout.addWidget(
            text_label
        )

        layout.addLayout(
            text_layout
        )

        return frame

    # ========================================================
    # QUICK COMMAND
    # ========================================================

    def execute_quick_command(
        self,
        command
    ):

        if self.voice_worker is not None:
            return

        response = self.executor.execute(
            command
        )

        self.you_message.setText(
            f'"{command}"'
        )

        self.nova_message.setText(
            response
        )

        self.status.setText(
            "●  COMMAND EXECUTED"
        )

    # ========================================================
    # START LISTENING
    # ========================================================

    def start_listening(self):

        if self.voice_worker is not None:
            return

        self.status.setText(
            "●  LISTENING..."
        )

        self.you_message.setText(
            "Listening for your command..."
        )

        self.nova_message.setText(
            "I'm listening."
        )

        self.microphone.setText(
            "◉"
        )

        self.voice_worker = VoiceWorker()

        self.voice_worker.finished.connect(
            self.voice_finished
        )

        self.voice_worker.start()

    # ========================================================
    # VOICE FINISHED
    # ========================================================

    def voice_finished(
        self,
        result
    ):

        command, response = result

        self.microphone.setText(
            "🎙"
        )

        if command:

            self.status.setText(
                "●  COMMAND EXECUTED"
            )

            self.you_message.setText(
                f'"{command}"'
            )

            self.nova_message.setText(
                response
            )

        else:

            self.status.setText(
                "●  READY"
            )

            self.you_message.setText(
                "I couldn't understand that."
            )

            self.nova_message.setText(
                "Please try again."
            )

        self.voice_worker = None


# ============================================================
# APPLICATION
# ============================================================

def main():

    app = QApplication(
        sys.argv
    )

    app.setApplicationName(
        "NOVA AI"
    )

    app.setStyle(
        "Fusion"
    )

    window = NovaWindow()

    window.show()

    sys.exit(
        app.exec()
    )


# ============================================================
# RUN
# ============================================================

if __name__ == "__main__":
    main()