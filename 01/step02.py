import sys
from PyQt6 import QtCore, QtWidgets

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setGeometry(300, 50, 400, 350)

        self.label = QtWidgets.QLabel('Hello World!', self)
        self.label.setGeometry(50, 50, 100, 10)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())