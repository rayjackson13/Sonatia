from os import path

from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QFontDatabase, QFont

from constants.common import PROJECT_ROOT

def load_fonts(app: QApplication):
    font_path = path.join(PROJECT_ROOT, 'assets', 'fonts', 'inter.ttf')
    font_id = QFontDatabase.addApplicationFont(font_path)
    
    if font_id == -1:
        print('Failed to load font!')
        return
    
    font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
    custom_font = QFont(font_family)
    custom_font.setHintingPreference(QFont.PreferNoHinting)
    custom_font.setPixelSize(16)
    custom_font.setStyleStrategy(QFont.PreferAntialias)
    app.setFont(custom_font)