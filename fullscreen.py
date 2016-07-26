from PyQt5.QtWidgets import QApplication, QMainWindow, QRubberBand, QWidget
from PyQt5 import QtCore, QtGui
from ui_fullscreen import Ui_MainWindow
import sys

class FsApp(QMainWindow):

	def __init__(self, app):
		super(FsApp, self).__init__()
		self.app       = app
		self.selRect   = None
		self.screenPix = None

		# Set up the user interface from Designer.
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		#self.setWindowOpacity(0.5)
		#self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
		self.captureScreen()
		self.showMaximized()
		self.showFullScreen()

		#capture screen and display
		self.ui.labPix.resize(self.size())
		self.ui.labPix.setScaledContents(True)
		self.ui.labPix.setPixmap(self.screenPix)

		#start rubberband
		self.rubberband = QRubberBand(QRubberBand.Rectangle, self)
		bla = QtGui.QPalette()
		bla.setBrush(QtGui.QPalette.Highlight, QtGui.QBrush(QtCore.Qt.red))
		self.rubberband.setPalette(bla)
		self.rubberband.setWindowOpacity(1.0)

	def captureScreen(self):
		screens = self.app.screens()
		self.screenPix = screens[0].grabWindow(0)

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
			codePix = self.screenPix.copy(	self.selRect.x(),
							self.selRect.y(), 
                                              		self.selRect.width(),
							self.selRect.height())
			QApplication.clipboard().setPixmap(codePix)
			#self.exit()
		QWidget.mouseReleaseEvent(self, event)

	def exit(self):
		sys.exit(0)

app = QApplication(sys.argv)
ui = FsApp(app)
ui.show()
sys.exit(app.exec_())
