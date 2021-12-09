import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from random import randint


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(542, 519)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.flex_btn = QtWidgets.QPushButton(self.centralwidget)
        self.flex_btn.setGeometry(QtCore.QRect(190, 430, 151, 31))
        self.flex_btn.setObjectName("flex_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 542, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.flex_btn.setText(_translate("MainWindow", "Устроить флекс"))


class Application(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.can_paint = False
        self.initUI()

    def initUI(self):
        # self.setWindowTitle("Шарики!!")
        self.flex_btn.clicked.connect(self.paint_circles)

    def paint_circles(self):
        self.can_paint = True
        self.repaint()

    def paint_screen(self, qp):
        qp.setBrush(QColor(255, 255, 255))
        qp.setPen(QColor(255, 255, 255))
        qp.drawRect(0, 0, 541, 411)
        drawed_circles = list()
        value = randint(5, 50)
        for i in range(value):
            color = QColor(randint(0, 255), randint(0, 255), randint(0, 255))
            qp.setBrush(color)
            qp.setPen(color)
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
