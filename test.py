import matplotlib.pyplot as plt
import networkx as nx
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class Figure_Canvas(FigureCanvas):
    # 通过继承FigureCanvas类，使得该类既是一个PyQt5的Qwidget，又是一个matplotlib的FigureCanvas，这是连接pyqt5与matplotlib的关键
    def __init__(self):
        self.fig = plt.figure()  # 可选参数,facecolor为背景颜色
        FigureCanvas.__init__(self, self.fig)  # 初始化激活widget中的plt部分

    def draw_graph(self):
        node_color = ['r']
        data = {'张三':
                    {'校友': ['李一', '李二', '李三', '李四'],
                     '同学': ['王一', '王二', '王三', '王四', '王五'],
                     '同事': ['马一', '马二', '马三', '马四', '马五', '马六']
                     }
                }

        self.G = nx.Graph()
        for k, v in data.items():
            self.G.add_node(k, id='0001')
            for m, n in v.items():
                if m == '校友':
                    node_color.extend(['b'] * len(n))
                    for i in n:
                        self.G.add_node(i, id='0002')
                        self.G.add_edge(k, i, weight=0.3, relation='校友')
                elif m == '同学':
                    node_color.extend(['b'] * len(n))
                    for i in n:
                        self.G.add_node(i, id='0003')
                        self.G.add_edge(k, i, weight=0.5, relation='同学')
                else:
                    node_color.extend(['g'] * len(n))
                    for i in n:
                        self.G.add_node(i, id='0003')
                        self.G.add_edge(k, i, weight=0.9, relation='同事')
        pos = nx.spring_layout(self.G)

        relations = {}
        for po in pos:
            print(po, pos[po])
            xy = [[pos[po][0] - 0.05, pos[po][0] + 0.05],
                  [pos[po][1] - 0.05, pos[po][1] + 0.05]]
            relations[po] = xy

        labels = {}
        for edge in self.G.edges(data=True):
            labels[(edge[0], edge[1])] = edge[-1]['relation']
        # 如果不使用canvas.mpl_connect的话将不能激活event
        self.fig.canvas.mpl_connect('button_press_event', lambda event: self.on_press(event, relations))

        nx.draw(self.G, pos, with_labels=True, node_color=node_color, edge_color='b', node_size=1000,
                rotate=True)

        nx.draw_networkx_edge_labels(self.G, pos, edge_labels=labels)

    def gui_draw(self):
        # 第一步，创建一个QGraphicsView，注意同样以gridLayoutWidget为参数
        self.graphicview = QtWidgets.QGraphicsView(self.gridLayoutWidget)
        # 第二步，设置graphicview的区域
        self.graphicsView.setGeometry(QtCore.QRect(40, 10, 481, 431))
        # 第三步，实例化一个FigureCanvas
        dr = Figure_Canvas()
        dr.draw_graph()  # 画图
        # 第四步，创建一个QGraphicsScene，因为加载的图形（FigureCanvas）不能直接放到graphicview控件中，必须先放到graphicScene，然后再把graphicscene放到graphicview中
        graphicscene = QtWidgets.QGraphicsScene()
        # 第五步，把图形放到QGraphicsScene中，注意：图形是作为一个QWidget放到QGraphicsScene中的
        graphicscene.addWidget(dr)
        # 第六步，把QGraphicsScene放入QGraphicsView
        self.graphicview.setScene(graphicscene)
        # 第七步，调用show方法呈现图形！
        self.graphicview.show()


if __name__ == '__main__':
    g = Figure_Canvas
    g.gui_draw()
