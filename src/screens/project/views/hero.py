from components.common.gradient_image import GradientImageWidget

class HeroSection(GradientImageWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setStyleSheet('background: pink;')
        self.setMinimumWidth(1200)
        self.setMinimumHeight(350)