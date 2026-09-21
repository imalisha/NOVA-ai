import sys
from datetime import datetime

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QStackedWidget,
    QLabel,
    QFrame,
    QPushButton,
    QGraphicsDropShadowEffect,
)

from PySide6.QtCore import (
    Qt,
    QThread,
    Signal,
    QTimer,
)

from PySide6.QtGui import QColor


# ============================================================
# SERVICES
# ============================================================

from app.services.speech import SpeechService
from app.services.history import HistoryService

from app.commands.executor import CommandExecutor

# ============================================================
# UI PAGES
# ============================================================

from app.ui.sidebar import Sidebar
from app.ui.dashboard import Dashboard
from app.ui.assistant import AssistantPage
from app.ui.apps import AppsPage
from app.ui.history import HistoryPage
from app.ui.settings import SettingsPage


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

        print(
            "NOVA HANDS-FREE: Started"
        )

        self.status_changed.emit(
            "WAITING"
        )

        while self.running:

            # ====================================================
            # WAIT FOR WAKE WORD
            # ====================================================

            wake_detected = (
                self.speech.listen_for_wake_word()
            )

            if not self.running:
                break

            if not wake_detected:
                continue

            # ====================================================
            # NOVA ACTIVATED
            # ====================================================

            print(
                "NOVA HANDS-FREE: NOVA activated!"
            )

            self.status_changed.emit(
                "ACTIVATED"
            )

            # Small delay so UI can visibly show activation
            import time
            time.sleep(0.3)

            # ====================================================
            # LISTEN FOR COMMAND
            # ====================================================

            self.status_changed.emit(
                "LISTENING"
            )

            command = self.speech.listen()

            if not self.running:
                break

            if not command:

                self.status_changed.emit(
                    "WAITING"
                )

                continue

            # ====================================================
            # PROCESSING
            # ====================================================

            print(
                f"NOVA HANDS-FREE: Command = {command}"
            )

            self.status_changed.emit(
                "PROCESSING"
            )

            import time
            time.sleep(0.2)

            # ====================================================
            # EXECUTE
            # ====================================================

            self.status_changed.emit(
                "EXECUTING"
            )

            response = self.executor.execute(
                command
            )

            print(
                f"NOVA HANDS-FREE: Response = {response}"
            )

            # ====================================================
            # SEND RESULT
            # ====================================================

            self.command_detected.emit(
                (
                    command,
                    response
                )
            )

            # ====================================================
            # BACK TO WAITING
            # ====================================================

            self.status_changed.emit(
                "WAITING"
            )

        print(
            "NOVA HANDS-FREE: Worker stopped"
        )
# ============================================================
# HANDS-FREE VOICE WORKER
# ============================================================

class HandsFreeWorker(QThread):

    command_detected = Signal(object)

    status_changed = Signal(str)

    def __init__(self):

        super().__init__()

        self.speech = SpeechService()
        self.executor = CommandExecutor()

        self.running = True

    # =========================================================
    # STOP WORKER
    # =========================================================

    def stop(self):

        self.running = False

        print(
            "NOVA HANDS-FREE: Stopping..."
        )

    # =========================================================
    # WORKER LOOP
    # =========================================================

    def run(self):

        print(
            "NOVA HANDS-FREE: Started"
        )

        self.status_changed.emit(
            "WAITING"
        )

        while self.running:

            # -------------------------------------------------
            # WAIT FOR WAKE WORD
            # -------------------------------------------------

            wake_detected = (
                self.speech.listen_for_wake_word()
            )

            if not self.running:

                break

            if not wake_detected:

                continue

            # -------------------------------------------------
            # NOVA AWAKE
            # -------------------------------------------------

            print(
                "NOVA HANDS-FREE: NOVA activated!"
            )

            self.status_changed.emit(
                "LISTENING"
            )

            # -------------------------------------------------
            # LISTEN FOR COMMAND
            # -------------------------------------------------

            command = self.speech.listen()

            if not self.running:

                break

            if not command:

                self.status_changed.emit(
                    "WAITING"
                )

                continue

            print(
                f"NOVA HANDS-FREE: Command = {command}"
            )

            # -------------------------------------------------
            # EXECUTE COMMAND
            # -------------------------------------------------

            response = self.executor.execute(
                command
            )

            print(
                f"NOVA HANDS-FREE: Response = {response}"
            )

            # -------------------------------------------------
            # SEND RESULT TO MAIN WINDOW
            # -------------------------------------------------

            self.command_detected.emit(
                (
                    command,
                    response
                )
            )

            # -------------------------------------------------
            # BACK TO WAITING
            # -------------------------------------------------

            self.status_changed.emit(
                "WAITING"
            )

        print(
            "NOVA HANDS-FREE: Worker stopped"
        )
