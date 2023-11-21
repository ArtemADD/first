import sys
from random import randint
from PyQt5 import uic
from PyQt5.QtCore import QPointF
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.btn.clicked.connect(self.btn_draw)
        self.draw = False

    def btn_draw(self):
        self.draw = True
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        if self.draw:
            self.draw_circle(qp)
        qp.end()

    def draw_circle(self, qp):
        qp.setBrush(QColor('yellow'))
        d = (self.width() // 4 if self.height() < self.width() else self.height() // 4)
        d = randint(1, d)
        p = QPointF(self.width() / 2, self.height() / 2)
        qp.drawEllipse(p, d, d)
        self.draw = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec_())
