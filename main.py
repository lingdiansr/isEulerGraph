import sys

import networkx as nx
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget
from matplotlib.figure import Figure

from Mainwin import Ui_Form


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
        G = nx.Graph()
        edges = [(0, 1), (0, 4), (1, 2), (2, 3), (3, 4)]
        G.add_edges_from(edges)
        fig = Figure(figsize=(3, 3))
        ax = fig.add_subplot(111)
        ax.axis('off')
        ax.set_aspect('equal')
        pos = nx.spring_layout(G, seed=42)  # 使用spring layout布局，seed保证每次绘制结果一致
        nx.draw_networkx_nodes(G, pos, node_size=300, node_color='w', edgecolors='k', ax=ax)
        nx.draw_networkx_edges(G, pos, width=1, ax=ax)
        self.ui.graphCanvas.setGeometry(QtCore.QRect(30, 360, 300, 300))
        self.ui.graphCanvas.figure = fig
        self.ui.graphCanvas.draw()

    def getGraph(self):
        G = nx.Graph()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
