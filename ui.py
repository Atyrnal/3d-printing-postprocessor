# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.9.3
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
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QLabel,
    QLineEdit, QMainWindow, QPushButton, QRadioButton,
    QSizePolicy, QWidget)
import images_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 319)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 1px solid #ccc;\n"
"	border-radius: 2px;\n"
"	color: #000000;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 1px solid #0078d7;\n"
"	border-radius: 2px;\n"
"	background-color:  #cce8ff;\n"
"	color: #000000;\n"
"}")
        self.cancel = QPushButton(self.centralwidget)
        self.cancel.setObjectName(u"cancel")
        self.cancel.setGeometry(QRect(555, 290, 75, 20))
        self.cancel.setStyleSheet(u"")
        self.mainFrame = QFrame(self.centralwidget)
        self.mainFrame.setObjectName(u"mainFrame")
        self.mainFrame.setEnabled(True)
        self.mainFrame.setGeometry(QRect(0, 0, 640, 320))
        self.mainFrame.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.mainFrame.setFrameShape(QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QFrame.Raised)
        self.title = QLabel(self.mainFrame)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(220, 20, 400, 40))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(19)
        self.title.setFont(font)
        self.title.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.title.setAlignment(Qt.AlignCenter)
        self.nameInput = QLineEdit(self.mainFrame)
        self.nameInput.setObjectName(u"nameInput")
        self.nameInput.setGeometry(QRect(30, 130, 270, 20))
        self.nameInput.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"padding: 2px;\n"
"border-radius: 2px;")
        self.emailInput = QLineEdit(self.mainFrame)
        self.emailInput.setObjectName(u"emailInput")
        self.emailInput.setGeometry(QRect(30, 165, 270, 20))
        self.emailInput.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 2px;\n"
"padding: 2px;")
        self.filamentOwner = QGroupBox(self.mainFrame)
        self.filamentOwner.setObjectName(u"filamentOwner")
        self.filamentOwner.setGeometry(QRect(30, 200, 270, 50))
        self.filamentOwner.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.personal = QRadioButton(self.filamentOwner)
        self.personal.setObjectName(u"personal")
        self.personal.setGeometry(QRect(150, 20, 90, 18))
        self.personal.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.mkspace = QRadioButton(self.filamentOwner)
        self.mkspace.setObjectName(u"mkspace")
        self.mkspace.setGeometry(QRect(30, 20, 90, 18))
        self.mkspace.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.mkspace.setChecked(True)
        self.ImgLabel = QLabel(self.mainFrame)
        self.ImgLabel.setObjectName(u"ImgLabel")
        self.ImgLabel.setGeometry(QRect(10, 10, 250, 80))
        self.ImgLabel.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.ImgLabel.setPixmap(QPixmap(u":/svg/UMassAmherst.svg"))
        self.ImgLabel.setScaledContents(True)
        self.printInfoGroup = QGroupBox(self.mainFrame)
        self.printInfoGroup.setObjectName(u"printInfoGroup")
        self.printInfoGroup.setGeometry(QRect(325, 125, 285, 125))
        self.printInfoGroup.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.nameInfo = QLabel(self.printInfoGroup)
        self.nameInfo.setObjectName(u"nameInfo")
        self.nameInfo.setGeometry(QRect(10, 15, 250, 15))
        font1 = QFont()
        font1.setPointSize(8)
        self.nameInfo.setFont(font1)
        self.nameInfo.setText(u"Name: ERR")
        self.nameInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.printerInfo = QLabel(self.printInfoGroup)
        self.printerInfo.setObjectName(u"printerInfo")
        self.printerInfo.setGeometry(QRect(10, 32, 265, 15))
        self.printerInfo.setFont(font1)
        self.printerInfo.setText(u"Printer: ERR")
        self.printerInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.printInfo = QLabel(self.printInfoGroup)
        self.printInfo.setObjectName(u"printInfo")
        self.printInfo.setGeometry(QRect(10, 66, 250, 15))
        self.printInfo.setFont(font1)
        self.printInfo.setText(u"Print Settings: ERR")
        self.printInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.filamentInfo = QLabel(self.printInfoGroup)
        self.filamentInfo.setObjectName(u"filamentInfo")
        self.filamentInfo.setGeometry(QRect(10, 49, 250, 15))
        self.filamentInfo.setFont(font1)
        self.filamentInfo.setText(u"Filament: ERR")
        self.filamentInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.weightInfo = QLabel(self.printInfoGroup)
        self.weightInfo.setObjectName(u"weightInfo")
        self.weightInfo.setGeometry(QRect(10, 83, 250, 15))
        self.weightInfo.setFont(font1)
        self.weightInfo.setText(u"Weight: ERRg")
        self.weightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.durationInfo = QLabel(self.printInfoGroup)
        self.durationInfo.setObjectName(u"durationInfo")
        self.durationInfo.setGeometry(QRect(10, 100, 250, 15))
        self.durationInfo.setFont(font1)
        self.durationInfo.setText(u"Duration: ERR")
        self.durationInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.error = QLabel(self.mainFrame)
        self.error.setObjectName(u"error")
        self.error.setEnabled(True)
        self.error.setGeometry(QRect(0, 265, 640, 15))
        self.error.setFont(font1)
        self.error.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.error.setAlignment(Qt.AlignCenter)
        self.bg = QFrame(self.centralwidget)
        self.bg.setObjectName(u"bg")
        self.bg.setGeometry(QRect(0, 0, 640, 320))
        self.bg.setStyleSheet(u"background-color: rgb(129, 28, 28);")
        self.bg.setFrameShape(QFrame.StyledPanel)
        self.bg.setFrameShadow(QFrame.Raised)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setEnabled(True)
        self.frame.setGeometry(QRect(0, 0, 640, 320))
        self.frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.submit = QPushButton(self.centralwidget)
        self.submit.setObjectName(u"submit")
        self.submit.setGeometry(QRect(10, 290, 75, 20))
        self.submit.setStyleSheet(u"")
        MainWindow.setCentralWidget(self.centralwidget)
        self.frame.raise_()
        self.bg.raise_()
        self.mainFrame.raise_()
        self.cancel.raise_()
        self.submit.raise_()
        QWidget.setTabOrder(self.nameInput, self.emailInput)
        QWidget.setTabOrder(self.emailInput, self.mkspace)
        QWidget.setTabOrder(self.mkspace, self.personal)
        QWidget.setTabOrder(self.personal, self.cancel)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.cancel.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"Campus Makerspace 3D Printing Form", None))
        self.nameInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Full Name", None))
        self.emailInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"UMass Email", None))
        self.filamentOwner.setTitle(QCoreApplication.translate("MainWindow", u"Filament Provider", None))
        self.personal.setText(QCoreApplication.translate("MainWindow", u"Personal", None))
        self.mkspace.setText(QCoreApplication.translate("MainWindow", u"Makerspace", None))
        self.ImgLabel.setText("")
        self.printInfoGroup.setTitle(QCoreApplication.translate("MainWindow", u"Print Info", None))
        self.error.setText("")
        self.submit.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
    # retranslateUi

