from PyQt5.QtWidgets import QApplication, QMainWindow, QRubberBand, QWidget
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

		self.rubberband = QRubberBand(QRubberBand.Rectangle, self)
		self.selRect = None

	def mousePressEvent(self, event):
		self.origin = event.pos()
		self.rubberband.setGeometry(QtCore.QRect(self.origin, QtCore.QSize()))
		self.rubberband.show()
		QWidget.mousePressEvent(self, event)

	def mouseMoveEvent(self, event):
		if self.rubberband.isVisible():
			self.rubberband.setGeometry(QtCore.QRect(self.origin, event.pos()).normalized())
		QWidget.mouseMoveEvent(self, event)

	def mouseReleaseEvent(self, event):
		if self.rubberband.isVisible():
			self.rubberband.hide()
			self.selRect = self.rubberband.geometry()
		QWidget.mouseReleaseEvent(self, event)
		print("hallo")

	def exit(self):
		sys.exit(0)

app = QApplication(sys.argv)
ui = FsApp()
ui.show()
sys.exit(app.exec_())
