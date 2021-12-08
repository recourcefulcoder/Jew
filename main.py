import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor
from random import randint


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class Application(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.can_paint = False
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Шарики!!")
        self.flex_btn.clicked.connect(self.paint_circles)

    def paint_circles(self):
        self.can_paint = True
        self.repaint()

    def paint_screen(self, qp):
        qp.setBrush(QColor(255, 255, 255))
        qp.setPen(QColor(255, 255, 255))
        qp.drawRect(0, 0, 541, 411)
        qp.setBrush(QColor(255, 255, 0))
        qp.setPen(QColor(255, 255, 0))
        drawed_circles = list()
        value = randint(5, 50)
        for i in range(value):
            radius = randint(1, 50)
            x_coord = randint(0, 541 - radius)
            y_coord = randint(0, 411 - radius)
            drawed_circles.append(((x_coord, y_coord), radius))
            qp.drawEllipse(x_coord, y_coord, radius, radius)

    def paintEvent(self, event):
        if self.can_paint:
            self.can_paint = False
            qp = QPainter()
            qp.begin(self)
            self.paint_screen(qp)
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    application = Application()
    application.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
