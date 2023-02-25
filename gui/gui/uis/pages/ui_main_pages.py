# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_pagesFiYUxU.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_MainPages(object):
    def setupUi(self, MainPages):
        if not MainPages.objectName():
            MainPages.setObjectName(u"MainPages")
        MainPages.resize(860, 600)
        self.main_pages_layout = QVBoxLayout(MainPages)
        self.main_pages_layout.setSpacing(0)
        self.main_pages_layout.setObjectName(u"main_pages_layout")
        self.main_pages_layout.setContentsMargins(5, 5, 5, 5)
        self.pages = QStackedWidget(MainPages)
        self.pages.setObjectName(u"pages")
        self.widget_2 = QWidget()
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"font-size: 14pt")
        self.page_1_layout = QVBoxLayout(self.widget_2)
        self.page_1_layout.setSpacing(5)
        self.page_1_layout.setObjectName(u"page_1_layout")
        self.page_1_layout.setContentsMargins(5, 5, 5, 5)
        self.pages.addWidget(self.widget_2)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2_layout = QVBoxLayout(self.page_2)
        self.page_2_layout.setSpacing(5)
        self.page_2_layout.setObjectName(u"page_2_layout")
        self.page_2_layout.setContentsMargins(5, 5, 5, 5)
        self.scroll_area = QScrollArea(self.page_2)
        self.scroll_area.setObjectName(u"scroll_area")
        self.scroll_area.setStyleSheet(u"background: transparent;")
        self.scroll_area.setFrameShape(QFrame.NoFrame)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setWidgetResizable(True)
        self.contents = QWidget()
        self.contents.setObjectName(u"contents")
        self.contents.setGeometry(QRect(0, 0, 840, 580))
        self.contents.setStyleSheet(u"background: transparent;")
        self.verticalLayout = QVBoxLayout(self.contents)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.row_1_layout = QHBoxLayout()
        self.row_1_layout.setSpacing(0)
        self.row_1_layout.setObjectName(u"row_1_layout")
        self.frame_2 = QFrame(self.contents)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMaximumSize(QSize(200, 200))
        self.frame_2.setLayoutDirection(Qt.LeftToRight)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.image_layout = QHBoxLayout(self.frame_2)
        self.image_layout.setSpacing(0)
        self.image_layout.setObjectName(u"image_layout")
        self.image_layout.setContentsMargins(0, 0, 0, 0)

        self.row_1_layout.addWidget(self.frame_2)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_16 = QLabel(self.contents)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_2.addWidget(self.label_16, 6, 0, 1, 1)

        self.button_reset = QFrame(self.contents)
        self.button_reset.setObjectName(u"button_reset")
        self.button_reset.setMaximumSize(QSize(150, 16777215))
        self.button_reset.setFrameShape(QFrame.StyledPanel)
        self.button_reset.setFrameShadow(QFrame.Raised)
        self.button_reset_layout = QHBoxLayout(self.button_reset)
        self.button_reset_layout.setSpacing(0)
        self.button_reset_layout.setObjectName(u"button_reset_layout")
        self.button_reset_layout.setContentsMargins(0, -1, 0, 0)

        self.gridLayout_2.addWidget(self.button_reset, 8, 0, 1, 1)

        self.label_15 = QLabel(self.contents)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_2.addWidget(self.label_15, 5, 0, 1, 1)

        self.label_11 = QLabel(self.contents)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_2.addWidget(self.label_11, 1, 0, 1, 1)

        self.label_14 = QLabel(self.contents)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_2.addWidget(self.label_14, 4, 0, 1, 1)

        self.frame_5 = QFrame(self.contents)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(150, 16777215))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.textfields_layout_7 = QVBoxLayout(self.frame_5)
        self.textfields_layout_7.setSpacing(0)
        self.textfields_layout_7.setObjectName(u"textfields_layout_7")
        self.textfields_layout_7.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_2.addWidget(self.frame_5, 1, 1, 1, 1)

        self.frame_6 = QFrame(self.contents)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.comboBox = QComboBox(self.frame_6)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMaximumSize(QSize(150, 16777215))

        self.verticalLayout_3.addWidget(self.comboBox)


        self.gridLayout_2.addWidget(self.frame_6, 0, 1, 1, 1)

        self.label_13 = QLabel(self.contents)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_2.addWidget(self.label_13, 3, 0, 1, 1)

        self.frame_10 = QFrame(self.contents)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMaximumSize(QSize(150, 16777215))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.textfields_layout = QVBoxLayout(self.frame_10)
        self.textfields_layout.setSpacing(0)
        self.textfields_layout.setObjectName(u"textfields_layout")
        self.textfields_layout.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_2.addWidget(self.frame_10, 7, 1, 1, 1)

        self.button_calculator = QFrame(self.contents)
        self.button_calculator.setObjectName(u"button_calculator")
        self.button_calculator.setMaximumSize(QSize(150, 16777215))
        self.button_calculator.setFrameShape(QFrame.StyledPanel)
        self.button_calculator.setFrameShadow(QFrame.Raised)
        self.button_calculator_layout = QHBoxLayout(self.button_calculator)
        self.button_calculator_layout.setSpacing(0)
        self.button_calculator_layout.setObjectName(u"button_calculator_layout")
        self.button_calculator_layout.setContentsMargins(0, -1, 0, 0)

        self.gridLayout_2.addWidget(self.button_calculator, 8, 1, 1, 1)

        self.frame_4 = QFrame(self.contents)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(150, 16777215))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.textfields_layout_5 = QVBoxLayout(self.frame_4)
        self.textfields_layout_5.setSpacing(0)
        self.textfields_layout_5.setObjectName(u"textfields_layout_5")
        self.textfields_layout_5.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_2.addWidget(self.frame_4, 3, 1, 1, 1)

        self.frame_3 = QFrame(self.contents)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(150, 16777215))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.textfields_layout_3 = QVBoxLayout(self.frame_3)
        self.textfields_layout_3.setSpacing(0)
        self.textfields_layout_3.setObjectName(u"textfields_layout_3")
        self.textfields_layout_3.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_2.addWidget(self.frame_3, 2, 1, 1, 1)

        self.label_10 = QLabel(self.contents)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_2.addWidget(self.label_10, 0, 0, 1, 1)

        self.frame_8 = QFrame(self.contents)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(150, 16777215))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.textfields_layout_4 = QVBoxLayout(self.frame_8)
        self.textfields_layout_4.setSpacing(0)
        self.textfields_layout_4.setObjectName(u"textfields_layout_4")
        self.textfields_layout_4.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_2.addWidget(self.frame_8, 5, 1, 1, 1)

        self.frame_7 = QFrame(self.contents)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(150, 16777215))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.textfields_layout_6 = QVBoxLayout(self.frame_7)
        self.textfields_layout_6.setSpacing(0)
        self.textfields_layout_6.setObjectName(u"textfields_layout_6")
        self.textfields_layout_6.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_2.addWidget(self.frame_7, 4, 1, 1, 1)

        self.label_17 = QLabel(self.contents)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_2.addWidget(self.label_17, 7, 0, 1, 1)

        self.frame_9 = QFrame(self.contents)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMaximumSize(QSize(150, 16777215))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.textfields_layout_2 = QHBoxLayout(self.frame_9)
        self.textfields_layout_2.setSpacing(0)
        self.textfields_layout_2.setObjectName(u"textfields_layout_2")
        self.textfields_layout_2.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_2.addWidget(self.frame_9, 6, 1, 1, 1)

        self.label_12 = QLabel(self.contents)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_2.addWidget(self.label_12, 2, 0, 1, 1)


        self.row_1_layout.addLayout(self.gridLayout_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, -1, 0)
        self.comboBox_2 = QComboBox(self.contents)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMaximumSize(QSize(200, 16777215))

        self.verticalLayout_4.addWidget(self.comboBox_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.listWidget = QListWidget(self.contents)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy1)
        self.listWidget.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout.addWidget(self.listWidget)

        self.verticalScrollBar = QScrollBar(self.contents)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        sizePolicy1.setHeightForWidth(self.verticalScrollBar.sizePolicy().hasHeightForWidth())
        self.verticalScrollBar.setSizePolicy(sizePolicy1)
        self.verticalScrollBar.setMaximumSize(QSize(10, 16777215))
        self.verticalScrollBar.setOrientation(Qt.Vertical)

        self.horizontalLayout.addWidget(self.verticalScrollBar)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalScrollBar = QScrollBar(self.contents)
        self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        sizePolicy1.setHeightForWidth(self.horizontalScrollBar.sizePolicy().hasHeightForWidth())
        self.horizontalScrollBar.setSizePolicy(sizePolicy1)
        self.horizontalScrollBar.setMaximumSize(QSize(200, 10))
        self.horizontalScrollBar.setOrientation(Qt.Horizontal)

        self.verticalLayout_4.addWidget(self.horizontalScrollBar)


        self.row_1_layout.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setSpacing(5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_21 = QLabel(self.contents)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_3.addWidget(self.label_21, 0, 0, 1, 1)

        self.label_22 = QLabel(self.contents)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_3.addWidget(self.label_22, 1, 0, 1, 1)

        self.label_23 = QLabel(self.contents)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_3.addWidget(self.label_23, 2, 0, 1, 1)

        self.label_24 = QLabel(self.contents)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_3.addWidget(self.label_24, 3, 0, 1, 1)

        self.frame_12 = QFrame(self.contents)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMaximumSize(QSize(100, 16777215))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.label6_field_layout = QVBoxLayout(self.frame_12)
        self.label6_field_layout.setSpacing(0)
        self.label6_field_layout.setObjectName(u"label6_field_layout")
        self.label6_field_layout.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_3.addWidget(self.frame_12, 0, 1, 1, 1)

        self.frame_13 = QFrame(self.contents)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMaximumSize(QSize(100, 16777215))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.label7_field_layout = QVBoxLayout(self.frame_13)
        self.label7_field_layout.setSpacing(0)
        self.label7_field_layout.setObjectName(u"label7_field_layout")
        self.label7_field_layout.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_3.addWidget(self.frame_13, 1, 1, 1, 1)

        self.frame_14 = QFrame(self.contents)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMaximumSize(QSize(100, 16777215))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.label8_field_layout = QVBoxLayout(self.frame_14)
        self.label8_field_layout.setSpacing(0)
        self.label8_field_layout.setObjectName(u"label8_field_layout")
        self.label8_field_layout.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_3.addWidget(self.frame_14, 2, 1, 1, 1)

        self.frame_15 = QFrame(self.contents)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMaximumSize(QSize(100, 16777215))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.label9_field_layout = QVBoxLayout(self.frame_15)
        self.label9_field_layout.setSpacing(0)
        self.label9_field_layout.setObjectName(u"label9_field_layout")
        self.label9_field_layout.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_3.addWidget(self.frame_15, 3, 1, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout_3)

        self.frame_16 = QFrame(self.contents)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMaximumSize(QSize(200, 16777215))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.button_layout_right = QVBoxLayout(self.frame_16)
        self.button_layout_right.setSpacing(0)
        self.button_layout_right.setObjectName(u"button_layout_right")
        self.button_layout_right.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_5.addWidget(self.frame_16)

        self.label_19 = QLabel(self.contents)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMaximumSize(QSize(200, 16777215))

        self.verticalLayout_5.addWidget(self.label_19)

        self.label_20 = QLabel(self.contents)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMaximumSize(QSize(200, 16777215))

        self.verticalLayout_5.addWidget(self.label_20)

        self.frame_11 = QFrame(self.contents)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMaximumSize(QSize(200, 16777215))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.button_layout_right2 = QVBoxLayout(self.frame_11)
        self.button_layout_right2.setSpacing(0)
        self.button_layout_right2.setObjectName(u"button_layout_right2")
        self.button_layout_right2.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_5.addWidget(self.frame_11)


        self.row_1_layout.addLayout(self.verticalLayout_5)


        self.verticalLayout.addLayout(self.row_1_layout)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_6 = QLabel(self.contents)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 0, 2, 1, 1)

        self.label_8 = QLabel(self.contents)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 1, 5, 1, 1)

        self.label_2 = QLabel(self.contents)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 6, 1, 1)

        self.label_7 = QLabel(self.contents)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 0, 1, 1, 1)

        self.label_5 = QLabel(self.contents)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 1, 2, 1, 1)

        self.label_3 = QLabel(self.contents)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 5, 1, 1)

        self.label_4 = QLabel(self.contents)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 1, 1, 1, 1)

        self.label_9 = QLabel(self.contents)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 1, 6, 1, 1)

        self.horizontalSpacer = QSpacerItem(270, 20, QSizePolicy.Ignored, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.row_4_layout = QVBoxLayout()
        self.row_4_layout.setSpacing(5)
        self.row_4_layout.setObjectName(u"row_4_layout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame = QFrame(self.contents)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(120, 16777215))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)

        self.verticalLayout_2.addWidget(self.label)


        self.horizontalLayout_3.addWidget(self.frame)

        self.textfield = QFrame(self.contents)
        self.textfield.setObjectName(u"textfield")
        self.textfield.setMaximumSize(QSize(16777215, 16777215))
        self.textfield.setFrameShape(QFrame.StyledPanel)
        self.textfield.setFrameShadow(QFrame.Raised)
        self.textfield_layout = QVBoxLayout(self.textfield)
        self.textfield_layout.setObjectName(u"textfield_layout")

        self.horizontalLayout_3.addWidget(self.textfield)

        self.button = QFrame(self.contents)
        self.button.setObjectName(u"button")
        self.button.setMaximumSize(QSize(150, 16777215))
        self.button.setFrameShape(QFrame.StyledPanel)
        self.button.setFrameShadow(QFrame.Raised)
        self.button_layout = QHBoxLayout(self.button)
        self.button_layout.setObjectName(u"button_layout")

        self.horizontalLayout_3.addWidget(self.button)


        self.row_4_layout.addLayout(self.horizontalLayout_3)

        self.textbox_layout = QVBoxLayout()
        self.textbox_layout.setObjectName(u"textbox_layout")

        self.row_4_layout.addLayout(self.textbox_layout)


        self.verticalLayout.addLayout(self.row_4_layout)

        self.row_5_layout = QVBoxLayout()
        self.row_5_layout.setSpacing(5)
        self.row_5_layout.setObjectName(u"row_5_layout")
        self.row_5_layout.setSizeConstraint(QLayout.SetDefaultConstraint)

        self.verticalLayout.addLayout(self.row_5_layout)

        self.scroll_area.setWidget(self.contents)

        self.page_2_layout.addWidget(self.scroll_area)

        self.pages.addWidget(self.page_2)
        self.widget = QWidget()
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"QFrame {\n"
"	font-size: 16pt;\n"
"}")
        self.page_3_layout = QVBoxLayout(self.widget)
        self.page_3_layout.setSpacing(0)
        self.page_3_layout.setObjectName(u"page_3_layout")
        self.page_3_layout.setContentsMargins(0, 0, 0, 0)
        self.pages.addWidget(self.widget)

        self.main_pages_layout.addWidget(self.pages)


        self.retranslateUi(MainPages)

        self.pages.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainPages)
    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))
        self.label_16.setText(QCoreApplication.translate("MainPages", u"Nahtubehohung [mm]", None))
        self.label_15.setText(QCoreApplication.translate("MainPages", u"Gewichsuschlag [%]", None))
        self.label_11.setText(QCoreApplication.translate("MainPages", u"a [mm]", None))
        self.label_14.setText(QCoreApplication.translate("MainPages", u"L [m]", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainPages", u"Combo Box", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainPages", u"New Item", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainPages", u"New Item", None))

        self.label_13.setText(QCoreApplication.translate("MainPages", u"Winkel [0]", None))
        self.label_10.setText(QCoreApplication.translate("MainPages", u"Nahart", None))
        self.label_17.setText(QCoreApplication.translate("MainPages", u"Wurzeldurchhang [mm]", None))
        self.label_12.setText(QCoreApplication.translate("MainPages", u"Stegabstand [mm]", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainPages", u"Combo Box", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainPages", u"New Item", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainPages", u"New Item", None))


        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainPages", u"List View 01", None));
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainPages", u"New Item", None));
        ___qlistwidgetitem2 = self.listWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainPages", u"New Item", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.label_21.setText(QCoreApplication.translate("MainPages", u"Label 06", None))
        self.label_22.setText(QCoreApplication.translate("MainPages", u"Label 07", None))
        self.label_23.setText(QCoreApplication.translate("MainPages", u"Label 08", None))
        self.label_24.setText(QCoreApplication.translate("MainPages", u"Label 09", None))
        self.label_19.setText(QCoreApplication.translate("MainPages", u"Label 10", None))
        self.label_20.setText(QCoreApplication.translate("MainPages", u"Label 11", None))
        self.label_6.setText(QCoreApplication.translate("MainPages", u"Label 01", None))
        self.label_8.setText(QCoreApplication.translate("MainPages", u"Gewicht mit zuschlag", None))
        self.label_2.setText(QCoreApplication.translate("MainPages", u"Label 03", None))
        self.label_7.setText(QCoreApplication.translate("MainPages", u"Flache = ", None))
        self.label_5.setText(QCoreApplication.translate("MainPages", u"Label 02", None))
        self.label_3.setText(QCoreApplication.translate("MainPages", u"Gewicht", None))
        self.label_4.setText(QCoreApplication.translate("MainPages", u"Volume = ", None))
        self.label_9.setText(QCoreApplication.translate("MainPages", u"Label 04", None))
        self.label.setText(QCoreApplication.translate("MainPages", u"Bezeichnung = ", None))
    # retranslateUi

