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

        # =====================================================
        # HEADER
        # =====================================================

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

        # =====================================================
        # NOVA STATUS
        # =====================================================

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

        self.status_value = QLabel(
            "● ONLINE"
        )

        self.status_value.setObjectName(
            "statusValue"
        )

        status_text.addWidget(
            self.status_value
        )

        status_layout.addLayout(
            status_text
        )

        status_layout.addStretch()

        layout.addWidget(
            status_card
        )

        # =====================================================
        # SYSTEM MONITOR
        # =====================================================

        monitor_title = QLabel(
            "SYSTEM MONITOR"
        )

        monitor_title.setObjectName(
            "sectionTitle"
        )

        layout.addWidget(
            monitor_title
        )

        monitor_card = QFrame()

        monitor_card.setObjectName(
            "monitorCard"
        )

        monitor_layout = QHBoxLayout(
            monitor_card
        )

        monitor_layout.setContentsMargins(
            20,
            20,
            20,
            20
        )

        monitor_layout.setSpacing(15)

        # -----------------------------------------------------
        # CPU
        # -----------------------------------------------------

        cpu_box = QVBoxLayout()

        cpu_title = QLabel(
            "CPU"
        )

        cpu_title.setObjectName(
            "monitorTitle"
        )

        self.cpu_value = QLabel(
            "0%"
        )

        self.cpu_value.setObjectName(
            "monitorValue"
        )

        cpu_box.addWidget(
            cpu_title
        )

        cpu_box.addWidget(
            self.cpu_value
        )

        monitor_layout.addLayout(
            cpu_box
        )

        # -----------------------------------------------------
        # RAM
        # -----------------------------------------------------

        ram_box = QVBoxLayout()

        ram_title = QLabel(
            "RAM"
        )

        ram_title.setObjectName(
            "monitorTitle"
        )

        self.ram_value = QLabel(
            "0%"
        )

        self.ram_value.setObjectName(
            "monitorValue"
        )

        ram_box.addWidget(
            ram_title
        )

        ram_box.addWidget(
            self.ram_value
        )

        monitor_layout.addLayout(
            ram_box
        )

        # -----------------------------------------------------
        # DISK
        # -----------------------------------------------------

        disk_box = QVBoxLayout()

        disk_title = QLabel(
            "DISK"
        )

        disk_title.setObjectName(
            "monitorTitle"
        )

        self.disk_value = QLabel(
            "0%"
        )

        self.disk_value.setObjectName(
            "monitorValue"
        )

        disk_box.addWidget(
            disk_title
        )

        disk_box.addWidget(
            self.disk_value
        )

        monitor_layout.addLayout(
            disk_box
        )

        # -----------------------------------------------------
        # BATTERY
        # -----------------------------------------------------

        battery_box = QVBoxLayout()

        battery_title = QLabel(
            "BATTERY"
        )

        battery_title.setObjectName(
            "monitorTitle"
        )

        self.battery_value = QLabel(
            "0%"
        )

        self.battery_value.setObjectName(
            "monitorValue"
        )

        self.power_value = QLabel(
            "Checking..."
        )

        self.power_value.setObjectName(
            "powerValue"
        )

        battery_box.addWidget(
            battery_title
        )

        battery_box.addWidget(
            self.battery_value
        )

        battery_box.addWidget(
            self.power_value
        )

        monitor_layout.addLayout(
            battery_box
        )

        layout.addWidget(
            monitor_card
        )

        # =====================================================
        # WINDOWS
        # =====================================================

        self.windows_value = QLabel(
            "Windows • Checking system..."
        )

        self.windows_value.setObjectName(
            "windowsValue"
        )

        layout.addWidget(
            self.windows_value
        )

        # =====================================================
        # QUICK COMMANDS
        # =====================================================

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

        # =====================================================
        # STYLE
        # =====================================================

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

            QFrame#monitorCard {
                background: #0d0a14;
                border: 1px solid #28203c;
                border-radius: 18px;
            }

            QLabel#monitorTitle {
                color: #625976;
                font-size: 9px;
                font-weight: 900;
                letter-spacing: 1px;
            }

            QLabel#monitorValue {
                color: #ad99ff;
                font-size: 22px;
                font-weight: 900;
            }

            QLabel#powerValue {
                color: #777080;
                font-size: 9px;
            }

            QLabel#windowsValue {
                color: #777080;
                font-size: 10px;
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

    # =========================================================
    # UPDATE SYSTEM MONITOR
    # =========================================================

    def update_system_info(self, info):

        self.cpu_value.setText(
            f"{info['cpu']:.0f}%"
        )

        self.ram_value.setText(
            f"{info['ram']:.0f}%"
        )

        self.disk_value.setText(
            f"{info['disk']:.0f}%"
        )

        self.battery_value.setText(
            f"{info['battery']}%"
        )

        self.power_value.setText(
            info["power"]
        )

        self.windows_value.setText(
            f"{info['windows']} • System Monitor Active"
        )