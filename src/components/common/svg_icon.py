from os import path

from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter
from PySide6.QtSvg import QSvgRenderer
from PySide6.QtCore import QRect, Qt, QSize, QPoint

from constants.common import PROJECT_ROOT


class Alignment:
    Left = 0
    Middle = 1
    Right = 3


class SvgIcon(QWidget):
    def __init__(
        self, subpath: str, width: int, height: int, align: Alignment = Alignment.Left
    ):
        super().__init__()
        icon_uri = self.get_uri(subpath)
        self.svg_renderer = QSvgRenderer(icon_uri)
        self.align = align
        self.setFixedSize(width, height)

    def get_top_left_position(self, rect: QRect, size: QSize) -> QPoint:
        if self.align == Alignment.Left:
            return rect.topLeft()
        elif self.align == Alignment.Middle:
            return QPoint(int((rect.width() - size.width()) / 2), rect.top())
        elif self.align == Alignment.Right:
            return QPoint(rect.right() - size.width(), rect.top())
        return rect.topLeft()

    def paintEvent(self, event):
        painter = QPainter(self)

        # Get the available area (widget rectangle) and SVG's natural size
        available_rect = self.rect()  # Area to render the SVG
        svg_size = self.svg_renderer.defaultSize()  # Original size of the SVG

        # Scale the SVG to fit within the available area while preserving its aspect ratio
        scaled_size = svg_size.scaled(available_rect.size(), Qt.KeepAspectRatio)
        top_left = self.get_top_left_position(available_rect, scaled_size)
        target_rect = QRect(top_left, scaled_size)

        # Render the SVG into the scaled rectangle
        if self.svg_renderer.isValid():
            self.svg_renderer.render(painter, target_rect)
        else:
            painter.drawText(self.rect(), Qt.AlignCenter, "?")

    def get_uri(self, subpath: str):
        dirs = subpath.split("/")
        return path.join(PROJECT_ROOT, *dirs)
