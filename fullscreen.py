from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore
from ui_fullscreen import Ui_MainWindow
import sys


class FsApp(QMainWindow):

    def __init__(self):
        super(FsApp, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.showMaximized()
        self.showFullScreen()
        self.setWindowOpacity(0.7)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)

        # Connect up the buttons.
        #self.ui.okButton.clicked.connect(self.accept)
        self.ui.butExit.clicked.connect(self.exit)

    def exit(self):
        sys.exit(0)

app = QApplication(sys.argv)
ui = FsApp()
ui.show()
sys.exit(app.exec_())