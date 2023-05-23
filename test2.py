# python version: 3.8
# numpy, matplotlib
# copy from book ISBN:978-7-115-48558-8

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 6, 0.1)  # 0, 0.1, 0.2, ... , 5.9, 6.0
y = np.sin(x)

plt.plot(x, y)
plt.show()
