from PyQt5.QtWidgets import QApplication, QMainWindow, QRubberBand, QWidget
from PyQt5 import QtCore, QtGui
from ui_fullscreen import Ui_MainWindow
import sys


class FsApp(QMainWindow):

	def __init__(self):
		super(FsApp, self).__init__()

		# Set up the user interface from Designer.
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.setWindowOpacity(0.5)
		self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)

		# Connect up the buttons.
		self.ui.butExit.clicked.connect(self.exit)

		self.rubberband = QRubberBand(QRubberBand.Rectangle, self)
		self.selRect = None
		bla = QtGui.QPalette()
		bla.setBrush(QtGui.QPalette.Highlight, QtGui.QBrush(QtCore.Qt.red))
		self.rubberband.setPalette(bla)

		self.showMaximized()
		self.showFullScreen()

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
			self.selRect = self.rubberband.geometry()
			self.rubberband.hide()
			self.exit()
		QWidget.mouseReleaseEvent(self, event)
		print("hallo")

	def exit(self):
		sys.exit(0)

app = QApplication(sys.argv)
ui = FsApp()
ui.show()
sys.exit(app.exec_())
