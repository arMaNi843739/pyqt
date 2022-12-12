import sys
from PyQt6 import QtCore, QtWidgets

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        # ウィンドウを表示する位置(x,y)と大きさ(w,h)を指定
        # setGeometory(x, y, w, h)
        self.setGeometry(300, 50, 400, 350)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())