import sys
import mainwindow
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    exe = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = mainwindow.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(exe.exec_())