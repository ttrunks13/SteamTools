# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo_options.ui'
#
# Created: Fri Apr 06 14:53:13 2012
#      by: PyQt4 UI code generator 4.9
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DemoOptions(object):
    def setupUi(self, DemoOptions):
        DemoOptions.setObjectName(_fromUtf8("DemoOptions"))
        DemoOptions.setWindowModality(QtCore.Qt.ApplicationModal)
        DemoOptions.resize(320, 250)
        DemoOptions.setMinimumSize(QtCore.QSize(320, 250))
        DemoOptions.setMaximumSize(QtCore.QSize(320, 250))
        DemoOptions.setStyleSheet(_fromUtf8("QListWidget::item:hover, QTreeWidget::item:hover {\n"
"    background-color: none;\n"
"  border:none;\n"
"color:white;\n"
"}\n"
"QListWidget::item:selected, QTreeWidget::item:selected {\n"
"  border:none;\n"
"    background-color: rgb(49, 65, 89);\n"
"color:white;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"     background-color: #4d4b48;\n"
"     color: rgb(165,165,165);\n"
"     padding:3px 0 3px 5px;\n"
"     border-left:1px solid rgba(0,0,0, 40);border-right:none;border-top:none;border-bottom:none;\n"
"text-transform:uppercase;\n"
"    font: 10px \"Arial\";\n"
" }\n"
"QHeaderView::section:hover {\n"
"     color: rgb(255,255,255);\n"
" }\n"
"\n"
" /* style the sort indicator */\n"
" QHeaderView::down-arrow {\n"
"    image: url(:/icons/icons/steam/icon_down_default.tga);\n"
" }\n"
"\n"
" QHeaderView::up-arrow {\n"
"    image: url(:/icons/icons/steam/icon_up_default.tga);\n"
" }\n"
"\n"
"\n"
"QScrollBar {\n"
"background: rgba(215, 214, 213, 10)/*#5d5a58*/;\n"
"border:none;\n"
"border-style:none;\n"
"}\n"
"QScrollBar:horizontal {\n"
"         \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(50, 50, 50, 255), stop:0.5 rgba(0, 0, 0, 0));\n"
"         height: 15px;\n"
"         margin: 0px 23px 1 23px;\n"
"     }\n"
"\n"
"     QScrollBar::handle:horizontal {\n"
"         background:  #615f5c;\n"
"         min-width: 20px;\n"
"         border: 1px solid #615f5c;\n"
"         border-width: 1px;\n"
"         border-radius: 2px;\n"
"         image: url(:/icons/icons/steam/icon_scroll_handle.tga);\n"
"     }\n"
"\n"
"     QScrollBar::handle:horizontal:hover {\n"
"         background: #64615e;\n"
"         border: 1px solid #64615e;\n"
"     }\n"
"     QScrollBar::handle:vertical:hover {\n"
"         background: #64615e;\n"
"         border: 1px solid #64615e;\n"
"     }\n"
"\n"
"     QScrollBar::add-line:horizontal {\n"
"    image: url(:/icons/icons/steam/icon_right_default.tga);\n"
"         background: #5d5a58;\n"
"         width: 19px;\n"
"    margin:0px 1px 1px 0; \n"
"         subcontrol-position: right;\n"
"         subcontrol-origin: margin;\n"
"         border: 1px solid #5e5b58;\n"
"     border-width: 1px;\n"
"     border-radius: 2px;\n"
"     }\n"
"\n"
"     QScrollBar::sub-line:horizontal {\n"
"    image: url(:/icons/icons/steam/icon_left_default.tga);\n"
"         background: #5e5b58;\n"
"         width: 19px;\n"
"         subcontrol-position: top left;\n"
"         subcontrol-origin: margin;\n"
"       border: 1px solid #5d5a58;\n"
"margin:0 0 1px 1px; \n"
"     border-width: 1px;\n"
"     border-radius: 2px;\n"
"     }\n"
"\n"
"     QScrollBar::add-line:horizontal:hover {\n"
"         background: #64615e;\n"
"         border: 1px solid #64615e;\n"
"     }\n"
"     QScrollBar::sub-line:horizontal:hover {\n"
"         background: #64615e;\n"
"         border: 1px solid #64615e;\n"
"     }\n"
"\n"
"     QScrollBar:left-arrow:horizontal, QScrollBar::right-arrow:horizontal {\n"
"     }\n"
"\n"
"     QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"         background: none;\n"
"     }\n"
"\n"
"\n"
"\n"
"\n"
"QScrollBar:vertical {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.5 rgba(10, 10, 10, 0), stop:1 rgba(50, 50, 50, 255));\n"
"         width: 15px;\n"
"         margin: 23px 1px 24px 0;\n"
"     }\n"
"\n"
"     QScrollBar::handle:vertical {\n"
"         background:  #615f5c;\n"
"         min-height: 20px;\n"
"         border: 1px solid #615f5c;\n"
"         border-width: 1px;\n"
"     border-radius: 2px;\n"
"image: url(:/icons/icons/steam/icon_scroll_handle.tga);\n"
"     }\n"
"\n"
"     QScrollBar::add-line:vertical {\n"
"         background: #5d5a58;\n"
"         height: 19px;\n"
"    margin:1px 1px 1px 0; \n"
"         subcontrol-position: bottom;\n"
"         subcontrol-origin: margin;\n"
"         border: 1px solid #5d5a58;\n"
"     border-width: 1px;\n"
"     border-radius: 2px;\n"
"    image: url(:/icons/icons/steam/icon_down_default.tga);\n"
"     }\n"
"\n"
"     QScrollBar::add-line:vertical:hover {\n"
"         background: #64615e;\n"
"         border: 1px solid #64615e;\n"
"     }\n"
"\n"
"\n"
"     QScrollBar::sub-line:vertical {\n"
"         background: #5d5a58;\n"
"         height: 19px;\n"
"         subcontrol-position: top left;\n"
"         subcontrol-origin: margin;\n"
"       border: 1px solid #5d5a58;\n"
"margin:1px 1px 0 0 ; \n"
"     border-width: 1px;\n"
"     border-radius: 2px;\n"
"    image: url(:/icons/icons/steam/icon_up_default.tga);\n"
"     }\n"
"     QScrollBar::sub-line:vertical:hover {\n"
"         background: #64615e;\n"
"         border: 1px solid #64615e;\n"
"     }\n"
"     QScrollBar:up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"         width: 3px;\n"
"         height: 3px;\n"
"     }\n"
"\n"
"     QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"         background: none;\n"
"\n"
"     }\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
" QPushButton {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(92, 89, 86, 255), stop:1 rgba(64, 59, 60, 255));\n"
"     border-style: solid;\n"
"     border-width: 1px;\n"
"     border-radius: 2px;\n"
"     border-color: rgba(112,109, 105, 255);\n"
"    color: rgb(218, 218, 218);\n"
"    text-align:left;\n"
"    padding-left:5px;\n"
"padding-right:20px;\n"
"    text-transform:uppercase;\n"
"    font: 10px \"Arial\";\n"
"height:23px;\n"
" }\n"
" QPushButton:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(103,100,97, 255), stop:1 rgba(64, 59, 60, 255));\n"
"     border-color: rgba(153,147,141, 255);\n"
" }\n"
" QPushButton:disabled {\n"
"    background-color:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(103,100,97, 255), stop:1 rgba(64, 59, 60, 255));\n"
"     border-color:#666666;\n"
"color:#666666;\n"
" }\n"
"QLabel#bar{background-color:#6b6865;}\n"
" QPushButton#btn_close, QPushButton#btn_minimize {\n"
"     border-width: 0px;\n"
"    color: rgb(218, 218, 218);\n"
"    text-align:left;\n"
"    padding-left:0px;\n"
"background:none;\n"
" }\n"
"\n"
"QMessageBox, QInputDialog {background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(92, 89, 86, 255), stop:1 rgba(64, 59, 60, 255));}\n"
" QPushButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(56,54,53, 255), stop:1 rgba(73,71,69, 255));\n"
"     border-color: rgba(112,109,105, 255);\n"
" }\n"
"\n"
"QWidget {color: rgba(209, 207, 205, 255);}\n"
"QWidget:disabled {color: rgba(209, 207, 205, 100);}\n"
"\n"
"QGroupBox {border:none;}\n"
"\n"
"QLineEdit {\n"
"    background-color: rgba(57,55,54, 255);\n"
"     border-style: solid;\n"
"     border-width: 1px;\n"
"     border-radius: 2px;\n"
"     border-color: rgba(112,109, 105, 255);\n"
"padding-left:5px;\n"
"    color: rgb(218, 218, 218);\n"
" }\n"
"\n"
"QComboBox {\n"
"     border: 1px solid #807c78;\n"
"     border-radius: 2px;\n"
"     padding: 1px 1px 1px 3px;\n"
"     min-width: 6em;\n"
" }\n"
"\n"
" QComboBox:hover {\n"
"\n"
"    background:  #4a4846;\n"
" }\n"
" QComboBox:editable {\n"
"\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #5c5956, stop:1 #4a4846);\n"
" }\n"
"\n"
" QComboBox:!editable, QComboBox::drop-down:editable {\n"
"\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #5c5956, stop:1 #4a4846);\n"
" }\n"
"\n"
" /* QComboBox gets the \"on\" state when the popup is open */\n"
" QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #5c5956, stop:1 #4a4846);\n"
" }\n"
"\n"
" QComboBox:on { /* shift the text when the popup opens */\n"
" }\n"
"\n"
" QComboBox::drop-down {\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 20px;\n"
"    height:15px;\n"
"    margin-top:3px;\n"
"     border-left-width: 1px;\n"
"     border-left-color: #807c78;\n"
"     border-left-style: solid; /* just a single line */\n"
"     border-top-right-radius: 2px; /* same radius as the QComboBox */\n"
"     border-bottom-right-radius: 2px;\n"
" }\n"
"\n"
" QComboBox::down-arrow {\n"
"    right: 1px;\n"
"     image: url(:/icons/dropdown.png);\n"
" }\n"
"\n"
" QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
" }\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    margin-top:1px;\n"
"     border: 1px solid #807c78;\n"
"     border-radius: 2px;\n"
"     background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #5c5956, stop:1 #4a4846);\n"
" }\n"
"QComboBox QAbstractItem {\n"
"margin:5px;\n"
" }\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
" QListWidget,QPlainTextEdit, QTreeWidget {\n"
"    background-image: url(:/icons/viewbg.jpg);\n"
"background-repeat:repeat-x;\n"
"/*    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(56,54,53, 255), stop:1 rgba(73,71,69, 255));*/\n"
"     border-style: solid;\n"
"     border-width: 1px;\n"
"     border-radius: 2px;\n"
"     border-color: rgba(112,109, 105, 255);\n"
"    color: rgb(218, 218, 218);\n"
"background-color:#242322;\n"
"background-attachment:fixed;\n"
" }\n"
"QTreeWidget { \n"
"\n"
"}\n"
"\n"
"QTabWidget::pane { /* The tab widget frame */\n"
"    border-color: #6b6865; /* same as the pane color */\n"
"    border-top:0px solid;\n"
"\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    left: 0px; /* move to the right by 5px */\n"
"}\n"
"\n"
"/* Style the tab using the tab sub-control. Note that it reads QTabBar _not_ QTabWidget */\n"
"QTabBar::tab {\n"
"    background-color:#4a4846;\n"
"    border-bottom-color: #6b6865; /* same as the pane color */\n"
"    border-bottom:0px solid;\n"
"    min-width: 5px;\n"
"    padding: 3px 20px 3px 8px;\n"
"    margin-right:2px;\n"
"    margin-bottom:2px;\n"
"    text-transform:uppercase;\n"
"    font: 10px \"Arial\";\n"
"}\n"
"\n"
"QTabBar::tab:hover {\n"
"background-color:#666360;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(107, 104, 101, 255), stop:1 rgba(56, 54, 53, 255));\n"
"    margin-bottom:0px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"\n"
"}"))
        DemoOptions.setModal(True)
        self.buttonBox = QtGui.QDialogButtonBox(DemoOptions)
        self.buttonBox.setGeometry(QtCore.QRect(30, 190, 261, 23))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.checkBox = QtGui.QCheckBox(DemoOptions)
        self.checkBox.setGeometry(QtCore.QRect(30, 50, 260, 17))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.checkBox_2 = QtGui.QCheckBox(DemoOptions)
        self.checkBox_2.setGeometry(QtCore.QRect(30, 70, 260, 17))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.checkBox_3 = QtGui.QCheckBox(DemoOptions)
        self.checkBox_3.setGeometry(QtCore.QRect(30, 90, 260, 17))
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.comboBox = QtGui.QComboBox(DemoOptions)
        self.comboBox.setGeometry(QtCore.QRect(30, 130, 261, 23))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.BGIMG = QtGui.QLabel(DemoOptions)
        self.BGIMG.setGeometry(QtCore.QRect(0, 0, 320, 250))
        self.BGIMG.setText(_fromUtf8(""))
        self.BGIMG.setPixmap(QtGui.QPixmap(_fromUtf8(":/icons/demo_options.png")))
        self.BGIMG.setScaledContents(False)
        self.BGIMG.setObjectName(_fromUtf8("BGIMG"))
        self.apptitle = QtGui.QLabel(DemoOptions)
        self.apptitle.setGeometry(QtCore.QRect(10, 10, 301, 30))
        self.apptitle.setMargin(0)
        self.apptitle.setIndent(10)
        self.apptitle.setObjectName(_fromUtf8("apptitle"))

        self.retranslateUi(DemoOptions)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DemoOptions.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DemoOptions.reject)
        QtCore.QMetaObject.connectSlotsByName(DemoOptions)

    def retranslateUi(self, DemoOptions):
        DemoOptions.setWindowTitle(QtGui.QApplication.translate("DemoOptions", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("DemoOptions", "-sw (Start Windowed Mode)", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_2.setText(QtGui.QApplication.translate("DemoOptions", "-novid", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_3.setText(QtGui.QApplication.translate("DemoOptions", "-console", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(0, QtGui.QApplication.translate("DemoOptions", "800 x 600 (4:3)", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(1, QtGui.QApplication.translate("DemoOptions", "1024 x 768 (4:3)", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(2, QtGui.QApplication.translate("DemoOptions", "1024×576 (16:9)", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(3, QtGui.QApplication.translate("DemoOptions", "1280×720 (16:9)", None, QtGui.QApplication.UnicodeUTF8))
        self.apptitle.setText(QtGui.QApplication.translate("DemoOptions", "Demo Launch Options", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
