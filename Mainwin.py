# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Mainwin.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class Ui_Form(object):

    def __init__(self):
        self.inputtext = None
        self.outputLabel = None
        self.graphCanvas = None
        self.tipsLabel = None
        self.pushButton = None
        self.centralwidget = None

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(700, 700)
        Form.setMinimumSize(700, 700)
        Form.setMaximumSize(700, 700)
        self.pushButton = QtWidgets.QPushButton(Form, text="是欧拉图吗？")
        self.pushButton.setGeometry(QtCore.QRect(450, 270, 99, 28))
        self.pushButton.setIconSize(QtCore.QSize(20, 20))
        self.pushButton.setObjectName("pushButton")
        self.tipsLabel = QtWidgets.QLabel(Form)
        self.tipsLabel.setGeometry(QtCore.QRect(350, 30, 291, 191))
        self.tipsLabel.setStyleSheet("font: 75 9pt \"微软雅黑\";")
        self.tipsLabel.setObjectName("tipsLabel")
        self.graphCanvas = FigureCanvas(Figure(figsize=(3, 3)))
        self.graphCanvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.graphCanvas.updateGeometry()
        self.graphCanvas.setParent(Form)
        self.graphCanvas.move(30, 360)
        self.outputLabel = QtWidgets.QLabel(Form)
        self.outputLabel.setGeometry(QtCore.QRect(350, 360, 300, 300))
        self.outputLabel.setText("")
        self.outputLabel.setObjectName("outputLabel")
        self.inputtext = QtWidgets.QTextEdit(Form)
        self.inputtext.setGeometry(QtCore.QRect(30, 30, 300, 300))
        self.inputtext.setObjectName("inputtext")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.inputtext, self.pushButton)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "isEulerGraph"))
        self.pushButton.setText(_translate("Form", "是欧拉图吗？"))
        self.tipsLabel.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" "
                                                  "font-size:11pt;\">请在左边的文本框中按行输入</span></p><p "
                                                  "align=\"center\"><span style=\" "
                                                  "font-size:11pt;\">一个表示图的邻接矩阵</span></p><p align=\"center\"><span "
                                                  "style=\" font-size:11pt;\">格式要求：矩阵元素以英文逗号分割，</span></p><p "
                                                  "align=\"center\"><span style=\" "
                                                  "font-size:11pt;\">每行行末标记英文逗号</span></p><p align=\"center\"><span "
                                                  "style=\" font-size:11pt;\">最后一行不写逗号</span></p></body></html>"))
        self.inputtext.setHtml(_translate("Form",
                                          "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                          "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                          "<html><head><meta name=\"qrichtext\" content=\"1\" /><style "
                                          "type=\"text/css\">\n"
                                          "p, li { white-space: pre-wrap; }\n"
                                          "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; "
                                          "font-weight:400; font-style:normal;\">\n"
                                          "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; "
                                          "margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0,1,0,0,0;</p>\n"
                                          "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; "
                                          "margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0,0,1,0,0;</p>\n"
                                          "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; "
                                          "margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0,0,0,1,0;</p>\n"
                                          "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; "
                                          "margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0,0,0,0,1;</p>\n"
                                          "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; "
                                          "margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1,0,0,0,"
                                          "0</p></body></html>"))
