import sys
from PySide2 import QtCore, QtGui, QtWidgets

font = QtGui.QFont()
font.setFamily("Tekton Pro Ext")
font.setPointSize(16)
font.setWeight(10)

class Ui_Dialog(object):
	def setupUi(self, mainWidget):

		mainWidget.setWindowTitle(QtWidgets.QApplication.translate("mainWidget", "Substance Painter Library", None, -1))
		mainWidget.resize(320,100)

		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(mainWidget.sizePolicy().hasHeightForWidth())
		mainWidget.setSizePolicy(sizePolicy)

		#Preset List Widget
		self.listWidget = QtWidgets.QListWidget(mainWidget)
		self.listWidget.setGeometry(QtCore.QRect(10, 10, 300, 100))
		self.listWidget.setObjectName("listWidget")
		
		self.item = QtWidgets.QListWidgetItem(self.listWidget)
		self.item.setText("test")
		self.item.setFont(font)
		self.item.setToolTip('<img src="./icon.png" width = "400" height = "400">') #set Icon tool tip	for item	
		self.listWidget.addItem(self.item)

		mainWidget.show()

app = QtWidgets.QApplication(sys.argv)
ui = Ui_Dialog()
dialog = QtWidgets.QWidget()
ui.setupUi(dialog)
dialog.activateWindow()
sys.exit(app.exec_())