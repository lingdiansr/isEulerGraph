import matplotlib.pyplot as plt
import networkx as nx

# 画图！
G = nx.Graph()
G.add_node(1)
G.add_nodes_from([2, 3, 4, 5])
for i in range(5):
    for j in range(i):
        if abs(i - j) not in (1, 4):
            G.add_edge(i + 1, j + 1)
nx.draw(G,
        with_labels=True,  # 这个选项让节点有名称
        edge_color='b',  # b stands for blue!
        pos=nx.circular_layout(G),  # 这个是选项选择点的排列方式，具体可以用 help(nx.drawing.layout) 查看
        # 主要有spring_layout  (default), random_layout, circle_layout, shell_layout
        # 这里是环形排布，还有随机排列等其他方式
        node_color='r',  # r = red
        node_size=1000,  # 节点大小
        width=3,  # 边的宽度
        )
plt.show()
