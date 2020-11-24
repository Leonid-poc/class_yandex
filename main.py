import sys
from random import randint

from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.initUI()

    def initUI(self):
        # self.setGeometry(300, 300, 200, 200)
        # self.setWindowTitle('Рисование')
        # self.btn = QPushButton('Рисовать', self)
        # self.pushButton.move(70, 150)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        cnt = randint(5, 25)
        qp.setBrush(QColor(255, 242, 0))
        for i in range(cnt):
            x, y = randint(0, self.width()), randint(0, self.height())
            d = randint(10, 55)
            qp.drawEllipse(x, y, d, d)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())