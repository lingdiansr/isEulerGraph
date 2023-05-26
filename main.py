import sys

import networkx as nx
import numpy as np
# from Mainwin import Ui_Form
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget
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


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = None
        self.axes = None  # 保存绘图区域
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 700, 700)
        self.setWindowTitle('isEulerGraph')
        self.setWindowIcon(QIcon('icon.png'))
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.plotGraph)
        self.show()

    type = ""

    def plotGraph(self):
        self.ui.graphCanvas.figure.clear()  # 清空绘图区域

        # 示例绘制一个五个节点的无向图
        G = nx.Graph()
        G = self.getGraph()
        # edges = [(0, 1), (0, 4), (1, 2), (2, 3), (3, 4), (4, 5), (0, 2)]
        # G.add_edges_from(edges)
        fig = Figure(figsize=(3, 3))
        ax = fig.add_subplot(111)
        ax.axis('off')
        ax.set_aspect('equal')
        pos = nx.spring_layout(G, seed=42)  # 使用spring layout布局，seed保证每次绘制结果一致
        nx.draw_networkx_nodes(G, pos, node_size=100, node_color='w', edgecolors='k', ax=ax)
        nx.draw_networkx_edges(G, pos, width=1, ax=ax)
        self.ui.graphCanvas.setGeometry(QtCore.QRect(30, 360, 300, 300))
        self.ui.graphCanvas.figure = fig
        self.ui.graphCanvas.draw()

    def getGraph(self):
        G = nx.Graph()
        matrix = np.matrix(self.ui.inputtext.toPlainText())
        # print(G)
        """h, w = matrix.shape
        for i in range(h):
            for j in range(w):
                if matrix[i][j] == 1:
                    G.add_edge(i, j)"""
        G = nx.from_numpy_array(matrix)
        if (matrix == matrix.T).all():
            self.type = "Undirected"
        else:
            self.type = "Directed"
        return G


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

"""
0,1,1;
1,0,1;
1,1,0
"""
