from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import (
    QPainter,
    QPen,
    QBrush,
    QColor,
    QRadialGradient,
    QConicalGradient,
)


class AICore(QWidget):

    def __init__(self, parent=None):

        super().__init__(parent)

        self.setFixedSize(
            250,
            250
        )

        # =====================================================
        # ANIMATION VALUES
        # =====================================================

        self.phase = 0

        self.pulse = 0

        self.rotation = 0

        self.wave = 0

        self.direction = 1

        # =====================================================
        # ANIMATION TIMER
        # =====================================================

        self.timer = QTimer(self)

        self.timer.timeout.connect(
            self.animate
        )

        self.timer.start(
            30
        )

    # =========================================================
    # ANIMATION
    # =========================================================

    def animate(self):

        # Main animation phase

        self.phase += 1

        if self.phase >= 360:
            self.phase = 0

        # Breathing animation

        self.pulse += self.direction

        if self.pulse >= 18:

            self.direction = -1

        elif self.pulse <= 0:

            self.direction = 1

        # Rotation

        self.rotation += 1.2

        if self.rotation >= 360:

            self.rotation = 0

        # Wave

        self.wave += 4

        if self.wave >= 360:

            self.wave = 0

        self.update()

    # =========================================================
    # PAINT
    # =========================================================

    def paintEvent(self, event):

        painter = QPainter(self)

        painter.setRenderHint(
            QPainter.RenderHint.Antialiasing
        )

        center = self.rect().center()

        # =====================================================
        # OUTER ATMOSPHERIC GLOW
        # =====================================================

        glow_radius = 105 + self.pulse

        glow = QRadialGradient(
            center,
            glow_radius
        )

        glow.setColorAt(
            0.0,
            QColor(
                117,
                76,
                255,
                45
            )
        )

        glow.setColorAt(
            0.45,
            QColor(
                117,
                76,
                255,
                18
            )
        )

        glow.setColorAt(
            1.0,
            QColor(
                117,
                76,
                255,
                0
            )
        )

        painter.setPen(
            Qt.PenStyle.NoPen
        )

        painter.setBrush(
            QBrush(glow)
        )

        painter.drawEllipse(
            center,
            glow_radius,
            glow_radius
        )

        # =====================================================
        # OUTER RING
        # =====================================================

        outer_radius = 96 + self.pulse

        painter.setBrush(
            Qt.BrushStyle.NoBrush
        )

        painter.setPen(
            QPen(
                QColor(
                    117,
                    76,
                    255,
                    30
                ),
                1
            )
        )

        painter.drawEllipse(
            center,
            outer_radius,
            outer_radius
        )

        # =====================================================
        # SECOND OUTER RING
        # =====================================================

        second_radius = 87 + int(
            self.pulse * 0.6
        )

        painter.setPen(
            QPen(
                QColor(
                    155,
                    125,
                    255,
                    70
                ),
                1
            )
        )

        painter.drawEllipse(
            center,
            second_radius,
            second_radius
        )

        # =====================================================
        # ROTATING ENERGY RING
        # =====================================================

        painter.save()

        painter.translate(
            center.x(),
            center.y()
        )

        painter.rotate(
            self.rotation
        )

        energy_gradient = QConicalGradient(
            0,
            0,
            0
        )

        energy_gradient.setColorAt(
            0.0,
            QColor(
                170,
                140,
                255,
                0
            )
        )

        energy_gradient.setColorAt(
            0.15,
            QColor(
                170,
                140,
                255,
                180
            )
        )

        energy_gradient.setColorAt(
            0.28,
            QColor(
                117,
                76,
                255,
                30
            )
        )

        energy_gradient.setColorAt(
            0.50,
            QColor(
                117,
                76,
                255,
                0
            )
        )

        energy_gradient.setColorAt(
            0.70,
            QColor(
                117,
                76,
                255,
                80
            )
        )

        energy_gradient.setColorAt(
            0.85,
            QColor(
                170,
                140,
                255,
                0
            )
        )

        energy_gradient.setColorAt(
            1.0,
            QColor(
                170,
                140,
                255,
                0
            )
        )

        painter.setPen(
            QPen(
                QBrush(energy_gradient),
                3
            )
        )

        painter.drawArc(
            -92,
            -92,
            184,
            184,
            20 * 16,
            105 * 16
        )

        painter.drawArc(
            -92,
            -92,
            184,
            184,
            205 * 16,
            70 * 16
        )

        painter.restore()

        # =====================================================
        # ORBIT DOTS
        # =====================================================

        painter.save()

        painter.translate(
            center.x(),
            center.y()
        )

        painter.rotate(
            -self.rotation * 0.65
        )

        orbit_positions = [
            (0, -92),
            (92, 0),
            (0, 92),
            (-92, 0),
        ]

        for index, position in enumerate(
            orbit_positions
        ):

            x, y = position

            size = 3

            if index % 2 == 0:
                size = 4

            painter.setPen(
                Qt.PenStyle.NoPen
            )

            painter.setBrush(
                QBrush(
                    QColor(
                        172,
                        148,
                        255,
                        150
                    )
                )
            )

            painter.drawEllipse(
                x - size,
                y - size,
                size * 2,
                size * 2
            )

        painter.restore()

        # =====================================================
        # INNER OUTER RING
        # =====================================================

        core_radius = 67

        painter.setPen(
            QPen(
                QColor(
                    123,
                    84,
                    255,
                    220
                ),
                2
            )
        )

        painter.setBrush(
            QBrush(
                QColor(
                    10,
                    8,
                    18,
                    245
                )
            )
        )

        painter.drawEllipse(
            center,
            core_radius,
            core_radius
        )

        # =====================================================
        # INNER CORE GLOW
        # =====================================================

        inner_radius = (
            30
            + int(
                self.pulse * 0.55
            )
        )

        inner_gradient = QRadialGradient(
            center,
            inner_radius
        )

        inner_gradient.setColorAt(
            0.0,
            QColor(
                207,
                190,
                255,
                255
            )
        )

        inner_gradient.setColorAt(
            0.20,
            QColor(
                158,
                124,
                255,
                245
            )
        )

        inner_gradient.setColorAt(
            0.55,
            QColor(
                117,
                76,
                255,
                210
            )
        )

        inner_gradient.setColorAt(
            1.0,
            QColor(
                80,
                45,
                180,
                30
            )
        )

        painter.setPen(
            Qt.PenStyle.NoPen
        )

        painter.setBrush(
            QBrush(
                inner_gradient
            )
        )

        painter.drawEllipse(
            center,
            inner_radius,
            inner_radius
        )

        # =====================================================
        # ENERGY WAVES
        # =====================================================

        wave_radius = (
            38
            + int(
                (self.wave % 80)
            )
        )

        wave_alpha = max(
            0,
            75 - int(
                (self.wave % 80)
                * 0.9
            )
        )

        painter.setPen(
            QPen(
                QColor(
                    170,
                    145,
                    255,
                    wave_alpha
                ),
                1
            )
        )

        painter.setBrush(
            Qt.BrushStyle.NoBrush
        )

        painter.drawEllipse(
            center,
            wave_radius,
            wave_radius
        )

        # =====================================================
        # CENTER LIGHT
        # =====================================================

        center_gradient = QRadialGradient(
            center,
            15
        )

        center_gradient.setColorAt(
            0.0,
            QColor(
                245,
                240,
                255,
                255
            )
        )

        center_gradient.setColorAt(
            0.35,
            QColor(
                190,
                170,
                255,
                255
            )
        )

        center_gradient.setColorAt(
            1.0,
            QColor(
                140,
                110,
                255,
                0
            )
        )

        painter.setBrush(
            QBrush(
                center_gradient
            )
        )

        painter.setPen(
            Qt.PenStyle.NoPen
        )

        painter.drawEllipse(
            center,
            14,
            14
        )

        # =====================================================
        # CENTER POINT
        # =====================================================

        painter.setBrush(
            QBrush(
                QColor(
                    255,
                    255,
                    255,
                    240
                )
            )
        )

        painter.drawEllipse(
            center,
            4,
            4
        )

        # =====================================================
        # SMALL ORBIT PARTICLES
        # =====================================================

        painter.save()

        painter.translate(
            center.x(),
            center.y()
        )

        painter.rotate(
            self.rotation * 1.7
        )

        particles = [
            (-53, -53),
            (53, -53),
            (53, 53),
            (-53, 53),
        ]

        for x, y in particles:

            painter.setBrush(
                QBrush(
                    QColor(
                        137,
                        105,
                        255,
                        110
                    )
                )
            )

            painter.drawEllipse(
                x - 2,
                y - 2,
                4,
                4
            )

        painter.restore()

        painter.end()