# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(353, 294)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.img_preview = ScreenShotPreview(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img_preview.sizePolicy().hasHeightForWidth())
        self.img_preview.setSizePolicy(sizePolicy)
        self.img_preview.setObjectName("img_preview")
        self.verticalLayout.addWidget(self.img_preview)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 353, 28))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuCapture = QtWidgets.QMenu(self.menubar)
        self.menuCapture.setObjectName("menuCapture")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.ActionMenuEditCopy = QtWidgets.QAction(MainWindow)
        self.ActionMenuEditCopy.setObjectName("ActionMenuEditCopy")
        self.ActionMenuHelpAbout = QtWidgets.QAction(MainWindow)
        self.ActionMenuHelpAbout.setObjectName("ActionMenuHelpAbout")
        self.ActionMenuFileSave = QtWidgets.QAction(MainWindow)
        self.ActionMenuFileSave.setObjectName("ActionMenuFileSave")
        self.ActionMenuFileSaveAs = QtWidgets.QAction(MainWindow)
        self.ActionMenuFileSaveAs.setObjectName("ActionMenuFileSaveAs")
        self.ActionMenuFilePrint = QtWidgets.QAction(MainWindow)
        self.ActionMenuFilePrint.setObjectName("ActionMenuFilePrint")
        self.ActionMenuFilePrintSetup = QtWidgets.QAction(MainWindow)
        self.ActionMenuFilePrintSetup.setObjectName("ActionMenuFilePrintSetup")
        self.ActionMenuFileClose = QtWidgets.QAction(MainWindow)
        self.ActionMenuFileClose.setObjectName("ActionMenuFileClose")
        self.ActionMenuCaptureSelection = QtWidgets.QAction(MainWindow)
        self.ActionMenuCaptureSelection.setEnabled(False)
        self.ActionMenuCaptureSelection.setObjectName("ActionMenuCaptureSelection")
        self.ActionMenuCaptureWindow = QtWidgets.QAction(MainWindow)
        self.ActionMenuCaptureWindow.setEnabled(False)
        self.ActionMenuCaptureWindow.setObjectName("ActionMenuCaptureWindow")
        self.ActionMenuCaptureScreen = QtWidgets.QAction(MainWindow)
        self.ActionMenuCaptureScreen.setObjectName("ActionMenuCaptureScreen")
        self.ActionMenuCaptureTimedScreen = QtWidgets.QAction(MainWindow)
        self.ActionMenuCaptureTimedScreen.setEnabled(False)
        self.ActionMenuCaptureTimedScreen.setObjectName("ActionMenuCaptureTimedScreen")
        self.menuFile.addAction(self.ActionMenuFileClose)
        self.menuFile.addAction(self.ActionMenuFileSave)
        self.menuFile.addAction(self.ActionMenuFileSaveAs)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.ActionMenuFilePrint)
        self.menuFile.addAction(self.ActionMenuFilePrintSetup)
        self.menuEdit.addAction(self.ActionMenuEditCopy)
        self.menuCapture.addAction(self.ActionMenuCaptureSelection)
        self.menuCapture.addAction(self.ActionMenuCaptureWindow)
        self.menuCapture.addAction(self.ActionMenuCaptureScreen)
        self.menuCapture.addAction(self.ActionMenuCaptureTimedScreen)
        self.menuHelp.addAction(self.ActionMenuHelpAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuCapture.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Grab"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuCapture.setTitle(_translate("MainWindow", "Capture"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.ActionMenuEditCopy.setText(_translate("MainWindow", "Copy"))
        self.ActionMenuEditCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.ActionMenuHelpAbout.setText(_translate("MainWindow", "About"))
        self.ActionMenuFileSave.setText(_translate("MainWindow", "Save"))
        self.ActionMenuFileSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.ActionMenuFileSaveAs.setText(_translate("MainWindow", "Save As"))
        self.ActionMenuFileSaveAs.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.ActionMenuFilePrint.setText(_translate("MainWindow", "Print"))
        self.ActionMenuFilePrint.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.ActionMenuFilePrintSetup.setText(_translate("MainWindow", "Print Setup"))
        self.ActionMenuFilePrintSetup.setShortcut(_translate("MainWindow", "Ctrl+Shift+P"))
        self.ActionMenuFileClose.setText(_translate("MainWindow", "Close"))
        self.ActionMenuFileClose.setShortcut(_translate("MainWindow", "Ctrl+W"))
        self.ActionMenuCaptureSelection.setText(_translate("MainWindow", "Selection"))
        self.ActionMenuCaptureSelection.setShortcut(_translate("MainWindow", "Ctrl+Shift+A"))
        self.ActionMenuCaptureWindow.setText(_translate("MainWindow", "Window"))
        self.ActionMenuCaptureWindow.setShortcut(_translate("MainWindow", "Ctrl+Shift+W"))
        self.ActionMenuCaptureScreen.setText(_translate("MainWindow", "Screen"))
        self.ActionMenuCaptureScreen.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.ActionMenuCaptureTimedScreen.setText(_translate("MainWindow", "Timed Screen"))
        self.ActionMenuCaptureTimedScreen.setShortcut(_translate("MainWindow", "Ctrl+Shift+Z"))
from widget_screenshot_preview import ScreenShotPreview
