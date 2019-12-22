from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def clicked():
    print("Clicked")

def clicked2():
    print("clicked button 2")

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200,200,1000,1000)
    win.setWindowTitle("Tech with Aryan")

    label = QtWidgets.QLabel(win)
    label.setText("my label")
    label.move(50,50)

    b1 = QtWidgets.QPushButton(win)
    b1.setText("Click Me")
    b1.clicked.connect(clicked)

    b2 = QtWidgets.QPushButton(win)
    b2.setText("Click again")
    b2.move(100,100)
    b2.clicked.connect(clicked2)


    win.show()
    sys.exit(app.exec_())

window()