# ============================================================
# NOVA WINDOW
# ============================================================

class NovaWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        # ----------------------------------------------------
        # WINDOW
        # ----------------------------------------------------

        self.setWindowTitle(
            "NOVA AI"
        )

        self.resize(
            1450,
            920
        )

        self.setMinimumSize(
            1000,
            700
        )

        # ----------------------------------------------------
        # SERVICES
        # ----------------------------------------------------

        self.executor = CommandExecutor()

        self.history_service = HistoryService()

        self.voice_worker = None
        self.hands_free_worker = None

        # ----------------------------------------------------
        # UI
        # ----------------------------------------------------

        self.setup_ui()

        # ----------------------------------------------------
        # CLOCK
        # ----------------------------------------------------

        self.start_clock()

    # ========================================================
    # SHADOW
    # ========================================================

    def add_shadow(
        self,
        widget,
        blur=35,
        alpha=120
    ):

        shadow = QGraphicsDropShadowEffect()

        shadow.setBlurRadius(
            blur
        )

        shadow.setOffset(
            0,
            6
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
            now.strftime(
                "%I:%M %p"
            )
        )

        self.date_label.setText(
            now.strftime(
                "%A  •  %d %B %Y"
            )
        )

    # ========================================================
    # MAIN UI
    # ========================================================

    def setup_ui(self):

        # ----------------------------------------------------
        # CENTRAL
        # ----------------------------------------------------

        central = QWidget()

        central.setObjectName(
            "mainCentral"
        )

        self.setCentralWidget(
            central
        )

        root = QHBoxLayout(
            central
        )

        root.setContentsMargins(
            0,
            0,
            0,
            0
        )

        root.setSpacing(
            0
        )

        # ====================================================
        # SIDEBAR
        # ====================================================

        self.sidebar = Sidebar(
            page_changed=self.change_page
        )

        root.addWidget(
            self.sidebar
        )

        # ====================================================
        # RIGHT SIDE
        # ====================================================

        right = QWidget()

        right.setObjectName(
            "contentArea"
        )

        right_layout = QVBoxLayout(
            right
        )

        right_layout.setContentsMargins(
            0,
            0,
            0,
            0
        )

        right_layout.setSpacing(
            0
        )

        # ====================================================
        # TOP BAR
        # ====================================================

        topbar = QFrame()

        topbar.setObjectName(
            "topbar"
        )

        top_layout = QHBoxLayout(
            topbar
        )

        top_layout.setContentsMargins(
            25,
            18,
            25,
            18
        )

        top_layout.setSpacing(
            10
        )

        # ----------------------------------------------------
        # PAGE NAME
        # ----------------------------------------------------

        self.page_title = QLabel(
            "DASHBOARD"
        )

        self.page_title.setObjectName(
            "pageTitle"
        )

        top_layout.addWidget(
            self.page_title
        )

        top_layout.addStretch()

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
            13,
            6,
            13,
            6
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

        top_layout.addWidget(
            time_box
        )

        # ----------------------------------------------------
        # LANGUAGE
        # ----------------------------------------------------

        language = QLabel(
            "EN  •  اردو  •  ਪੰਜਾਬੀ"
        )

        language.setObjectName(
            "languagePill"
        )

        top_layout.addWidget(
            language
        )

        # ----------------------------------------------------
        # ONLINE
        # ----------------------------------------------------

        online = QLabel(
            "●  ONLINE"
        )

        online.setObjectName(
            "onlinePill"
        )

        top_layout.addWidget(
            online
        )

        # ----------------------------------------------------
        # SETTINGS BUTTON
        # ----------------------------------------------------

        settings_button = QPushButton(
            "⚙"
        )

        settings_button.setObjectName(
            "topSettings"
        )

        settings_button.setFixedSize(
            42,
            42
        )

        settings_button.clicked.connect(
            lambda: self.change_page(
                "settings"
            )
        )

        top_layout.addWidget(
            settings_button
        )

        right_layout.addWidget(
            topbar
        )

        # ====================================================
        # STACKED PAGES
        # ====================================================

        self.pages = QStackedWidget()

        self.pages.setObjectName(
            "pages"
        )

        # ----------------------------------------------------
        # DASHBOARD
        # ----------------------------------------------------

        self.dashboard = Dashboard()

        self.pages.addWidget(
            self.dashboard
        )

        # ----------------------------------------------------
        # ASSISTANT
        # ----------------------------------------------------

        self.assistant = AssistantPage(
            start_listening=self.start_listening,
            execute_command=self.execute_command
        )

        self.pages.addWidget(
            self.assistant
        )

        # ----------------------------------------------------
        # APPS
        # ----------------------------------------------------

        self.apps = AppsPage(
            execute_command=self.execute_command
        )

        self.pages.addWidget(
            self.apps
        )

        # ----------------------------------------------------
        # HISTORY
        # ----------------------------------------------------

        self.history_page = HistoryPage(
            self.history_service
        )

        self.pages.addWidget(
            self.history_page
        )

        # ----------------------------------------------------
        # SETTINGS
        # ----------------------------------------------------

        self.settings_page = SettingsPage()

        self.settings_page.hands_free_changed.connect(
            self.hands_free_setting_changed
        )
        if self.settings_page.hands_free_checkbox.isChecked():

            QTimer.singleShot(
                500,
                self.start_hands_free
            )

        self.pages.addWidget(
            self.settings_page
        )

        right_layout.addWidget(
            self.pages
        )

        root.addWidget(
            right,
            1
        )

                # ====================================================
        # GLOBAL STYLE
        # ====================================================

        self.setStyleSheet("""

        /* ==================================================
           GENERAL
           ================================================== */

        QWidget {
            font-family: "Segoe UI";
            font-size: 15px;
        }

        QLabel {
            font-size: 15px;
        }

        QPushButton {
            font-size: 15px;
            font-weight: 600;
        }

        QLineEdit {
            font-size: 15px;
        }

        QComboBox {
            font-size: 15px;
        }


        /* ==================================================
           MAIN BACKGROUND
           ================================================== */

        QMainWindow {
            background: #111827;
        }

        QWidget#mainCentral {
            background: #111827;
        }

        QWidget#contentArea {
            background:
                qlineargradient(
                    x1: 0,
                    y1: 0,
                    x2: 1,
                    y2: 1,
                    stop: 0 #111827,
                    stop: 0.5 #172033,
                    stop: 1 #111827
                );
        }


        /* ==================================================
           TOP BAR
           ================================================== */

        QFrame#topbar {
            background: #172033;
            border-bottom: 1px solid #334155;
        }


        /* ==================================================
           PAGE TITLE
           ================================================== */

        QLabel#pageTitle {
            color: #F8FAFC;
            font-size: 18px;
            font-weight: 900;
            letter-spacing: 2px;
        }


        /* ==================================================
           TIME
           ================================================== */

        QFrame#timeBox {
            background: #1E293B;
            border: 1px solid #475569;
            border-radius: 10px;
        }

        QLabel#timeLabel {
            color: #C4B5FD;
            font-size: 16px;
            font-weight: 900;
        }

        QLabel#dateLabel {
            color: #CBD5E1;
            font-size: 12px;
            font-weight: 600;
        }


        /* ==================================================
           LANGUAGE
           ================================================== */

        QLabel#languagePill {
            background: #1E293B;
            color: #E2E8F0;
            border: 1px solid #475569;
            border-radius: 10px;
            padding: 9px 12px;
            font-size: 13px;
            font-weight: 700;
        }


        /* ==================================================
           ONLINE
           ================================================== */

        QLabel#onlinePill {
            background: #12352F;
            color: #5EEAD4;
            border: 1px solid #166534;
            border-radius: 10px;
            padding: 9px 12px;
            font-size: 13px;
            font-weight: 800;
            letter-spacing: 1px;
        }


        /* ==================================================
           SETTINGS
           ================================================== */

        QPushButton#topSettings {
            background: #1E293B;
            color: #C4B5FD;
            border: 1px solid #475569;
            border-radius: 11px;
            font-size: 20px;
        }

        QPushButton#topSettings:hover {
            background: #334155;
            color: #A78BFA;
            border: 1px solid #8B5CF6;
        }


        /* ==================================================
           PAGES
           ================================================== */

        QStackedWidget#pages {
            background: transparent;
        }


        /* ==================================================
           GENERAL TEXT
           ================================================== */

        QLabel {
            color: #F8FAFC;
        }


        /* ==================================================
           BUTTONS
           ================================================== */

        QPushButton {
            color: #F8FAFC;
        }


        /* ==================================================
           INPUTS
           ================================================== */

        QLineEdit {
            color: #F8FAFC;
            background: #1E293B;
            border: 1px solid #475569;
            border-radius: 10px;
            padding: 10px;
        }

        QLineEdit:focus {
            border: 1px solid #8B5CF6;
        }

        QComboBox {
            color: #F8FAFC;
            background: #1E293B;
            border: 1px solid #475569;
            border-radius: 10px;
            padding: 10px;
        }


        /* ==================================================
           SCROLLBAR
           ================================================== */

        QScrollBar:vertical {
            background: #111827;
            width: 10px;
            margin: 2px;
        }

        QScrollBar::handle:vertical {
            background: #475569;
            border-radius: 5px;
            min-height: 40px;
        }

        QScrollBar::handle:vertical:hover {
            background: #64748B;
        }

        QScrollBar::add-line:vertical,
        QScrollBar::sub-line:vertical {
            height: 0px;
        }

        """)

    # ========================================================
    # CHANGE PAGE
    # ========================================================

    def change_page(
        self,
        page
    ):

        page_map = {

            "dashboard": (
                0,
                "DASHBOARD"
            ),

            "assistant": (
                1,
                "NOVA ASSISTANT"
            ),

            "apps": (
                2,
                "APPLICATIONS"
            ),

            "history": (
                3,
                "COMMAND HISTORY"
            ),

            "settings": (
                4,
                "SETTINGS"
            )

        }

        if page not in page_map:

            return

        index, title = page_map[
            page
        ]

        self.pages.setCurrentIndex(
            index
        )

        self.page_title.setText(
            title
        )

        # Refresh history whenever opened

        if page == "history":

            self.history_page.refresh()

    # ========================================================
    # QUICK COMMAND
    # ========================================================

    def execute_command(
        self,
        command
    ):

        response = self.executor.execute(
            command
        )

        self.history_service.add(
            command,
            response,
            True
        )

        self.history_page.refresh()

        return response

    # ========================================================
    # START LISTENING
    # ========================================================

    def start_listening(self):

        if self.voice_worker is not None:

            print(
                "NOVA MAIN: Voice worker already running"
            )

            return

        print(
            "NOVA MAIN: Starting voice worker..."
        )

        self.voice_worker = VoiceWorker()

        self.voice_worker.finished.connect(
            self.voice_finished
        )

        self.voice_worker.start()
    # ========================================================
    # START HANDS-FREE MODE
    # ========================================================

    def start_hands_free(self):

        if self.hands_free_worker is not None:

            print(
                "NOVA MAIN: Hands-free worker already running"
            )

            return

        print(
            "NOVA MAIN: Starting hands-free mode..."
        )

        self.hands_free_worker = HandsFreeWorker()

        self.hands_free_worker.command_detected.connect(
            self.hands_free_command
        )

        self.hands_free_worker.status_changed.connect(
            self.hands_free_status
        )

        self.hands_free_worker.start()
        

    # ========================================================
    # HANDS-FREE COMMAND RESULT
    # ========================================================

    def hands_free_command(self, result):

        command, response = result

        print(
            f"NOVA MAIN: Hands-free command = {command}"
        )

        print(
            f"NOVA MAIN: Hands-free response = {response}"
        )

        # Save to history

        if command:

            self.history_service.add(
                command,
                response
            )

            self.history_page.refresh()

        # Update Assistant UI

        self.assistant.voice_result(
            command,
            response
        )

    # ========================================================
    # HANDS-FREE STATUS
    # ========================================================

    def hands_free_status(self, status):

        print(
            f"NOVA MAIN: Hands-free status = {status}"
        )

    # ============================================================
    # HANDS-FREE SETTING CONTROL
    # ============================================================

    def hands_free_setting_changed(self, enabled):

        print(
            f"NOVA MAIN: Hands-free setting changed = {enabled}"
        )

        if enabled:

            print(
                "NOVA MAIN: Starting hands-free mode..."
            )

            self.start_hands_free()

        else:

            print(
                "NOVA MAIN: Stopping hands-free mode..."
            )

            self.stop_hands_free()


    # ============================================================
    # STOP HANDS-FREE MODE
    # ============================================================

    def stop_hands_free(self):

        if self.hands_free_worker is None:

            print(
                "NOVA MAIN: Hands-free worker is not running"
            )

            return

        print(
            "NOVA MAIN: Stopping hands-free worker..."
        )

        self.hands_free_worker.stop()

        self.hands_free_worker = None

        print(
            "NOVA MAIN: Hands-free mode stopped"
        )
    # ========================================================
    # VOICE FINISHED
    # ========================================================

    def voice_finished(self, result):

        command, response = result

        print(
            f"NOVA MAIN: Voice finished"
        )

        print(
            f"NOVA MAIN: Command = {command}"
        )

        print(
            f"NOVA MAIN: Response = {response}"
        )

        # Save to history

        if command:

            self.history_service.add(
                command,
                response
            )

            self.history_page.refresh()

        # Update Assistant UI

        self.assistant.voice_result(
            command,
            response
        )

        # Worker finished

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
    # window.start_hands_free()

    sys.exit(
        app.exec()
    )


# ============================================================
# RUN
# ============================================================

if __name__ == "__main__":

    main()