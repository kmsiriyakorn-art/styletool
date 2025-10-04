try :
	from PySide6 import QtCore , QtGui , QtWidgets 
	from shiboken6 import wrapInstance
except :
	from PySide2 import QtCore , QtGui , QtWidgets 
	from shiboken2 import wrapInstance

IMAGE_DIR = 'C:/Users/ICT68/Documents/maya/2025/scripts/styletool/image'

import maya.OpenMayaUI as omui

class StyleToolDialog(QtWidgets.QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)

		self.setWindowTitle('style tool')
		self.resize(300,100)

		self.mainLayout = QtWidgets.QVBoxLayout()
		self.setLayout(self.mainLayout)
		self.setStyleSheet(
			'''
				QDialog {
					background-color:#413C35;
				}
			'''
		)
		self.imageLabel = QtWidgets.QLabel()
		self.imagePixmap = QtGui.QPixmap(f'{IMAGE_DIR}/butter.png')
		scaledPixmap = self.imagePixmap.scaled(
			QtCore.QSize(100,100),
			QtCore.Qt.KeepAspectRatio,
			QtCore.Qt.SmoothTransformation

			)
		self.imageLabel.setPixmap(scaledPixmap)
		self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)
		
		self.mainLayout.addWidget(self.imageLabel)

		self.nameLayout = QtWidgets.QHBoxLayout()
		self.mainLayout. addLayout(self.nameLayout)
		self.nameLabel = QtWidgets.QLabel('Name:')
		self.nameLineEdit = QtWidgets.QLineEdit()
		self.nameLineEdit.setStyleSheet(
		'''	
			QLineEdit{
				background-color:qlineargradient(x1:0,y1:0,x2:0,y2:1, stop:0 #C0B1A5,stop:1 #968374);
				color: black;
				border-radius: 8px;
				font-family: Arial;
				font-weight: bold;
			}
	
		''')
		self.nameLayout.addWidget(self.nameLabel)
		self.nameLayout.addWidget(self.nameLineEdit)

		self.buttonLayout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.buttonLayout)
		self.selectButton = QtWidgets.QPushButton('select')
		self.selectButton.setStyleSheet(
			'''
				QPushButton {
					background-color:#C08C3D;
					border-radius: 12px;
					font-size: 16px;
					font-family: Papyrus;
					padding: 4px;
				}
				QPushButton:hover {
					background-color: qlineargradient(x1:0,y1:0,x2:0,y2:1, stop:0 #C08C3D,stop:1 #000000)
				}
				QPushButton:pressed{
					background-color: black;
				}
			''')
		self.cancelButton = QtWidgets.QPushButton('cancel')
		self.buttonLayout.addWidget(self.selectButton)
		self.buttonLayout.addWidget(self.cancelButton)

def run() :
	global ui
	try :
		ui.close()
	except :
		pass
	ptr = wrapInstance(int(omui.MQtUtil.mainWindow()),QtWidgets.QWidget)
	ui = StyleToolDialog(parent=ptr)
	ui.show()




