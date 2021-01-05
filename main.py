# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
import win32api
from PyQt5.QtWidgets import *
from draw_box import *


class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(569, 542)
        self.input = ' '
        self.value_of_box_width = 50
        self.value_of_box_height = 50
        self.value_of_zoom_width = 125
        self.value_of_zoom_height = 125

        self.value_of_line_width = 2
        self.value_of_R = 0
        self.value_of_G = 255
        self.value_of_B = 0
        self.value_of_zoom_line_width = 4

        self.pushButton = QtWidgets.QPushButton(MainWindow)
        self.pushButton.setGeometry(QtCore.QRect(300, 450, 101, 51))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(130, 50, 81, 31))
        self.label.setObjectName("label")
        self.box_width = QtWidgets.QTextEdit(MainWindow)
        self.box_width.setGeometry(QtCore.QRect(120, 90, 91, 51))
        self.box_width.setObjectName("box_width")
        self.box_height = QtWidgets.QTextEdit(MainWindow)
        self.box_height.setGeometry(QtCore.QRect(260, 90, 91, 51))
        self.box_height.setObjectName("box_height")
        self.box_height_2 = QtWidgets.QLabel(MainWindow)
        self.box_height_2.setGeometry(QtCore.QRect(270, 50, 81, 31))
        self.box_height_2.setObjectName("box_height_2")
        self.label_3 = QtWidgets.QLabel(MainWindow)
        self.label_3.setGeometry(QtCore.QRect(270, 170, 81, 31))
        self.label_3.setObjectName("label_3")
        self.zoom_width = QtWidgets.QTextEdit(MainWindow)
        self.zoom_width.setGeometry(QtCore.QRect(120, 210, 91, 51))
        self.zoom_width.setObjectName("zoom_width")
        self.label_4 = QtWidgets.QLabel(MainWindow)
        self.label_4.setGeometry(QtCore.QRect(130, 170, 81, 31))
        self.label_4.setObjectName("label_4")
        self.zoom_height = QtWidgets.QTextEdit(MainWindow)
        self.zoom_height.setGeometry(QtCore.QRect(260, 210, 91, 51))
        self.zoom_height.setObjectName("zoom_height")
        self.textBrowser = QtWidgets.QTextBrowser(MainWindow)
        self.textBrowser.setGeometry(QtCore.QRect(20, 370, 491, 61))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_2 = QtWidgets.QPushButton(MainWindow)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 450, 101, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_6 = QtWidgets.QLabel(MainWindow)
        self.label_6.setGeometry(QtCore.QRect(20, 100, 81, 31))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(MainWindow)
        self.label_7.setGeometry(QtCore.QRect(20, 220, 81, 31))
        self.label_7.setObjectName("label_7")
        self.line_width = QtWidgets.QTextEdit(MainWindow)
        self.line_width.setGeometry(QtCore.QRect(400, 90, 91, 51))
        self.line_width.setObjectName("line_width")
        self.label_9 = QtWidgets.QLabel(MainWindow)
        self.label_9.setGeometry(QtCore.QRect(410, 50, 81, 31))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(MainWindow)
        self.label_10.setGeometry(QtCore.QRect(410, 170, 81, 31))
        self.label_10.setObjectName("label_10")
        self.line_width_2 = QtWidgets.QTextEdit(MainWindow)
        self.line_width_2.setGeometry(QtCore.QRect(400, 210, 91, 51))
        self.line_width_2.setObjectName("line_width_2")
        self.label_8 = QtWidgets.QLabel(MainWindow)
        self.label_8.setGeometry(QtCore.QRect(20, 310, 81, 31))
        self.label_8.setObjectName("label_8")
        self.G = QtWidgets.QTextEdit(MainWindow)
        self.G.setGeometry(QtCore.QRect(260, 310, 91, 51))
        self.G.setObjectName("G")
        self.label_5 = QtWidgets.QLabel(MainWindow)
        self.label_5.setGeometry(QtCore.QRect(300, 270, 21, 31))
        self.label_5.setObjectName("label_5")
        self.R = QtWidgets.QTextEdit(MainWindow)
        self.R.setGeometry(QtCore.QRect(120, 310, 91, 51))
        self.R.setObjectName("R")
        self.label_11 = QtWidgets.QLabel(MainWindow)
        self.label_11.setGeometry(QtCore.QRect(440, 270, 21, 31))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(MainWindow)
        self.label_12.setGeometry(QtCore.QRect(160, 270, 31, 31))
        self.label_12.setObjectName("label_12")
        self.B = QtWidgets.QTextEdit(MainWindow)
        self.B.setGeometry(QtCore.QRect(400, 310, 91, 51))
        self.B.setObjectName("B")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        ############################################################
        # 将各按钮与事件关联
        ############################################################
        self.pushButton_2.clicked.connect(self.slot_btn_chooseDir)
        self.pushButton.clicked.connect(self.start)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "框选工具"))
        self.pushButton.setText(_translate("MainWindow", "开始运行"))
        self.label.setText(_translate("MainWindow", "box_width"))
        self.box_height_2.setText(_translate("MainWindow", "box_height"))
        self.label_3.setText(_translate("MainWindow", "zoom_height"))
        self.label_4.setText(_translate("MainWindow", "zoom_width"))
        self.pushButton_2.setText(_translate("MainWindow", "文件夹"))
        self.label_6.setText(_translate("MainWindow", "原始的大小"))
        self.label_7.setText(_translate("MainWindow", "缩放后的大小"))
        self.label_9.setText(_translate("MainWindow", "line_width"))
        self.label_10.setText(_translate("MainWindow", "line_width"))
        self.label_8.setText(_translate("MainWindow", "颜色"))
        self.label_5.setText(_translate("MainWindow", "G"))
        self.label_11.setText(_translate("MainWindow", "B"))
        self.label_12.setText(_translate("MainWindow", "R"))


        self.box_width.setText(_translate("MainWindow", str(self.value_of_box_width)))
        self.box_height.setText(_translate("MainWindow", str(self.value_of_box_height)))
        self.zoom_width.setText(_translate("MainWindow", str(self.value_of_zoom_width)))
        self.zoom_height.setText(_translate("MainWindow", str(self.value_of_zoom_height)))
        self.line_width.setText(_translate("MainWindow",str(self.value_of_line_width)))
        self.line_width_2.setText(_translate("MainWindow",str(self.value_of_zoom_line_width)))
        self.R.setText(_translate("MainWindow", str(self.value_of_R)))
        self.G.setText(_translate("MainWindow", str(self.value_of_G)))
        self.B.setText(_translate("MainWindow", str(self.value_of_B)))
        
    
    def slot_btn_chooseDir(self):
        dir_choose = QFileDialog.getExistingDirectory(self, "选取文件夹")
        _translate = QtCore.QCoreApplication.translate
        self.textBrowser.setText(_translate("MainWindow", dir_choose))
        self.input = dir_choose
    def start(self):
        print('start')
        self.value_of_box_width = int(self.box_width.toPlainText())
        self.value_of_box_height = int(self.box_height.toPlainText())
        self.value_of_zoom_width = int(self.zoom_width.toPlainText())
        self.value_of_zoom_height = int(self.zoom_height.toPlainText())
        self.value_of_line_width = int(self.line_width.toPlainText())
        self.value_of_zoom_line_width = int(self.line_width_2.toPlainText())
        self.value_of_R = int(self.R.toPlainText()) 
        self.value_of_G = int(self.G.toPlainText())
        self.value_of_B = int(self.B.toPlainText())
        draw_box_all(self.value_of_box_width,self.value_of_box_height,self.value_of_line_width,
        self.value_of_zoom_width,self.value_of_zoom_height,self.value_of_zoom_line_width,
        self.value_of_R, self.value_of_G,self.value_of_B,
        self.input
        )

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())