import ctypes
import sys

import networkx as nx
import numpy as np
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget
from matplotlib.figure import Figure

from Mainwin import Ui_Form

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")


class Main(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = None
        self.axes = None  # 保存绘图区域
        self.graphType = ""
        self.judgeEuler = True
        self.G = None
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 700, 700)
        self.setWindowTitle('isEulerGraph')
        self.setWindowIcon(QIcon('winico.ico'))
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.getGraph)
        self.ui.pushButton.clicked.connect(self.plotGraph)
        self.ui.pushButton.clicked.connect(self.outJudge)
        self.show()

    def getGraph(self):
        while True:
            try:
                matrix = np.matrix(self.ui.inputtext.toPlainText())
                if (matrix == matrix.T).all():
                    self.graphType = "Undirected"
                    self.G = nx.Graph(matrix)
                    self.judgeEuler = all(d % 2 == 0 for v, d in self.G.degree()) and nx.is_connected(self.G)
                else:
                    self.graphType = "Directed"
                    self.G = nx.DiGraph(matrix)
                    self.judgeEuler = all(
                        self.G.out_degree(n) == self.G.in_degree(n) for n in self.G) and nx.is_strongly_connected(
                        self.G)
            except:
                QtWidgets.QMessageBox.warning(self, "错误", "输入格式错误，请按照要求重新输入！")
                return

    def plotGraph(self):
        if self.G is None:
            return
        self.ui.graphCanvas.figure.clear()  # 清空绘图区域
        fig = Figure(figsize=(3, 3))
        ax = fig.add_subplot(111)
        ax.axis('off')
        ax.set_aspect('equal')
        pos = nx.spring_layout(self.G, seed=42)  # 使用spring layout布局，seed保证每次绘制结果一致
        nx.draw_networkx_nodes(self.G, pos, node_size=100, node_color='w', edgecolors='k', ax=ax)
        if self.graphType == "Undirected":
            nx.draw_networkx_edges(self.G, pos, width=1, ax=ax)
        elif self.graphType == "Directed":
            nx.draw_networkx_edges(self.G, pos, width=1, arrows=True, arrowstyle='->', arrowsize=5, ax=ax)
        self.ui.graphCanvas.setGeometry(QtCore.QRect(30, 360, 300, 300))
        self.ui.graphCanvas.figure = fig
        self.ui.graphCanvas.draw()

    def outJudge(self):
        if self.G is None:
            return
        outString = "您输入的"
        if self.graphType == "Undirected":
            outString = outString + "无向图"
        else:
            outString = outString + "有向图"
        if self.judgeEuler:
            outString = outString + "是"
        else:
            outString = outString + "不是"
        outString = outString + "欧拉图！"
        self.ui.outputLabel.setText(outString)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
