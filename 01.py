import sys

import numpy as np
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(700, 700)
        Form.setMinimumSize(700, 700)  # 修改代码
        Form.setMaximumSize(700, 700)  # 修改代码
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(450, 270, 99, 28))
        self.pushButton.setIconSize(QtCore.QSize(20, 20))
        self.pushButton.setObjectName("pushButton")
        self.tipsLabel = QtWidgets.QLabel(Form)
        self.tipsLabel.setGeometry(QtCore.QRect(350, 30, 291, 191))
        self.tipsLabel.setStyleSheet("font: 75 9pt \"微软雅黑\";")
        self.tipsLabel.setObjectName("tipsLabel")
        self.graphCanvas = FigureCanvas(Figure(figsize=(3, 3)))
        self.graphCanvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)  # 修改代码
        self.graphCanvas.updateGeometry()  # 修改代码
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
        self.tipsLabel.setText(_translate("Form",
                                          "<html><head/><body><p align=\"center\"><span style=\"\n"
                                          "                    font-size:12pt;\">请在左边的文本框中按行输入</span></p><p align=\"center\"><span\n"
                                          "                    style=\" font-size:12pt;\">一个表示图的邻接矩阵</span></p><p align=\"center\"><span\n"
                                          "                    style=\" font-size:12pt;\">格式参考文本框内示例</span></p></body></html>\n"
                                          "                "))


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.ui = None
        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 700, 700)
        self.setWindowTitle('isEulerGraph')
        self.setWindowIcon(QIcon('icon.png'))

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.plotGraph)

        self.show()

    def plotGraph(self):
        # 示例绘制一个五个节点的无向图
        G = np.array([[0, 1, 0, 0, 1],
                      [1, 0, 1, 0, 0],
                      [0, 1, 0, 1, 0],
                      [0, 0, 1, 0, 1],
                      [1, 0, 0, 1, 0]])

        fig = Figure(figsize=(3, 3))
        ax = fig.add_subplot(111)
        ax.axis('off')
        ax.set_aspect('equal')
        pos = np.array([[0, 0], [-1, 1], [1, 1], [-1, -1], [1, -1]])
        ax.scatter(pos[:, 0], pos[:, 1], s=300, c='w', edgecolors='k', zorder=2)
        for i in range(5):
            for j in range(i + 1, 5):
                if G[i, j] == 1:
                    ax.plot([pos[i, 0], pos[j, 0]], [pos[i, 1], pos[j, 1]], 'k-', zorder=1)

        self.ui.graphCanvas = FigureCanvas(fig)
        self.ui.graphCanvas.setParent(self.ui.graphCanvasParent)
        self.ui.graphCanvas.show()

        try:
            self.ui.graphCanvas.draw()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
