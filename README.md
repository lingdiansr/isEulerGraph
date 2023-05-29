# isEulerGraph

## 1. 作品描述

本程序是一个通用程序，可以通过输入一个图的邻接矩阵，将其绘制出来，并判断此图是有向图或无向图，以及是否为欧拉图

## 2. 使用的程序开发工具

- 开发语言 Python 3
- 开发环境 Pycharm Virtualenv
- 其他运行库
  - numpy 获取矩阵及矩阵运算
  - networkx 创建图及其绘制等
  - matplotlib 将图形绘制在界面上
  - Pyqt5 制作图形界面
- 安装命令
  ```
  pip install numpy -i https://pypi.tuna.tsinghua.edu.cn/simple
  pip install networkx -i https://pypi.tuna.tsinghua.edu.cn/simple
  pip install matplotlib -i https://pypi.tuna.tsinghua.edu.cn/simple
  pip install PyQt5 -i https://pypi.douban.com/simple
  pip install PyQt5-tools -i https://pypi.douban.com/simple
  ```  

## 3. 程序代码文件说明、运行方法说明及运行效果截图

### 3.1 程序代码文件说明

- main.py 程序的主要代码文件
- Mainwin.py 构建程序界面的ui代码文件
- Mainwin.ui 从QtDesigner创建的界面文件
- winico.ico 程序的图标文件
- onlyEXE.zip 程序的可执行文件以及图标文件的压缩包

### 3.2 运行方法说明

完全解压onlyEXE.zip后双击main.exe运行即可

### 3.3 运行效果截图