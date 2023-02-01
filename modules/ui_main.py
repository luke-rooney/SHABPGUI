# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QMainWindow, QProgressBar,
    QPushButton, QRadioButton, QSizePolicy, QSlider,
    QSpacerItem, QStackedWidget, QTextEdit, QVBoxLayout,
    QWidget)

from mplwidget import (MplCanvas, MplCanvas2D)
from . resources_rc import *
from superqt import QLabeledRangeSlider, QLabeledDoubleRangeSlider

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QSize(940, 560))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background"
                        "-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/PyDracula.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(18"
                        "9, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb("
                        "189, 147, 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border"
                        "-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-sty"
                        "le: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb"
                        "(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-co"
                        "lor: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-c"
                        "olor: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
""
                        "QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     su"
                        "bcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	back"
                        "ground-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subco"
                        "ntrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    h"
                        "eight: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLi"
                        "nkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.verticalLayout_15 = QVBoxLayout(self.styleSheet)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.frame = QFrame(self.topLogoInfo)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(8, 4, 42, 42))
        self.frame.setStyleSheet(u"border-image:url(:/images/images/images/paper-plane-icon.png)")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_meshResizer = QPushButton(self.topMenu)
        self.btn_meshResizer.setObjectName(u"btn_meshResizer")
        sizePolicy.setHeightForWidth(self.btn_meshResizer.sizePolicy().hasHeightForWidth())
        self.btn_meshResizer.setSizePolicy(sizePolicy)
        self.btn_meshResizer.setMinimumSize(QSize(0, 45))
        self.btn_meshResizer.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_8.addWidget(self.btn_meshResizer)

        self.btn_pressure = QPushButton(self.topMenu)
        self.btn_pressure.setObjectName(u"btn_pressure")
        sizePolicy.setHeightForWidth(self.btn_pressure.sizePolicy().hasHeightForWidth())
        self.btn_pressure.setSizePolicy(sizePolicy)
        self.btn_pressure.setMinimumSize(QSize(0, 45))
        self.btn_pressure.setFont(font)
        self.btn_pressure.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pressure.setLayoutDirection(Qt.LeftToRight)
        self.btn_pressure.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-pressure.png);")

        self.verticalLayout_8.addWidget(self.btn_pressure)

        self.btn_plots = QPushButton(self.topMenu)
        self.btn_plots.setObjectName(u"btn_plots")
        sizePolicy.setHeightForWidth(self.btn_plots.sizePolicy().hasHeightForWidth())
        self.btn_plots.setSizePolicy(sizePolicy)
        self.btn_plots.setMinimumSize(QSize(0, 45))
        self.btn_plots.setFont(font)
        self.btn_plots.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_plots.setLayoutDirection(Qt.LeftToRight)
        self.btn_plots.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-chart-line.png);")

        self.verticalLayout_8.addWidget(self.btn_plots)

        self.btn_tables = QPushButton(self.topMenu)
        self.btn_tables.setObjectName(u"btn_tables")
        sizePolicy.setHeightForWidth(self.btn_tables.sizePolicy().hasHeightForWidth())
        self.btn_tables.setSizePolicy(sizePolicy)
        self.btn_tables.setMinimumSize(QSize(0, 45))
        self.btn_tables.setFont(font)
        self.btn_tables.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_tables.setLayoutDirection(Qt.LeftToRight)
        self.btn_tables.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-view-quilt.png);")

        self.verticalLayout_8.addWidget(self.btn_tables)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.toggleLeftBox = QPushButton(self.bottomMenu)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        sizePolicy.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy)
        self.toggleLeftBox.setMinimumSize(QSize(0, 45))
        self.toggleLeftBox.setFont(font)
        self.toggleLeftBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LeftToRight)
        self.toggleLeftBox.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_settings.png);")

        self.verticalLayout_9.addWidget(self.toggleLeftBox)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_lightmode = QPushButton(self.extraTopMenu)
        self.btn_lightmode.setObjectName(u"btn_lightmode")
        sizePolicy.setHeightForWidth(self.btn_lightmode.sizePolicy().hasHeightForWidth())
        self.btn_lightmode.setSizePolicy(sizePolicy)
        self.btn_lightmode.setMinimumSize(QSize(0, 45))
        self.btn_lightmode.setFont(font)
        self.btn_lightmode.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_lightmode.setLayoutDirection(Qt.LeftToRight)
        self.btn_lightmode.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-lightbulb.png);")

        self.verticalLayout_11.addWidget(self.btn_lightmode)

        self.btn_darkmode = QPushButton(self.extraTopMenu)
        self.btn_darkmode.setObjectName(u"btn_darkmode")
        sizePolicy.setHeightForWidth(self.btn_darkmode.sizePolicy().hasHeightForWidth())
        self.btn_darkmode.setSizePolicy(sizePolicy)
        self.btn_darkmode.setMinimumSize(QSize(0, 45))
        self.btn_darkmode.setFont(font)
        self.btn_darkmode.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_darkmode.setLayoutDirection(Qt.LeftToRight)
        self.btn_darkmode.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-moon.png);")

        self.verticalLayout_11.addWidget(self.btn_darkmode)


        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.textEdit)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon1)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font3)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon2)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setEnabled(True)
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.pagesContainer)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.home.sizePolicy().hasHeightForWidth())
        self.home.setSizePolicy(sizePolicy3)
        self.home.setStyleSheet(u"")
        self.verticalLayout_22 = QVBoxLayout(self.home)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_5.setHorizontalSpacing(-1)
        self.gridLayout_5.setContentsMargins(-1, -1, -1, 0)
        self.open_stl_button = QPushButton(self.home)
        self.open_stl_button.setObjectName(u"open_stl_button")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.open_stl_button.sizePolicy().hasHeightForWidth())
        self.open_stl_button.setSizePolicy(sizePolicy4)
        self.open_stl_button.setMinimumSize(QSize(150, 30))
        self.open_stl_button.setFont(font)
        self.open_stl_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.open_stl_button.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.open_stl_button.setIcon(icon3)

        self.gridLayout_5.addWidget(self.open_stl_button, 0, 1, 1, 1)

        self.FileLocationText = QLineEdit(self.home)
        self.FileLocationText.setObjectName(u"FileLocationText")
        self.FileLocationText.setMinimumSize(QSize(0, 30))
        self.FileLocationText.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_5.addWidget(self.FileLocationText, 0, 0, 1, 1)

        self.FileLocationLabel = QLabel(self.home)
        self.FileLocationLabel.setObjectName(u"FileLocationLabel")
        sizePolicy1.setHeightForWidth(self.FileLocationLabel.sizePolicy().hasHeightForWidth())
        self.FileLocationLabel.setSizePolicy(sizePolicy1)
        self.FileLocationLabel.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.FileLocationLabel.setLineWidth(1)
        self.FileLocationLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.FileLocationLabel, 1, 0, 1, 2)


        self.verticalLayout_21.addLayout(self.gridLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        self.label = QLabel(self.home)
        self.label.setObjectName(u"label")
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setBold(True)
        font4.setItalic(False)
        self.label.setFont(font4)
        self.label.setStyleSheet(u"font-size: 12px; font-weight: bold; color: rgb(189, 147, 249)")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(self.home)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.mean_aero_chord_val = QLineEdit(self.home)
        self.mean_aero_chord_val.setObjectName(u"mean_aero_chord_val")
        sizePolicy.setHeightForWidth(self.mean_aero_chord_val.sizePolicy().hasHeightForWidth())
        self.mean_aero_chord_val.setSizePolicy(sizePolicy)
        self.mean_aero_chord_val.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.mean_aero_chord_val)

        self.label_3 = QLabel(self.home)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.span_val = QLineEdit(self.home)
        self.span_val.setObjectName(u"span_val")
        sizePolicy.setHeightForWidth(self.span_val.sizePolicy().hasHeightForWidth())
        self.span_val.setSizePolicy(sizePolicy)
        self.span_val.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.span_val)

        self.label_4 = QLabel(self.home)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.reference_area_val = QLineEdit(self.home)
        self.reference_area_val.setObjectName(u"reference_area_val")
        sizePolicy.setHeightForWidth(self.reference_area_val.sizePolicy().hasHeightForWidth())
        self.reference_area_val.setSizePolicy(sizePolicy)
        self.reference_area_val.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.reference_area_val)

        self.label_5 = QLabel(self.home)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_5)

        self.cgx_val = QLineEdit(self.home)
        self.cgx_val.setObjectName(u"cgx_val")
        sizePolicy.setHeightForWidth(self.cgx_val.sizePolicy().hasHeightForWidth())
        self.cgx_val.setSizePolicy(sizePolicy)
        self.cgx_val.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.cgx_val)

        self.label_6 = QLabel(self.home)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.label_6)

        self.cgy_val = QLineEdit(self.home)
        self.cgy_val.setObjectName(u"cgy_val")
        sizePolicy.setHeightForWidth(self.cgy_val.sizePolicy().hasHeightForWidth())
        self.cgy_val.setSizePolicy(sizePolicy)
        self.cgy_val.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.cgy_val)

        self.label_7 = QLabel(self.home)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.label_7)

        self.cgz_val = QLineEdit(self.home)
        self.cgz_val.setObjectName(u"cgz_val")
        sizePolicy.setHeightForWidth(self.cgz_val.sizePolicy().hasHeightForWidth())
        self.cgz_val.setSizePolicy(sizePolicy)
        self.cgz_val.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.cgz_val)

        self.label_8 = QLabel(self.home)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_2.setWidget(7, QFormLayout.LabelRole, self.label_8)

        self.mass_val = QLineEdit(self.home)
        self.mass_val.setObjectName(u"mass_val")
        sizePolicy.setHeightForWidth(self.mass_val.sizePolicy().hasHeightForWidth())
        self.mass_val.setSizePolicy(sizePolicy)
        self.mass_val.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.formLayout_2.setWidget(7, QFormLayout.FieldRole, self.mass_val)

        self.label_9 = QLabel(self.home)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_2.setWidget(8, QFormLayout.LabelRole, self.label_9)

        self.compression_method_box = QComboBox(self.home)
        self.compression_method_box.addItem("")
        self.compression_method_box.addItem("")
        self.compression_method_box.addItem("")
        self.compression_method_box.addItem("")
        self.compression_method_box.addItem("")
        self.compression_method_box.addItem("")
        self.compression_method_box.setObjectName(u"compression_method_box")
        sizePolicy.setHeightForWidth(self.compression_method_box.sizePolicy().hasHeightForWidth())
        self.compression_method_box.setSizePolicy(sizePolicy)
        self.compression_method_box.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.formLayout_2.setWidget(8, QFormLayout.FieldRole, self.compression_method_box)

        self.label_10 = QLabel(self.home)
        self.label_10.setObjectName(u"label_10")

        self.formLayout_2.setWidget(9, QFormLayout.LabelRole, self.label_10)

        self.expansion_method_box = QComboBox(self.home)
        self.expansion_method_box.addItem("")
        self.expansion_method_box.addItem("")
        self.expansion_method_box.addItem("")
        self.expansion_method_box.addItem("")
        self.expansion_method_box.addItem("")
        self.expansion_method_box.addItem("")
        self.expansion_method_box.setObjectName(u"expansion_method_box")
        sizePolicy.setHeightForWidth(self.expansion_method_box.sizePolicy().hasHeightForWidth())
        self.expansion_method_box.setSizePolicy(sizePolicy)
        self.expansion_method_box.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.formLayout_2.setWidget(9, QFormLayout.FieldRole, self.expansion_method_box)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_2.setItem(10, QFormLayout.FieldRole, self.verticalSpacer_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_2.setItem(11, QFormLayout.FieldRole, self.verticalSpacer)


        self.horizontalLayout_6.addLayout(self.formLayout_2)

        self.MplWidget = MplCanvas(self.home)
        self.MplWidget.setObjectName(u"MplWidget")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.MplWidget.sizePolicy().hasHeightForWidth())
        self.MplWidget.setSizePolicy(sizePolicy5)
        self.MplWidget.setMinimumSize(QSize(150, 0))
        self.MplWidget.setToolTipDuration(0)
        self.MplWidget.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_6.addWidget(self.MplWidget)

        self.horizontalLayout_6.setStretch(0, 5)
        self.horizontalLayout_6.setStretch(1, 6)

        self.verticalLayout_21.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.vehicle_status = QLabel(self.home)
        self.vehicle_status.setObjectName(u"vehicle_status")
        sizePolicy1.setHeightForWidth(self.vehicle_status.sizePolicy().hasHeightForWidth())
        self.vehicle_status.setSizePolicy(sizePolicy1)
        self.vehicle_status.setStyleSheet(u"color: rgb(220,20,60)")

        self.horizontalLayout_7.addWidget(self.vehicle_status)

        self.btn_create_vehicle = QPushButton(self.home)
        self.btn_create_vehicle.setObjectName(u"btn_create_vehicle")
        sizePolicy4.setHeightForWidth(self.btn_create_vehicle.sizePolicy().hasHeightForWidth())
        self.btn_create_vehicle.setSizePolicy(sizePolicy4)
        self.btn_create_vehicle.setMinimumSize(QSize(150, 30))
        self.btn_create_vehicle.setMaximumSize(QSize(150, 30))
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setPointSize(10)
        font5.setBold(False)
        font5.setItalic(False)
        font5.setStyleStrategy(QFont.NoAntialias)
        self.btn_create_vehicle.setFont(font5)
        self.btn_create_vehicle.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.horizontalLayout_7.addWidget(self.btn_create_vehicle)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)


        self.verticalLayout_21.addLayout(self.horizontalLayout_7)


        self.verticalLayout_22.addLayout(self.verticalLayout_21)

        self.stackedWidget.addWidget(self.home)
        self.MeshResizer = QWidget()
        self.MeshResizer.setObjectName(u"MeshResizer")
        self.verticalLayout_25 = QVBoxLayout(self.MeshResizer)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_26 = QLabel(self.MeshResizer)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setStyleSheet(u"font-size: 12px; font-weight: bold; color: rgb(189, 147, 249)")
        self.label_26.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.label_26)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_32 = QLabel(self.MeshResizer)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setStyleSheet(u"font-size: 12px; font-weight: bold; color: rgb(189, 147, 249)")
        self.label_32.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.label_32)


        self.verticalLayout_27.addLayout(self.horizontalLayout_17)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lbl_span = QLabel(self.MeshResizer)
        self.lbl_span.setObjectName(u"lbl_span")
        self.lbl_span.setStyleSheet(u"font-size: 12px; font-weight: bold; color: rgb(189, 147, 249)")
        self.lbl_span.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.lbl_span, 0, 2, 1, 1)

        self.lbl_height = QLabel(self.MeshResizer)
        self.lbl_height.setObjectName(u"lbl_height")
        self.lbl_height.setStyleSheet(u"font-size: 12px; font-weight: bold; color: rgb(189, 147, 249)")
        self.lbl_height.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.lbl_height, 0, 4, 1, 1)

        self.val_len = QLabel(self.MeshResizer)
        self.val_len.setObjectName(u"val_len")

        self.gridLayout_3.addWidget(self.val_len, 0, 1, 1, 1)

        self.lbl_len = QLabel(self.MeshResizer)
        self.lbl_len.setObjectName(u"lbl_len")
        self.lbl_len.setStyleSheet(u"font-size: 12px; font-weight: bold; color: rgb(189, 147, 249)")
        self.lbl_len.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.lbl_len, 0, 0, 1, 1)

        self.val_height = QLabel(self.MeshResizer)
        self.val_height.setObjectName(u"val_height")

        self.gridLayout_3.addWidget(self.val_height, 0, 5, 1, 1)

        self.val_span = QLabel(self.MeshResizer)
        self.val_span.setObjectName(u"val_span")

        self.gridLayout_3.addWidget(self.val_span, 0, 3, 1, 1)

        self.label_40 = QLabel(self.MeshResizer)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setStyleSheet(u"font-size: 12px; font-weight: bold; color: rgb(189, 147, 249)")
        self.label_40.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_40, 1, 0, 1, 1)

        self.minx_val = QLabel(self.MeshResizer)
        self.minx_val.setObjectName(u"minx_val")

        self.gridLayout_3.addWidget(self.minx_val, 1, 1, 1, 1)

        self.label_44 = QLabel(self.MeshResizer)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setStyleSheet(u"font-size: 12px; font-weight: bold; color: rgb(189, 147, 249)")
        self.label_44.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_44, 1, 2, 1, 1)

        self.miny_val = QLabel(self.MeshResizer)
        self.miny_val.setObjectName(u"miny_val")

        self.gridLayout_3.addWidget(self.miny_val, 1, 3, 1, 1)

        self.label_47 = QLabel(self.MeshResizer)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setStyleSheet(u"font-size: 12px; font-weight: bold; color: rgb(189, 147, 249)")
        self.label_47.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_47, 1, 4, 1, 1)

        self.minz_val = QLabel(self.MeshResizer)
        self.minz_val.setObjectName(u"minz_val")

        self.gridLayout_3.addWidget(self.minz_val, 1, 5, 1, 1)


        self.verticalLayout_27.addLayout(self.gridLayout_3)

        self.line_2 = QFrame(self.MeshResizer)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_27.addWidget(self.line_2)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_27.addItem(self.verticalSpacer_6)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_34 = QLabel(self.MeshResizer)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setStyleSheet(u"font-size: 12px; font-weight: bold; color: rgb(189, 147, 249)")
        self.label_34.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.label_34)


        self.verticalLayout_27.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_25 = QLabel(self.MeshResizer)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setStyleSheet(u"font-size: 12px; font-weight: bold; color: rgb(189, 147, 249)")

        self.horizontalLayout_10.addWidget(self.label_25)

        self.x_scale = QLineEdit(self.MeshResizer)
        self.x_scale.setObjectName(u"x_scale")
        self.x_scale.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_10.addWidget(self.x_scale)

        self.y_scale = QLineEdit(self.MeshResizer)
        self.y_scale.setObjectName(u"y_scale")
        self.y_scale.setEnabled(False)
        self.y_scale.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.y_scale.setReadOnly(False)

        self.horizontalLayout_10.addWidget(self.y_scale)

        self.z_scale = QLineEdit(self.MeshResizer)
        self.z_scale.setObjectName(u"z_scale")
        self.z_scale.setEnabled(False)
        self.z_scale.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_10.addWidget(self.z_scale)

        self.Lock_scale = QRadioButton(self.MeshResizer)
        self.Lock_scale.setObjectName(u"Lock_scale")
        self.Lock_scale.setChecked(True)

        self.horizontalLayout_10.addWidget(self.Lock_scale)


        self.verticalLayout_27.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.btn_scale = QPushButton(self.MeshResizer)
        self.btn_scale.setObjectName(u"btn_scale")
        self.btn_scale.setMinimumSize(QSize(0, 30))
        self.btn_scale.setMaximumSize(QSize(150, 16777215))
        self.btn_scale.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.horizontalLayout_14.addWidget(self.btn_scale)


        self.verticalLayout_27.addLayout(self.horizontalLayout_14)

        self.line = QFrame(self.MeshResizer)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_27.addWidget(self.line)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_27.addItem(self.verticalSpacer_7)

        self.label_36 = QLabel(self.MeshResizer)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setStyleSheet(u"font-size: 12px; font-weight: bold; color: rgb(189, 147, 249)")
        self.label_36.setAlignment(Qt.AlignCenter)

        self.verticalLayout_27.addWidget(self.label_36)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.z_rotate_left = QPushButton(self.MeshResizer)
        self.z_rotate_left.setObjectName(u"z_rotate_left")
        self.z_rotate_left.setMinimumSize(QSize(0, 30))
        self.z_rotate_left.setMaximumSize(QSize(150, 16777215))
        self.z_rotate_left.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_6.addWidget(self.z_rotate_left, 2, 2, 1, 1)

        self.label_30 = QLabel(self.MeshResizer)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_30, 0, 2, 1, 1)

        self.z_rotate_right = QPushButton(self.MeshResizer)
        self.z_rotate_right.setObjectName(u"z_rotate_right")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.z_rotate_right.sizePolicy().hasHeightForWidth())
        self.z_rotate_right.setSizePolicy(sizePolicy6)
        self.z_rotate_right.setMinimumSize(QSize(0, 30))
        self.z_rotate_right.setMaximumSize(QSize(150, 16777215))
        self.z_rotate_right.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_6.addWidget(self.z_rotate_right, 1, 2, 1, 1)

        self.y_rotate_left = QPushButton(self.MeshResizer)
        self.y_rotate_left.setObjectName(u"y_rotate_left")
        self.y_rotate_left.setMinimumSize(QSize(0, 30))
        self.y_rotate_left.setMaximumSize(QSize(150, 16777215))
        self.y_rotate_left.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_6.addWidget(self.y_rotate_left, 2, 1, 1, 1)

        self.label_28 = QLabel(self.MeshResizer)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_28, 0, 1, 1, 1)

        self.label_27 = QLabel(self.MeshResizer)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_27, 0, 0, 1, 1)

        self.x_rotate_left = QPushButton(self.MeshResizer)
        self.x_rotate_left.setObjectName(u"x_rotate_left")
        self.x_rotate_left.setMinimumSize(QSize(0, 30))
        self.x_rotate_left.setMaximumSize(QSize(150, 16777215))
        self.x_rotate_left.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_6.addWidget(self.x_rotate_left, 2, 0, 1, 1)

        self.x_rotate_right = QPushButton(self.MeshResizer)
        self.x_rotate_right.setObjectName(u"x_rotate_right")
        self.x_rotate_right.setMinimumSize(QSize(0, 30))
        self.x_rotate_right.setMaximumSize(QSize(150, 16777215))
        self.x_rotate_right.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_6.addWidget(self.x_rotate_right, 1, 0, 1, 1)

        self.y_rotate_right = QPushButton(self.MeshResizer)
        self.y_rotate_right.setObjectName(u"y_rotate_right")
        self.y_rotate_right.setMinimumSize(QSize(0, 30))
        self.y_rotate_right.setMaximumSize(QSize(150, 16777215))
        self.y_rotate_right.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_6.addWidget(self.y_rotate_right, 1, 1, 1, 1)


        self.verticalLayout_27.addLayout(self.gridLayout_6)

        self.line_3 = QFrame(self.MeshResizer)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_27.addWidget(self.line_3)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_27.addItem(self.verticalSpacer_5)

        self.label_38 = QLabel(self.MeshResizer)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setStyleSheet(u"font-size: 12px; font-weight: bold; color: rgb(189, 147, 249)")
        self.label_38.setAlignment(Qt.AlignCenter)

        self.verticalLayout_27.addWidget(self.label_38)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.x_translate = QLineEdit(self.MeshResizer)
        self.x_translate.setObjectName(u"x_translate")
        self.x_translate.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_15.addWidget(self.x_translate)

        self.y_translate = QLineEdit(self.MeshResizer)
        self.y_translate.setObjectName(u"y_translate")
        self.y_translate.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_15.addWidget(self.y_translate)

        self.z_translate = QLineEdit(self.MeshResizer)
        self.z_translate.setObjectName(u"z_translate")
        self.z_translate.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_15.addWidget(self.z_translate)


        self.verticalLayout_27.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.btn_translate = QPushButton(self.MeshResizer)
        self.btn_translate.setObjectName(u"btn_translate")
        self.btn_translate.setMinimumSize(QSize(0, 30))
        self.btn_translate.setMaximumSize(QSize(150, 16777215))
        self.btn_translate.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.horizontalLayout_16.addWidget(self.btn_translate)


        self.verticalLayout_27.addLayout(self.horizontalLayout_16)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_27.addItem(self.verticalSpacer_8)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.btn_saveas = QPushButton(self.MeshResizer)
        self.btn_saveas.setObjectName(u"btn_saveas")
        self.btn_saveas.setMinimumSize(QSize(0, 30))
        self.btn_saveas.setMaximumSize(QSize(150, 16777215))
        self.btn_saveas.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.horizontalLayout_21.addWidget(self.btn_saveas)


        self.verticalLayout_27.addLayout(self.horizontalLayout_21)


        self.horizontalLayout_19.addLayout(self.verticalLayout_27)

        self.MeshEditorPreview = MplCanvas(self.MeshResizer)
        self.MeshEditorPreview.setObjectName(u"MeshEditorPreview")

        self.horizontalLayout_19.addWidget(self.MeshEditorPreview)

        self.horizontalLayout_19.setStretch(0, 1)
        self.horizontalLayout_19.setStretch(1, 1)

        self.verticalLayout_25.addLayout(self.horizontalLayout_19)

        self.stackedWidget.addWidget(self.MeshResizer)
        self.comparemethods = QWidget()
        self.comparemethods.setObjectName(u"comparemethods")
        self.verticalLayout_26 = QVBoxLayout(self.comparemethods)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.MethodsForm = QFormLayout()
        self.MethodsForm.setObjectName(u"MethodsForm")
        self.label_12 = QLabel(self.comparemethods)
        self.label_12.setObjectName(u"label_12")

        self.MethodsForm.setWidget(0, QFormLayout.LabelRole, self.label_12)

        self.label_19 = QLabel(self.comparemethods)
        self.label_19.setObjectName(u"label_19")

        self.MethodsForm.setWidget(0, QFormLayout.FieldRole, self.label_19)

        self.label_13 = QLabel(self.comparemethods)
        self.label_13.setObjectName(u"label_13")

        self.MethodsForm.setWidget(1, QFormLayout.LabelRole, self.label_13)

        self.comp_newtonian = QCheckBox(self.comparemethods)
        self.comp_newtonian.setObjectName(u"comp_newtonian")

        self.MethodsForm.setWidget(1, QFormLayout.FieldRole, self.comp_newtonian)

        self.label_14 = QLabel(self.comparemethods)
        self.label_14.setObjectName(u"label_14")

        self.MethodsForm.setWidget(2, QFormLayout.LabelRole, self.label_14)

        self.comp_npm = QCheckBox(self.comparemethods)
        self.comp_npm.setObjectName(u"comp_npm")

        self.MethodsForm.setWidget(2, QFormLayout.FieldRole, self.comp_npm)

        self.label_15 = QLabel(self.comparemethods)
        self.label_15.setObjectName(u"label_15")

        self.MethodsForm.setWidget(3, QFormLayout.LabelRole, self.label_15)

        self.comp_mn = QCheckBox(self.comparemethods)
        self.comp_mn.setObjectName(u"comp_mn")

        self.MethodsForm.setWidget(3, QFormLayout.FieldRole, self.comp_mn)

        self.label_16 = QLabel(self.comparemethods)
        self.label_16.setObjectName(u"label_16")

        self.MethodsForm.setWidget(4, QFormLayout.LabelRole, self.label_16)

        self.comp_hankey = QCheckBox(self.comparemethods)
        self.comp_hankey.setObjectName(u"comp_hankey")

        self.MethodsForm.setWidget(4, QFormLayout.FieldRole, self.comp_hankey)

        self.label_17 = QLabel(self.comparemethods)
        self.label_17.setObjectName(u"label_17")

        self.MethodsForm.setWidget(5, QFormLayout.LabelRole, self.label_17)

        self.comp_vandyke = QCheckBox(self.comparemethods)
        self.comp_vandyke.setObjectName(u"comp_vandyke")

        self.MethodsForm.setWidget(5, QFormLayout.FieldRole, self.comp_vandyke)

        self.label_18 = QLabel(self.comparemethods)
        self.label_18.setObjectName(u"label_18")

        self.MethodsForm.setWidget(6, QFormLayout.LabelRole, self.label_18)

        self.comp_busemann = QCheckBox(self.comparemethods)
        self.comp_busemann.setObjectName(u"comp_busemann")

        self.MethodsForm.setWidget(6, QFormLayout.FieldRole, self.comp_busemann)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.MethodsForm.setItem(7, QFormLayout.LabelRole, self.verticalSpacer_4)

        self.label_21 = QLabel(self.comparemethods)
        self.label_21.setObjectName(u"label_21")

        self.MethodsForm.setWidget(10, QFormLayout.LabelRole, self.label_21)

        self.aoa_slider = QLabeledRangeSlider(self.comparemethods)
        self.aoa_slider.setObjectName(u"aoa_slider")
        self.aoa_slider.setMinimumSize(QSize(300, 0))
        self.aoa_slider.setMinimum(-90)
        self.aoa_slider.setMaximum(90)
        self.aoa_slider.setSliderPosition([0, 25])
        self.aoa_slider.setOrientation(Qt.Horizontal)
        self.aoa_slider.setInvertedAppearance(False)
        self.aoa_slider.setInvertedControls(False)
        self.aoa_slider.setTickPosition(QSlider.TicksBelow)
        self.aoa_slider.setTickInterval(1)

        self.MethodsForm.setWidget(10, QFormLayout.FieldRole, self.aoa_slider)

        self.label_22 = QLabel(self.comparemethods)
        self.label_22.setObjectName(u"label_22")

        self.MethodsForm.setWidget(11, QFormLayout.LabelRole, self.label_22)

        self.sideslip_slider = QLabeledRangeSlider(self.comparemethods)
        self.sideslip_slider.setObjectName(u"sideslip_slider")
        self.sideslip_slider.setSliderPosition([0, 25])
        self.sideslip_slider.setMinimumSize(QSize(300, 0))
        self.sideslip_slider.setMinimum(-90)
        self.sideslip_slider.setMaximum(90)
        self.sideslip_slider.setOrientation(Qt.Horizontal)
        self.sideslip_slider.setTickPosition(QSlider.TicksBelow)
        self.sideslip_slider.setTickInterval(1)

        self.MethodsForm.setWidget(11, QFormLayout.FieldRole, self.sideslip_slider)

        self.label_20 = QLabel(self.comparemethods)
        self.label_20.setObjectName(u"label_20")

        self.MethodsForm.setWidget(12, QFormLayout.LabelRole, self.label_20)

        self.Compare_PlotName = QComboBox(self.comparemethods)
        self.Compare_PlotName.addItem("")
        self.Compare_PlotName.addItem("")
        self.Compare_PlotName.addItem("")
        self.Compare_PlotName.addItem("")
        self.Compare_PlotName.addItem("")
        self.Compare_PlotName.addItem("")
        self.Compare_PlotName.addItem("")
        self.Compare_PlotName.addItem("")
        self.Compare_PlotName.addItem("")
        self.Compare_PlotName.addItem("")
        self.Compare_PlotName.addItem("")
        self.Compare_PlotName.addItem("")
        self.Compare_PlotName.addItem("")
        self.Compare_PlotName.addItem("")
        self.Compare_PlotName.addItem("")
        self.Compare_PlotName.addItem("")
        self.Compare_PlotName.addItem("")
        self.Compare_PlotName.addItem("")
        self.Compare_PlotName.addItem("")
        self.Compare_PlotName.setObjectName(u"Compare_PlotName")
        sizePolicy.setHeightForWidth(self.Compare_PlotName.sizePolicy().hasHeightForWidth())
        self.Compare_PlotName.setSizePolicy(sizePolicy)
        self.Compare_PlotName.setMinimumSize(QSize(300, 0))
        self.Compare_PlotName.setStyleSheet(u"background-color: rgb(52, 59, 72); selection-background-color: rgb(189, 147, 249);")

        self.MethodsForm.setWidget(12, QFormLayout.FieldRole, self.Compare_PlotName)

        self.label_23 = QLabel(self.comparemethods)
        self.label_23.setObjectName(u"label_23")

        self.MethodsForm.setWidget(8, QFormLayout.LabelRole, self.label_23)

        self.label_24 = QLabel(self.comparemethods)
        self.label_24.setObjectName(u"label_24")

        self.MethodsForm.setWidget(9, QFormLayout.LabelRole, self.label_24)

        self.compare_MachNumber = QLineEdit(self.comparemethods)
        self.compare_MachNumber.setObjectName(u"compare_MachNumber")
        self.compare_MachNumber.setStyleSheet(u"background-color: rgb(52, 59, 72); selection-background-color: rgb(189, 147, 249);")

        self.MethodsForm.setWidget(8, QFormLayout.FieldRole, self.compare_MachNumber)

        self.Compare_gamma = QLineEdit(self.comparemethods)
        self.Compare_gamma.setObjectName(u"Compare_gamma")
        self.Compare_gamma.setStyleSheet(u"background-color: rgb(52, 59, 72); selection-background-color: rgb(189, 147, 249);")

        self.MethodsForm.setWidget(9, QFormLayout.FieldRole, self.Compare_gamma)


        self.horizontalLayout_8.addLayout(self.MethodsForm)

        self.comparison_plot = MplCanvas2D(self.comparemethods)
        self.comparison_plot.setObjectName(u"comparison_plot")
        self.comparison_plot.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.horizontalLayout_8.addWidget(self.comparison_plot)

        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 1)

        self.verticalLayout_24.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.compare_vehiclestatus = QLabel(self.comparemethods)
        self.compare_vehiclestatus.setObjectName(u"compare_vehiclestatus")
        sizePolicy1.setHeightForWidth(self.compare_vehiclestatus.sizePolicy().hasHeightForWidth())
        self.compare_vehiclestatus.setSizePolicy(sizePolicy1)
        self.compare_vehiclestatus.setStyleSheet(u"color: rgb(220,20,60)")

        self.horizontalLayout_13.addWidget(self.compare_vehiclestatus)

        self.btn_compareMethods = QPushButton(self.comparemethods)
        self.btn_compareMethods.setObjectName(u"btn_compareMethods")
        sizePolicy7 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.btn_compareMethods.sizePolicy().hasHeightForWidth())
        self.btn_compareMethods.setSizePolicy(sizePolicy7)
        self.btn_compareMethods.setMinimumSize(QSize(150, 30))
        self.btn_compareMethods.setMaximumSize(QSize(150, 16777215))
        self.btn_compareMethods.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.horizontalLayout_13.addWidget(self.btn_compareMethods)

        self.exportcompare_progress = QProgressBar(self.comparemethods)
        self.exportcompare_progress.setObjectName(u"exportcompare_progress")
        self.exportcompare_progress.setMaximumSize(QSize(16777215, 10))
        self.exportcompare_progress.setStyleSheet(u"QProgressBar::chunk{background:  rgb(189, 147, 249); border-radius: 5px; }")
        self.exportcompare_progress.setValue(0)
        self.exportcompare_progress.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.exportcompare_progress)

        self.compare_export_csv = QPushButton(self.comparemethods)
        self.compare_export_csv.setObjectName(u"compare_export_csv")
        self.compare_export_csv.setMinimumSize(QSize(150, 30))
        self.compare_export_csv.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.horizontalLayout_13.addWidget(self.compare_export_csv)


        self.verticalLayout_24.addLayout(self.horizontalLayout_13)


        self.verticalLayout_26.addLayout(self.verticalLayout_24)

        self.stackedWidget.addWidget(self.comparemethods)
        self.lookup = QWidget()
        self.lookup.setObjectName(u"lookup")
        self.lookup.setStyleSheet(u"b")
        self.verticalLayout = QVBoxLayout(self.lookup)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.Title_Export_Lookup_Table = QLabel(self.lookup)
        self.Title_Export_Lookup_Table.setObjectName(u"Title_Export_Lookup_Table")
        self.Title_Export_Lookup_Table.setStyleSheet(u"font-size: 12px; font-weight: bold; color: rgb(189, 147, 249)")
        self.Title_Export_Lookup_Table.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.Title_Export_Lookup_Table)

        self.row_1 = QFrame(self.lookup)
        self.row_1.setObjectName(u"row_1")
        self.row_1.setFrameShape(QFrame.StyledPanel)
        self.row_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.row_1)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_42 = QLabel(self.row_1)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setStyleSheet(u"font-size: 12px; font-weight: bold; color: rgb(189, 147, 249)")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_42)

        self.mach_slider_lookup = QLabeledDoubleRangeSlider(self.row_1)
        self.mach_slider_lookup.setObjectName(u"mach_slider_lookup")
        self.mach_slider_lookup.setMinimumSize(QSize(600, 0))
        self.mach_slider_lookup.setMinimum(1)
        self.mach_slider_lookup.setMaximum(30)
        self.mach_slider_lookup.setSingleStep(1)
        self.mach_slider_lookup.setSliderPosition([2, 5])
        self.mach_slider_lookup.setOrientation(Qt.Horizontal)
        self.mach_slider_lookup.setTickPosition(QSlider.TicksBelow)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.mach_slider_lookup)

        self.label_45 = QLabel(self.row_1)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setStyleSheet(u"font-size: 12px; font-weight: bold; color: rgb(189, 147, 249)")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_45)

        self.gamma_slider_lookup = QLabeledDoubleRangeSlider(self.row_1)
        self.gamma_slider_lookup.setObjectName(u"gamma_slider_lookup")
        self.gamma_slider_lookup.setMinimumSize(QSize(600, 0))
        self.gamma_slider_lookup.setSliderPosition([1.3, 1.4])
        self.gamma_slider_lookup.setMinimum(1.1)
        self.gamma_slider_lookup.setMaximum(1.4)
        self.gamma_slider_lookup.setSliderPosition(13)
        self.gamma_slider_lookup.setOrientation(Qt.Horizontal)
        self.gamma_slider_lookup.setTickPosition(QSlider.TicksBelow)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.gamma_slider_lookup)

        self.label_48 = QLabel(self.row_1)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setStyleSheet(u"font-size: 12px; font-weight: bold; color: rgb(189, 147, 249)")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_48)

        self.aoa_slider_lookup = QLabeledRangeSlider(self.row_1)
        self.aoa_slider_lookup.setSliderPosition([0, 25])
        self.aoa_slider_lookup.setObjectName(u"aoa_slider_lookup")
        self.aoa_slider_lookup.setMinimumSize(QSize(600, 0))
        self.aoa_slider_lookup.setMinimum(-90)
        self.aoa_slider_lookup.setMaximum(90)
        self.aoa_slider_lookup.setOrientation(Qt.Horizontal)
        self.aoa_slider_lookup.setTickPosition(QSlider.TicksBelow)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.aoa_slider_lookup)

        self.label_49 = QLabel(self.row_1)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setStyleSheet(u"font-size: 12px; font-weight: bold; color: rgb(189, 147, 249)")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_49)

        self.beta_slider_lookup = QLabeledRangeSlider(self.row_1)
        self.beta_slider_lookup.setSliderPosition([0, 25])
        self.beta_slider_lookup.setObjectName(u"beta_slider_lookup")
        self.beta_slider_lookup.setMinimumSize(QSize(600, 0))
        self.beta_slider_lookup.setMinimum(-90)
        self.beta_slider_lookup.setMaximum(90)
        self.beta_slider_lookup.setOrientation(Qt.Horizontal)
        self.beta_slider_lookup.setTickPosition(QSlider.TicksBelow)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.beta_slider_lookup)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(4, QFormLayout.FieldRole, self.verticalSpacer_10)


        self.verticalLayout_16.addLayout(self.formLayout)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.formLayout_4.setFormAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.formLayout_4.setHorizontalSpacing(-1)
        self.label_50 = QLabel(self.row_1)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setStyleSheet(u"font-size: 12px; font-weight: bold; color: rgb(189, 147, 249)")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_50)

        self.label_51 = QLabel(self.row_1)
        self.label_51.setObjectName(u"label_51")

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.label_51)

        self.label_52 = QLabel(self.row_1)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setMinimumSize(QSize(175, 20))

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.label_52)

        self.lookup_newtonian_check = QCheckBox(self.row_1)
        self.lookup_newtonian_check.setObjectName(u"lookup_newtonian_check")

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.lookup_newtonian_check)

        self.label_53 = QLabel(self.row_1)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setMinimumSize(QSize(175, 20))
        self.label_53.setSizeIncrement(QSize(0, 20))

        self.formLayout_4.setWidget(3, QFormLayout.LabelRole, self.label_53)

        self.lookup_npm_check = QCheckBox(self.row_1)
        self.lookup_npm_check.setObjectName(u"lookup_npm_check")
        sizePolicy8 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.lookup_npm_check.sizePolicy().hasHeightForWidth())
        self.lookup_npm_check.setSizePolicy(sizePolicy8)
        self.lookup_npm_check.setLayoutDirection(Qt.LeftToRight)
        self.lookup_npm_check.setInputMethodHints(Qt.ImhMultiLine)

        self.formLayout_4.setWidget(3, QFormLayout.FieldRole, self.lookup_npm_check)

        self.label_54 = QLabel(self.row_1)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setMinimumSize(QSize(175, 20))
        self.label_54.setSizeIncrement(QSize(0, 20))

        self.formLayout_4.setWidget(4, QFormLayout.LabelRole, self.label_54)

        self.lookup_mn_check = QCheckBox(self.row_1)
        self.lookup_mn_check.setObjectName(u"lookup_mn_check")

        self.formLayout_4.setWidget(4, QFormLayout.FieldRole, self.lookup_mn_check)

        self.label_55 = QLabel(self.row_1)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setMinimumSize(QSize(175, 20))

        self.formLayout_4.setWidget(5, QFormLayout.LabelRole, self.label_55)

        self.lookup_hankey_check = QCheckBox(self.row_1)
        self.lookup_hankey_check.setObjectName(u"lookup_hankey_check")

        self.formLayout_4.setWidget(5, QFormLayout.FieldRole, self.lookup_hankey_check)

        self.label_56 = QLabel(self.row_1)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setMinimumSize(QSize(175, 20))

        self.formLayout_4.setWidget(6, QFormLayout.LabelRole, self.label_56)

        self.lookup_vandyke_check = QCheckBox(self.row_1)
        self.lookup_vandyke_check.setObjectName(u"lookup_vandyke_check")

        self.formLayout_4.setWidget(6, QFormLayout.FieldRole, self.lookup_vandyke_check)

        self.label_57 = QLabel(self.row_1)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setMinimumSize(QSize(175, 20))

        self.formLayout_4.setWidget(7, QFormLayout.LabelRole, self.label_57)

        self.lookup_busemann_check = QCheckBox(self.row_1)
        self.lookup_busemann_check.setObjectName(u"lookup_busemann_check")

        self.formLayout_4.setWidget(7, QFormLayout.FieldRole, self.lookup_busemann_check)

        self.label_66 = QLabel(self.row_1)
        self.label_66.setObjectName(u"label_66")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.label_66)

        self.label_67 = QLabel(self.row_1)
        self.label_67.setObjectName(u"label_67")

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.label_67)


        self.horizontalLayout_9.addLayout(self.formLayout_4)

        self.formLayout_5 = QFormLayout()
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.label_58 = QLabel(self.row_1)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setStyleSheet(u"font-size: 12px; font-weight: bold; color: rgb(189, 147, 249)")

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.label_58)

        self.label_59 = QLabel(self.row_1)
        self.label_59.setObjectName(u"label_59")

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.label_59)

        self.label_60 = QLabel(self.row_1)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setMinimumSize(QSize(175, 20))

        self.formLayout_5.setWidget(2, QFormLayout.LabelRole, self.label_60)

        self.label_61 = QLabel(self.row_1)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setMinimumSize(QSize(175, 20))

        self.formLayout_5.setWidget(3, QFormLayout.LabelRole, self.label_61)

        self.label_62 = QLabel(self.row_1)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setMinimumSize(QSize(175, 20))

        self.formLayout_5.setWidget(4, QFormLayout.LabelRole, self.label_62)

        self.label_63 = QLabel(self.row_1)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setMinimumSize(QSize(175, 20))

        self.formLayout_5.setWidget(5, QFormLayout.LabelRole, self.label_63)

        self.label_64 = QLabel(self.row_1)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setMinimumSize(QSize(175, 20))

        self.formLayout_5.setWidget(6, QFormLayout.LabelRole, self.label_64)

        self.label_65 = QLabel(self.row_1)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setMinimumSize(QSize(175, 20))

        self.formLayout_5.setWidget(7, QFormLayout.LabelRole, self.label_65)

        self.lookup_exp_newtonian_check = QCheckBox(self.row_1)
        self.lookup_exp_newtonian_check.setObjectName(u"lookup_exp_newtonian_check")

        self.formLayout_5.setWidget(2, QFormLayout.FieldRole, self.lookup_exp_newtonian_check)

        self.lookup_exp_npm_check = QCheckBox(self.row_1)
        self.lookup_exp_npm_check.setObjectName(u"lookup_exp_npm_check")

        self.formLayout_5.setWidget(3, QFormLayout.FieldRole, self.lookup_exp_npm_check)

        self.lookup_exp_mn_check = QCheckBox(self.row_1)
        self.lookup_exp_mn_check.setObjectName(u"lookup_exp_mn_check")

        self.formLayout_5.setWidget(4, QFormLayout.FieldRole, self.lookup_exp_mn_check)

        self.lookup_exp_hankey_check = QCheckBox(self.row_1)
        self.lookup_exp_hankey_check.setObjectName(u"lookup_exp_hankey_check")

        self.formLayout_5.setWidget(5, QFormLayout.FieldRole, self.lookup_exp_hankey_check)

        self.lookup_exp_vandyke_check = QCheckBox(self.row_1)
        self.lookup_exp_vandyke_check.setObjectName(u"lookup_exp_vandyke_check")

        self.formLayout_5.setWidget(6, QFormLayout.FieldRole, self.lookup_exp_vandyke_check)

        self.lookup_exp_busemann_check = QCheckBox(self.row_1)
        self.lookup_exp_busemann_check.setObjectName(u"lookup_exp_busemann_check")

        self.formLayout_5.setWidget(7, QFormLayout.FieldRole, self.lookup_exp_busemann_check)

        self.label_68 = QLabel(self.row_1)
        self.label_68.setObjectName(u"label_68")

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.label_68)

        self.label_69 = QLabel(self.row_1)
        self.label_69.setObjectName(u"label_69")

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.label_69)


        self.horizontalLayout_9.addLayout(self.formLayout_5)


        self.verticalLayout_16.addLayout(self.horizontalLayout_9)


        self.verticalLayout.addWidget(self.row_1)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_9)

        self.lookup_table_progress = QProgressBar(self.lookup)
        self.lookup_table_progress.setObjectName(u"lookup_table_progress")
        self.lookup_table_progress.setStyleSheet(u"QProgressBar::chunk{background:  rgb(189, 147, 249); border-radius: 5px; }")
        self.lookup_table_progress.setValue(0)
        self.lookup_table_progress.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lookup_table_progress)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.btn_export_lookup = QPushButton(self.lookup)
        self.btn_export_lookup.setObjectName(u"btn_export_lookup")
        self.btn_export_lookup.setMinimumSize(QSize(0, 30))
        self.btn_export_lookup.setMaximumSize(QSize(150, 16777215))
        self.btn_export_lookup.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.horizontalLayout_12.addWidget(self.btn_export_lookup)


        self.verticalLayout.addLayout(self.horizontalLayout_12)

        self.stackedWidget.addWidget(self.lookup)
        self.pressurepage = QWidget()
        self.pressurepage.setObjectName(u"pressurepage")
        self.verticalLayout_20 = QVBoxLayout(self.pressurepage)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.pressure_horizontal = QHBoxLayout()
        self.pressure_horizontal.setObjectName(u"pressure_horizontal")
        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_11 = QLabel(self.pressurepage)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"font-size: 12px; font-weight: bold; color: rgb(189, 147, 249)")

        self.verticalLayout_23.addWidget(self.label_11)

        self.pressure_form = QFormLayout()
        self.pressure_form.setObjectName(u"pressure_form")
        self.p_machNumber_label = QLabel(self.pressurepage)
        self.p_machNumber_label.setObjectName(u"p_machNumber_label")
        sizePolicy1.setHeightForWidth(self.p_machNumber_label.sizePolicy().hasHeightForWidth())
        self.p_machNumber_label.setSizePolicy(sizePolicy1)

        self.pressure_form.setWidget(0, QFormLayout.LabelRole, self.p_machNumber_label)

        self.p_mach_val = QLineEdit(self.pressurepage)
        self.p_mach_val.setObjectName(u"p_mach_val")
        sizePolicy.setHeightForWidth(self.p_mach_val.sizePolicy().hasHeightForWidth())
        self.p_mach_val.setSizePolicy(sizePolicy)
        self.p_mach_val.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.pressure_form.setWidget(0, QFormLayout.FieldRole, self.p_mach_val)

        self.p_gamma = QLabel(self.pressurepage)
        self.p_gamma.setObjectName(u"p_gamma")
        sizePolicy9 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.p_gamma.sizePolicy().hasHeightForWidth())
        self.p_gamma.setSizePolicy(sizePolicy9)

        self.pressure_form.setWidget(1, QFormLayout.LabelRole, self.p_gamma)

        self.p_gamma_val = QLineEdit(self.pressurepage)
        self.p_gamma_val.setObjectName(u"p_gamma_val")
        sizePolicy.setHeightForWidth(self.p_gamma_val.sizePolicy().hasHeightForWidth())
        self.p_gamma_val.setSizePolicy(sizePolicy)
        self.p_gamma_val.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.pressure_form.setWidget(1, QFormLayout.FieldRole, self.p_gamma_val)

        self.p_alpha_label = QLabel(self.pressurepage)
        self.p_alpha_label.setObjectName(u"p_alpha_label")
        sizePolicy1.setHeightForWidth(self.p_alpha_label.sizePolicy().hasHeightForWidth())
        self.p_alpha_label.setSizePolicy(sizePolicy1)

        self.pressure_form.setWidget(2, QFormLayout.LabelRole, self.p_alpha_label)

        self.p_alpha_val = QLineEdit(self.pressurepage)
        self.p_alpha_val.setObjectName(u"p_alpha_val")
        sizePolicy.setHeightForWidth(self.p_alpha_val.sizePolicy().hasHeightForWidth())
        self.p_alpha_val.setSizePolicy(sizePolicy)
        self.p_alpha_val.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.pressure_form.setWidget(2, QFormLayout.FieldRole, self.p_alpha_val)

        self.p_beta_label = QLabel(self.pressurepage)
        self.p_beta_label.setObjectName(u"p_beta_label")
        sizePolicy1.setHeightForWidth(self.p_beta_label.sizePolicy().hasHeightForWidth())
        self.p_beta_label.setSizePolicy(sizePolicy1)

        self.pressure_form.setWidget(3, QFormLayout.LabelRole, self.p_beta_label)

        self.p_beta_val = QLineEdit(self.pressurepage)
        self.p_beta_val.setObjectName(u"p_beta_val")
        sizePolicy.setHeightForWidth(self.p_beta_val.sizePolicy().hasHeightForWidth())
        self.p_beta_val.setSizePolicy(sizePolicy)
        self.p_beta_val.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.pressure_form.setWidget(3, QFormLayout.FieldRole, self.p_beta_val)

        self.p_compression_label = QLabel(self.pressurepage)
        self.p_compression_label.setObjectName(u"p_compression_label")
        sizePolicy1.setHeightForWidth(self.p_compression_label.sizePolicy().hasHeightForWidth())
        self.p_compression_label.setSizePolicy(sizePolicy1)

        self.pressure_form.setWidget(4, QFormLayout.LabelRole, self.p_compression_label)

        self.p_compression_val = QComboBox(self.pressurepage)
        self.p_compression_val.addItem("")
        self.p_compression_val.addItem("")
        self.p_compression_val.addItem("")
        self.p_compression_val.addItem("")
        self.p_compression_val.addItem("")
        self.p_compression_val.addItem("")
        self.p_compression_val.setObjectName(u"p_compression_val")
        sizePolicy.setHeightForWidth(self.p_compression_val.sizePolicy().hasHeightForWidth())
        self.p_compression_val.setSizePolicy(sizePolicy)
        self.p_compression_val.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.pressure_form.setWidget(4, QFormLayout.FieldRole, self.p_compression_val)

        self.p_expansion_label = QLabel(self.pressurepage)
        self.p_expansion_label.setObjectName(u"p_expansion_label")
        sizePolicy1.setHeightForWidth(self.p_expansion_label.sizePolicy().hasHeightForWidth())
        self.p_expansion_label.setSizePolicy(sizePolicy1)

        self.pressure_form.setWidget(5, QFormLayout.LabelRole, self.p_expansion_label)

        self.p_expansion_val = QComboBox(self.pressurepage)
        self.p_expansion_val.addItem("")
        self.p_expansion_val.addItem("")
        self.p_expansion_val.addItem("")
        self.p_expansion_val.addItem("")
        self.p_expansion_val.addItem("")
        self.p_expansion_val.addItem("")
        self.p_expansion_val.setObjectName(u"p_expansion_val")
        sizePolicy.setHeightForWidth(self.p_expansion_val.sizePolicy().hasHeightForWidth())
        self.p_expansion_val.setSizePolicy(sizePolicy)
        self.p_expansion_val.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.pressure_form.setWidget(5, QFormLayout.FieldRole, self.p_expansion_val)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.pressure_form.setItem(6, QFormLayout.FieldRole, self.verticalSpacer_3)


        self.verticalLayout_23.addLayout(self.pressure_form)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_39 = QLabel(self.pressurepage)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_39, 1, 4, 1, 1)

        self.label_35 = QLabel(self.pressurepage)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_35, 1, 0, 1, 1)

        self.cyprime_val = QLabel(self.pressurepage)
        self.cyprime_val.setObjectName(u"cyprime_val")

        self.gridLayout_4.addWidget(self.cyprime_val, 0, 5, 1, 1)

        self.cy_val = QLabel(self.pressurepage)
        self.cy_val.setObjectName(u"cy_val")

        self.gridLayout_4.addWidget(self.cy_val, 1, 3, 1, 1)

        self.label_29 = QLabel(self.pressurepage)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_29, 0, 0, 1, 1)

        self.cz_val = QLabel(self.pressurepage)
        self.cz_val.setObjectName(u"cz_val")

        self.gridLayout_4.addWidget(self.cz_val, 1, 5, 1, 1)

        self.label_33 = QLabel(self.pressurepage)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_33, 0, 4, 1, 1)

        self.label_31 = QLabel(self.pressurepage)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_31, 0, 2, 1, 1)

        self.cl_val = QLabel(self.pressurepage)
        self.cl_val.setObjectName(u"cl_val")

        self.gridLayout_4.addWidget(self.cl_val, 0, 1, 1, 1)

        self.cd_val = QLabel(self.pressurepage)
        self.cd_val.setObjectName(u"cd_val")

        self.gridLayout_4.addWidget(self.cd_val, 0, 3, 1, 1)

        self.cx_val = QLabel(self.pressurepage)
        self.cx_val.setObjectName(u"cx_val")

        self.gridLayout_4.addWidget(self.cx_val, 1, 1, 1, 1)

        self.label_37 = QLabel(self.pressurepage)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_37, 1, 2, 1, 1)

        self.label_41 = QLabel(self.pressurepage)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_41, 2, 0, 1, 1)

        self.cmx_val = QLabel(self.pressurepage)
        self.cmx_val.setObjectName(u"cmx_val")

        self.gridLayout_4.addWidget(self.cmx_val, 2, 1, 1, 1)

        self.label_43 = QLabel(self.pressurepage)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_43, 2, 2, 1, 1)

        self.cmy_val = QLabel(self.pressurepage)
        self.cmy_val.setObjectName(u"cmy_val")

        self.gridLayout_4.addWidget(self.cmy_val, 2, 3, 1, 1)

        self.cmz_val = QLabel(self.pressurepage)
        self.cmz_val.setObjectName(u"cmz_val")

        self.gridLayout_4.addWidget(self.cmz_val, 2, 5, 1, 1)

        self.label_46 = QLabel(self.pressurepage)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_46, 2, 4, 1, 1)


        self.verticalLayout_23.addLayout(self.gridLayout_4)


        self.pressure_horizontal.addLayout(self.verticalLayout_23)

        self.pressureplot = MplCanvas(self.pressurepage)
        self.pressureplot.setObjectName(u"pressureplot")

        self.pressure_horizontal.addWidget(self.pressureplot)

        self.pressure_horizontal.setStretch(0, 4)
        self.pressure_horizontal.setStretch(1, 5)

        self.verticalLayout_20.addLayout(self.pressure_horizontal)

        self.pressure_button = QHBoxLayout()
        self.pressure_button.setObjectName(u"pressure_button")
        self.btn_plotpressure = QPushButton(self.pressurepage)
        self.btn_plotpressure.setObjectName(u"btn_plotpressure")
        self.btn_plotpressure.setMinimumSize(QSize(0, 30))
        self.btn_plotpressure.setMaximumSize(QSize(300, 16777215))
        self.btn_plotpressure.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.pressure_button.addWidget(self.btn_plotpressure)


        self.verticalLayout_20.addLayout(self.pressure_button)

        self.stackedWidget.addWidget(self.pressurepage)

        self.horizontalLayout_20.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_message = QPushButton(self.topMenus)
        self.btn_message.setObjectName(u"btn_message")
        sizePolicy.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy)
        self.btn_message.setMinimumSize(QSize(0, 45))
        self.btn_message.setFont(font)
        self.btn_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LeftToRight)
        self.btn_message.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-open.png);")

        self.verticalLayout_14.addWidget(self.btn_message)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(font)
        self.btn_print.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LeftToRight)
        self.btn_print.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-print.png);")

        self.verticalLayout_14.addWidget(self.btn_print)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font6 = QFont()
        font6.setFamilies([u"Segoe UI"])
        font6.setBold(False)
        font6.setItalic(False)
        self.creditsLabel.setFont(font6)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.verticalLayout_15.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"Super/Hypersonic Arbitrary Body Program", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"Modified By UNSW", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_meshResizer.setText(QCoreApplication.translate("MainWindow", u"Mesh Editor", None))
        self.btn_pressure.setText(QCoreApplication.translate("MainWindow", u"Pressure Map Plots", None))
        self.btn_plots.setText(QCoreApplication.translate("MainWindow", u"Plot Results", None))
        self.btn_tables.setText(QCoreApplication.translate("MainWindow", u"Generate Lookup Tables", None))
        self.toggleLeftBox.setText("")
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.btn_lightmode.setText(QCoreApplication.translate("MainWindow", u"Light Mode", None))
        self.btn_darkmode.setText(QCoreApplication.translate("MainWindow", u"Dark Mode", None))
        self.textEdit.setMarkdown("")
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"S/HABP UNSW", None))
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.open_stl_button.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.FileLocationText.setText("")
        self.FileLocationText.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.FileLocationLabel.setText(QCoreApplication.translate("MainWindow", u"Open .STL File", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Vehicle Parameters:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Mean Aerodynamic Chord (m)", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Span (m)", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Reference Area (m^2)", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Center of Gravity X Axis (m)", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Center of Gravity Y Axis (m)", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Center of Gravity Z Axis (m)", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Mass (kg)", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Compression Panel Method", None))
        self.compression_method_box.setItemText(0, QCoreApplication.translate("MainWindow", u"Newtonian Method", None))
        self.compression_method_box.setItemText(1, QCoreApplication.translate("MainWindow", u"Newtonian Prandtl Meyer", None))
        self.compression_method_box.setItemText(2, QCoreApplication.translate("MainWindow", u"Modified Newtonian", None))
        self.compression_method_box.setItemText(3, QCoreApplication.translate("MainWindow", u"Hankey Flat Surface", None))
        self.compression_method_box.setItemText(4, QCoreApplication.translate("MainWindow", u"Van Dyke Unified", None))
        self.compression_method_box.setItemText(5, QCoreApplication.translate("MainWindow", u"Busemann Second Order Theory", None))

        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Expansion Panel Method", None))
        self.expansion_method_box.setItemText(0, QCoreApplication.translate("MainWindow", u"Newtonian Method", None))
        self.expansion_method_box.setItemText(1, QCoreApplication.translate("MainWindow", u"Newtonian Prandtl Meyer", None))
        self.expansion_method_box.setItemText(2, QCoreApplication.translate("MainWindow", u"Modified Newtonian", None))
        self.expansion_method_box.setItemText(3, QCoreApplication.translate("MainWindow", u"Hankey Flat Surface", None))
        self.expansion_method_box.setItemText(4, QCoreApplication.translate("MainWindow", u"Van Dyke Unified", None))
        self.expansion_method_box.setItemText(5, QCoreApplication.translate("MainWindow", u"Busemann Second Order Theory", None))

        self.vehicle_status.setText(QCoreApplication.translate("MainWindow", u"No Vehicle Object", None))
        self.btn_create_vehicle.setText(QCoreApplication.translate("MainWindow", u"Create Vehicle", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Mesh Editor", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Vehicle Details", None))
        self.lbl_span.setText(QCoreApplication.translate("MainWindow", u"Span:", None))
        self.lbl_height.setText(QCoreApplication.translate("MainWindow", u"Height:", None))
        self.val_len.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lbl_len.setText(QCoreApplication.translate("MainWindow", u"Length:", None))
        self.val_height.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.val_span.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Min x:", None))
        self.minx_val.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Min y:", None))
        self.miny_val.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Min z:", None))
        self.minz_val.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Scale Mesh", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Scale:", None))
        self.Lock_scale.setText(QCoreApplication.translate("MainWindow", u"Locked", None))
        self.btn_scale.setText(QCoreApplication.translate("MainWindow", u"Scale", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Re-Orient Mesh", None))
        self.z_rotate_left.setText(QCoreApplication.translate("MainWindow", u"Rotate Right", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Z", None))
        self.z_rotate_right.setText(QCoreApplication.translate("MainWindow", u"Rotate Right", None))
        self.y_rotate_left.setText(QCoreApplication.translate("MainWindow", u"Rotate Left", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.x_rotate_left.setText(QCoreApplication.translate("MainWindow", u"Rotate Left", None))
        self.x_rotate_right.setText(QCoreApplication.translate("MainWindow", u"Rotate Right", None))
        self.y_rotate_right.setText(QCoreApplication.translate("MainWindow", u"Rotate Right", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Translate Mesh", None))
        self.x_translate.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.y_translate.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.z_translate.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_translate.setText(QCoreApplication.translate("MainWindow", u"Translate", None))
        self.btn_saveas.setText(QCoreApplication.translate("MainWindow", u"Save As", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Methods To Compare", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Click to Add to Plot", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Newtownian", None))
        self.comp_newtonian.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Newtonian Prandtl Meyer", None))
        self.comp_npm.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Modified Newtonian", None))
        self.comp_mn.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Hankey Flat Surface", None))
        self.comp_hankey.setText("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Van Dyke Unified", None))
        self.comp_vandyke.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Busemann Second Order Theory", None))
        self.comp_busemann.setText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Angle of Attack Range (Degrees)", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Sideslip Angle (Degrees)", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Plot", None))
        self.Compare_PlotName.setItemText(0, QCoreApplication.translate("MainWindow", u"CL v CD", None))
        self.Compare_PlotName.setItemText(1, QCoreApplication.translate("MainWindow", u"AoA v CL", None))
        self.Compare_PlotName.setItemText(2, QCoreApplication.translate("MainWindow", u"AoA v CD", None))
        self.Compare_PlotName.setItemText(3, QCoreApplication.translate("MainWindow", u"AoA v Cy'", None))
        self.Compare_PlotName.setItemText(4, QCoreApplication.translate("MainWindow", u"AoA v Cx", None))
        self.Compare_PlotName.setItemText(5, QCoreApplication.translate("MainWindow", u"AoA v Cy", None))
        self.Compare_PlotName.setItemText(6, QCoreApplication.translate("MainWindow", u"AoA v Cz", None))
        self.Compare_PlotName.setItemText(7, QCoreApplication.translate("MainWindow", u"AoA v Cmx", None))
        self.Compare_PlotName.setItemText(8, QCoreApplication.translate("MainWindow", u"AoA v Cmy", None))
        self.Compare_PlotName.setItemText(9, QCoreApplication.translate("MainWindow", u"AoA v Cmz", None))
        self.Compare_PlotName.setItemText(10, QCoreApplication.translate("MainWindow", u"Sideslip v CL", None))
        self.Compare_PlotName.setItemText(11, QCoreApplication.translate("MainWindow", u"Sideslip v CD", None))
        self.Compare_PlotName.setItemText(12, QCoreApplication.translate("MainWindow", u"Sideslip v Cy'", None))
        self.Compare_PlotName.setItemText(13, QCoreApplication.translate("MainWindow", u"Sideslip v Cx", None))
        self.Compare_PlotName.setItemText(14, QCoreApplication.translate("MainWindow", u"Sideslip v Cy", None))
        self.Compare_PlotName.setItemText(15, QCoreApplication.translate("MainWindow", u"Sideslip v Cz", None))
        self.Compare_PlotName.setItemText(16, QCoreApplication.translate("MainWindow", u"Sideslip v Cmx", None))
        self.Compare_PlotName.setItemText(17, QCoreApplication.translate("MainWindow", u"Sideslip v Cmy", None))
        self.Compare_PlotName.setItemText(18, QCoreApplication.translate("MainWindow", u"Sideslip v Cmz", None))

        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Mach Number", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Ratio of Specific Heats (\u03b3)", None))
        self.compare_MachNumber.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.Compare_gamma.setText(QCoreApplication.translate("MainWindow", u"1.4", None))
        self.compare_vehiclestatus.setText(QCoreApplication.translate("MainWindow", u"No Vehicle Loaded", None))
        self.btn_compareMethods.setText(QCoreApplication.translate("MainWindow", u"Compare Methods", None))
        self.compare_export_csv.setText(QCoreApplication.translate("MainWindow", u"Export To .pkl", None))
        self.Title_Export_Lookup_Table.setText(QCoreApplication.translate("MainWindow", u"Export Lookup Table", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Mach Range", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Ratio of Specific Heats (\u03b3)", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Angle of Attack (Degrees)", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Sideslip Angle (Degrees)", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Compression Methods:", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Click to Add To Plot", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Newtonian Method", None))
        self.lookup_newtonian_check.setText("")
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Newtonian Prandtl Meyer", None))
        self.lookup_npm_check.setText("")
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Modified Newtonian", None))
        self.lookup_mn_check.setText("")
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Hankey Flat Surface", None))
        self.lookup_hankey_check.setText("")
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Van Dyke Unified", None))
        self.lookup_vandyke_check.setText("")
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Busemann Second Order Theory", None))
        self.lookup_busemann_check.setText("")
        self.label_66.setText("")
        self.label_67.setText("")
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"Expansion Methods:", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Click to Add to Plot", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"Newtonian Method", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"Newtonian Prandtl Meyer", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"Modified Newtonian", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Hankey Flat Surface", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Van Dyke Unified", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"Busemann Second Order Theory", None))
        self.lookup_exp_newtonian_check.setText("")
        self.lookup_exp_npm_check.setText("")
        self.lookup_exp_mn_check.setText("")
        self.lookup_exp_hankey_check.setText("")
        self.lookup_exp_vandyke_check.setText("")
        self.lookup_exp_busemann_check.setText("")
        self.label_68.setText("")
        self.label_69.setText("")
        self.btn_export_lookup.setText(QCoreApplication.translate("MainWindow", u"Save As .pkl", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Pressure Mapping", None))
        self.p_machNumber_label.setText(QCoreApplication.translate("MainWindow", u"Mach Number", None))
        self.p_gamma.setText(QCoreApplication.translate("MainWindow", u"Ratio Specific Heats", None))
        self.p_alpha_label.setText(QCoreApplication.translate("MainWindow", u"Angle of Attack (Degrees)", None))
        self.p_beta_label.setText(QCoreApplication.translate("MainWindow", u"Sideslip Angle (Degrees)", None))
        self.p_compression_label.setText(QCoreApplication.translate("MainWindow", u"Compression Method", None))
        self.p_compression_val.setItemText(0, QCoreApplication.translate("MainWindow", u"Newtonian Method", None))
        self.p_compression_val.setItemText(1, QCoreApplication.translate("MainWindow", u"NewTonian Prandtl Meyer", None))
        self.p_compression_val.setItemText(2, QCoreApplication.translate("MainWindow", u"Modified Newtonian", None))
        self.p_compression_val.setItemText(3, QCoreApplication.translate("MainWindow", u"Hankey Flat Surface", None))
        self.p_compression_val.setItemText(4, QCoreApplication.translate("MainWindow", u"Van Dyke Unified", None))
        self.p_compression_val.setItemText(5, QCoreApplication.translate("MainWindow", u"Busemann Second Order Theory", None))

        self.p_expansion_label.setText(QCoreApplication.translate("MainWindow", u"Expansion Method", None))
        self.p_expansion_val.setItemText(0, QCoreApplication.translate("MainWindow", u"Newtonian Method", None))
        self.p_expansion_val.setItemText(1, QCoreApplication.translate("MainWindow", u"Newtonian Prandtl Meyer", None))
        self.p_expansion_val.setItemText(2, QCoreApplication.translate("MainWindow", u"Modified Newtonian", None))
        self.p_expansion_val.setItemText(3, QCoreApplication.translate("MainWindow", u"Hankey Flat Surface", None))
        self.p_expansion_val.setItemText(4, QCoreApplication.translate("MainWindow", u"Van Dyke Unified", None))
        self.p_expansion_val.setItemText(5, QCoreApplication.translate("MainWindow", u"Busemann Second Order Theory", None))

        self.label_39.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>C<span style=\" vertical-align:sub;\">z</span>:</p></body></html>", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>C<span style=\" vertical-align:sub;\">x</span>:</p></body></html>", None))
        self.cyprime_val.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.cy_val.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>C<span style=\" vertical-align:sub;\">L</span>:</p></body></html>", None))
        self.cz_val.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>C<span style=\" vertical-align:sub;\">Y</span>':</p></body></html>", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>C<span style=\" vertical-align:sub;\">D</span>:</p></body></html>", None))
        self.cl_val.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.cd_val.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.cx_val.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>C<span style=\" vertical-align:sub;\">y</span>:</p></body></html>", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>C<span style=\" vertical-align:sub;\">Mx</span>:</p></body></html>", None))
        self.cmx_val.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>C<span style=\" vertical-align:sub;\">My</span>:</p></body></html>", None))
        self.cmy_val.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.cmz_val.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>C<span style=\" vertical-align:sub;\">Mz</span>:</p></body></html>", None))
        self.btn_plotpressure.setText(QCoreApplication.translate("MainWindow", u"Plot Pressure Map", None))
        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"S/HABP UNSW GUI", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0.1", None))
    # retranslateUi

