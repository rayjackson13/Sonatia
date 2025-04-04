from os import path

from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QImage, QLinearGradient, QColor
from PySide6.QtCore import Qt

from constants.common import PROJECT_ROOT


class GradientImageWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

    def paintEvent(self, _):
        painter = QPainter(self)

        # Load the image
        uri = self.get_uri("assets/images/hero.png")
        image = QImage(uri)
        
        # Scale the image to simulate 'background-size: cover'
        scaled_image = image.scaled(self.width(), self.height(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        
        # Calculate the offset to center the image
        x_offset = (scaled_image.width() - self.width()) // 2
        y_offset = (scaled_image.height() - self.height()) // 2

        # Draw the scaled image with the offset to center it
        painter.drawImage(-x_offset, -y_offset, scaled_image)

        # Create a linear gradient
        gradient = QLinearGradient(0, 0, 0, self.height())  # Diagonal gradient
        gradient.setColorAt(0.0, QColor(0, 0, 0, 255))  # Start color
        gradient.setColorAt(0.5, QColor(255, 255, 255, 0))  # Middle color
        gradient.setColorAt(1.0, QColor(0, 0, 0, 255))  # End color

        # Set the gradient as a brush and paint over the image
        painter.setBrush(gradient)
        painter.setPen(Qt.NoPen)  # Remove border around the gradient
        painter.drawRect(
            0, 0, self.width(), self.height()
        )  # Draw gradient over the widget

    def get_uri(self, subpath: str):
        dirs = subpath.split("/")
        return path.join(PROJECT_ROOT, *dirs)
