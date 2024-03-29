# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(663, 612)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.frame.setFont(font)
        self.frame.setStyleSheet("background-color: rgba(85, 170, 255, 180);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(450, 30, 83, 33))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.Button_start_1 = QtWidgets.QPushButton(self.frame_2)
        self.Button_start_1.setGeometry(QtCore.QRect(30, 20, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Button_start_1.setFont(font)
        self.Button_start_1.setStyleSheet("background-color: rgb(0, 85, 255);")
        self.Button_start_1.setObjectName("Button_start_1")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 90, 601, 371))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.screen = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.screen.setContentsMargins(0, 0, 0, 0)
        self.screen.setObjectName("screen")
        self.Button_start_2 = QtWidgets.QPushButton(self.frame_2)
        self.Button_start_2.setGeometry(QtCore.QRect(30, 500, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Button_start_2.setFont(font)
        self.Button_start_2.setStyleSheet("background-color: rgb(0, 85, 255);")
        self.Button_start_2.setObjectName("Button_start_2")
        self.Button_stop_1 = QtWidgets.QPushButton(self.frame_2)
        self.Button_stop_1.setGeometry(QtCore.QRect(210, 20, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Button_stop_1.setFont(font)
        self.Button_stop_1.setStyleSheet("background-color: rgb(0, 85, 255);")
        self.Button_stop_1.setObjectName("Button_stop_1")
        self.lineEdit_1 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_1.setGeometry(QtCore.QRect(250, 500, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_1.setFont(font)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "chart 1"))
        self.Button_start_1.setText(_translate("MainWindow", "Start Chart"))
        self.Button_start_2.setText(_translate("MainWindow", "Start update"))
        self.Button_stop_1.setText(_translate("MainWindow", "Stop Chart"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
