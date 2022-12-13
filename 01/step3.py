import sys
from PyQt6 import QtCore, QtWidgets

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        # ウィンドウを表示する位置(x,y)と大きさ(w,h)を指定
        # setGeometory(x, y, w, h)
        self.setGeometry(300, 50, 400, 350)

        # Hello World!と書かれたラベルを追加
        self.label = QtWidgets.QLabel('Hello World!', self)
        # ラベルを表示する位置と大きさを指定
        self.label.setGeometry(50, 50, 100, 10)

        # Buttonと書かれたボタンを追加
        button = QtWidgets.QPushButton('Button', self)
        button.setGeometry(170, 155, 60, 40)
        # ボタンがクリックされたときにself.buttonClicked関数を発火
        button.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        print('Button Clicked!')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())