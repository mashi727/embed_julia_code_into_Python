# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'graphPlotUi.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QMainWindow, QMenuBar, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTreeView,
    QVBoxLayout, QWidget)

from pyqtgraph.opengl import GLViewWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1638, 967)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.quitButton = QPushButton(self.centralwidget)
        self.quitButton.setObjectName(u"quitButton")
        self.quitButton.setMinimumSize(QSize(0, 40))
        self.quitButton.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setFamilies([u"HackGen35 Console NFJ"])
        font.setPointSize(17)
        self.quitButton.setFont(font)

        self.horizontalLayout.addWidget(self.quitButton)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.openGLWidget = GLViewWidget(self.centralwidget)
        self.openGLWidget.setObjectName(u"openGLWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.openGLWidget.sizePolicy().hasHeightForWidth())
        self.openGLWidget.setSizePolicy(sizePolicy)
        self.openGLWidget.setMinimumSize(QSize(1000, 0))

        self.horizontalLayout_4.addWidget(self.openGLWidget)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.treeView = QTreeView(self.centralwidget)
        self.treeView.setObjectName(u"treeView")
        sizePolicy.setHeightForWidth(self.treeView.sizePolicy().hasHeightForWidth())
        self.treeView.setSizePolicy(sizePolicy)
        self.treeView.setMinimumSize(QSize(600, 0))
        self.treeView.setMaximumSize(QSize(500, 16777215))
        font1 = QFont()
        font1.setFamilies([u"HackGen35 Console NFJ"])
        font1.setPointSize(14)
        self.treeView.setFont(font1)

        self.verticalLayout.addWidget(self.treeView)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.clearButton = QPushButton(self.centralwidget)
        self.clearButton.setObjectName(u"clearButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.clearButton.sizePolicy().hasHeightForWidth())
        self.clearButton.setSizePolicy(sizePolicy1)
        self.clearButton.setMinimumSize(QSize(125, 25))
        self.clearButton.setMaximumSize(QSize(125, 30))
        self.clearButton.setFont(font)

        self.horizontalLayout_3.addWidget(self.clearButton)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.codeView = QPlainTextEdit(self.centralwidget)
        self.codeView.setObjectName(u"codeView")
        sizePolicy.setHeightForWidth(self.codeView.sizePolicy().hasHeightForWidth())
        self.codeView.setSizePolicy(sizePolicy)
        self.codeView.setMinimumSize(QSize(600, 450))
        self.codeView.setMaximumSize(QSize(600, 16777215))
        font2 = QFont()
        font2.setFamilies([u"HackGen35 Console NFJ"])
        font2.setPointSize(20)
        self.codeView.setFont(font2)

        self.verticalLayout.addWidget(self.codeView)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.plotButton = QPushButton(self.centralwidget)
        self.plotButton.setObjectName(u"plotButton")
        sizePolicy1.setHeightForWidth(self.plotButton.sizePolicy().hasHeightForWidth())
        self.plotButton.setSizePolicy(sizePolicy1)
        self.plotButton.setMinimumSize(QSize(70, 40))
        self.plotButton.setMaximumSize(QSize(70, 40))
        self.plotButton.setFont(font)

        self.horizontalLayout_2.addWidget(self.plotButton)

        self.saveButton = QPushButton(self.centralwidget)
        self.saveButton.setObjectName(u"saveButton")
        sizePolicy1.setHeightForWidth(self.saveButton.sizePolicy().hasHeightForWidth())
        self.saveButton.setSizePolicy(sizePolicy1)
        self.saveButton.setMinimumSize(QSize(70, 40))
        self.saveButton.setMaximumSize(QSize(70, 40))
        self.saveButton.setFont(font)

        self.horizontalLayout_2.addWidget(self.saveButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_4.addLayout(self.verticalLayout)


        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1638, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.quitButton.clicked.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.quitButton.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.clearButton.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.plotButton.setText(QCoreApplication.translate("MainWindow", u"Plot", None))
        self.saveButton.setText(QCoreApplication.translate("MainWindow", u"Save", None))
    # retranslateUi

