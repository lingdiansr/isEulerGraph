import sys

import numpy as np
from PyQt5 import QtWidgets
from PyQt5 import uic
from PyQt5.QtWidgets import QDialog


class MyMainWin(QDialog):
    def __init__(self):
        super(MyMainWin, self).__init__()
        uic.loadUi('Mainwin.ui', self)

        self.pushButton.clicked.connect(self.onClick1)

    def onClick1(self):
        # self.inputtext.setText('文本测试\n测试测试')
        matrix = np.mat(self.inputtext.toPlainText())
        # self.outputLabel.setText(matrix)
        print(matrix)


def show_myMainWin():
    app = QtWidgets.QApplication(sys.argv)
    myMainWin = MyMainWin()
    myMainWin.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    show_myMainWin()
