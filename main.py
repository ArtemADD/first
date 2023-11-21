import sys
from random import randint
from PyQt5.QtCore import QPointF
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_yellow_circle(object):
    def setupUi(self, yellow_circle):
        yellow_circle.setObjectName("yellow_circle")
        yellow_circle.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(yellow_circle)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 255, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn.setFont(font)
        self.btn.setObjectName("btn")
        self.horizontalLayout.addWidget(self.btn)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        yellow_circle.setCentralWidget(self.centralwidget)

        self.retranslateUi(yellow_circle)
        QtCore.QMetaObject.connectSlotsByName(yellow_circle)

    def retranslateUi(self, yellow_circle):
        _translate = QtCore.QCoreApplication.translate
        yellow_circle.setWindowTitle(_translate("yellow_circle", "Желтые окружности"))
        self.btn.setText(_translate("yellow_circle", "Нажми на меня"))


class Main(QMainWindow, Ui_yellow_circle):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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
        qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0,255)))
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
