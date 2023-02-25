

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from gui.core.functions import Functions
from qt_core import *


# STYLE
# ///////////////////////////////////////////////////////////////
style = '''
QPushButton {{
    color: {_color};
	border-radius: {_radius};	
	background-color: {_bg_color};
    font :  15px;
    font-style: italic;
}}
QPushButton:hover {{
	background-color: {_bg_color_hover};
}}
QPushButton:pressed {{	
	background-color: {_bg_color_pressed};
}}
'''


# PY PUSH BUTTON
# ///////////////////////////////////////////////////////////////
class PyImage(QPushButton):
    def __init__(
        self, 
        width,
        height,
        iconName,
        iconHover,
        color = "none",
        text = "",
        radius = 0,
        bg_color = "none",
        bg_color_hover = "none",
        bg_color_pressed = "#272c36",
        parent = None,
    ):
        super().__init__()

        self.__iconHover = iconHover
        self.__iconName = iconName
        self.__width = width
        self.__height = height

        # SET PARAMETRES
        self.setText(text)
        self.setIcon(QIcon(Functions.set_svg_image(iconName)))
        self.setIconSize(QSize(width,height))

        if parent != None:
            self.setParent(parent)
        self.setCursor(Qt.PointingHandCursor)

        # SET STYLESHEET
        custom_style = style.format(
            _color = color,
            _radius = radius,
            _bg_color = bg_color,
            _bg_color_hover = bg_color_hover,
            _bg_color_pressed = bg_color_pressed,
            
        )

        self.setStyleSheet(custom_style)

    def enterEvent(self, QEvent):
        self.setIcon(QIcon(Functions.set_svg_image(self.__iconHover)))
        self.setIconSize(QSize(self.__width,self.__height))

    def leaveEvent(self, QEvent):
        self.setIcon(QIcon(Functions.set_svg_image(self.__iconName)))
        self.setIconSize(QSize(self.__width,self.__height))

        



    



        