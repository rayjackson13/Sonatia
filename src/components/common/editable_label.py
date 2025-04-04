from PySide6.QtWidgets import QLabel, QLineEdit, QVBoxLayout, QWidget, QApplication
from PySide6.QtGui import QCursor
from PySide6.QtCore import Qt, Signal

from constants.colors import Colors

title_style = f"""
    QLabel#EditableLabelText {{
        border: 0;
        color: {Colors.WHITE};
        font-size: 24px;
        line-height: 40px;
        font-weight: 600;
    }}
"""

title_style_hovered = f"""
    QLabel#EditableLabelText {{
        border-bottom: 1px dashed {Colors.WHITE};
        color: {Colors.WHITE};
        font-size: 24px;
        line-height: 40px;
        font-weight: 600;
    }}
"""

edit_style = f"""
    QLineEdit {{
        border: 0;
        color: {Colors.WHITE};
        font-size: 24px;
        line-height: 40px;
        font-weight: 600;
        background-color: transparent;
        padding-bottom: 2px;
    }}
"""

class EditableLabel(QWidget):
    text_changed = Signal(str)
    
    def __init__(self, initial_text):
        super().__init__()
        self.text = initial_text
        self.is_editing = False  # Global flag to track editing mode
        layout = QVBoxLayout(self)
        self.setLayout(layout)
        self.setFixedHeight(40)

        # Create the QLabel
        self.label = QLabel(self.text)
        self.label.setObjectName("EditableLabelText")
        self.label.setStyleSheet(title_style)
        self.label.setCursor(QCursor(Qt.IBeamCursor))  # Set cursor to text-edit style
        layout.addWidget(self.label)

        # Connect QLabel click event to start editing
        self.label.mousePressEvent = self.start_editing

    def start_editing(self, event):
        self.is_editing = True
        # Create the QLineEdit to replace QLabel
        self.edit = QLineEdit(self.text, self)
        self.edit.setStyleSheet(edit_style)  # Optional style for QLineEdit
        self.layout().replaceWidget(self.label, self.edit)
        self.label.deleteLater()  # Remove the QLabel
        self.edit.setFocus()

        # Update text on every key press
        self.edit.textChanged.connect(self.update_text)

        # Connect events to finish editing
        self.edit.editingFinished.connect(self.finish_editing)  # Focus lost
        self.edit.escapePressed = False  # Track Esc key

        # Override keyPressEvent to detect Esc key
        def keyPressEvent(event):
            if event.key() == Qt.Key_Escape:
                self.edit.escapePressed = True
                self.finish_editing()
            else:
                QLineEdit.keyPressEvent(self.edit, event)

        self.edit.keyPressEvent = keyPressEvent

    def update_text(self, text):
        # Update the class variable in real time
        self.text = text

    def finish_editing(self):
        self.text_changed.emit(self.text)
        self.is_editing = False
        # Create a QLabel to replace QLineEdit
        self.label = QLabel(self.text)
        self.label.setObjectName("EditableLabelText")
        self.label.setStyleSheet(title_style)
        self.label.setCursor(QCursor(Qt.IBeamCursor))
        self.layout().replaceWidget(self.edit, self.label)
        self.edit.deleteLater()  # Remove the QLineEdit

        # Reconnect QLabel click event
        self.label.mousePressEvent = self.start_editing

    def enterEvent(self, event):
        # Check if QLabel exists before applying hover logic
        if not self.is_editing:
            self.label.setStyleSheet(title_style_hovered)

    def leaveEvent(self, event):
        # Check if QLabel exists before removing hover effect
        if not self.is_editing:
            self.label.setStyleSheet(title_style)
