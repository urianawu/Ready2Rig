###############################################################################
# Name: 
#   ready2rig.py
#
# Description: 
#   Tool for automatically checking all standard requirements 
#	that needs to be met before going into rigging, includes
#	freeze transformation, delete history, pivot point, and symmetry(optional)
# Author: 
#   You Wu
###############################################################################

from PySide import QtCore
from PySide import QtGui

from shiboken import wrapInstance

import maya.cmds as cmds
import maya.OpenMayaUI as omui

def maya_main_window():
	main_window_ptr = omui.MQtUtil.mainWindow()
	return wrapInstance(long(main_window_ptr), QtGui.QWidget)
	
class Ready2RigUi(QtGui.QDialog):

	def __init__(self, parent=maya_main_window()):
		super(Ready2RigUi, self).__init__(parent)

		self.setWindowTitle("Ready2Rig")
		self.setWindowFlags(QtCore.Qt.Tool)

		self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

		self.create_controls()
		self.create_layout()
		self.create_connections()

	def create_controls(self):
		self.checkbox_ft = QtGui.QCheckBox("check FT")
		self.checkbox_ft.setChecked(True)

		self.checkbox_dh = QtGui.QCheckBox("delete history")
		self.checkbox_dh.setChecked(True)

		self.checkbox_pivot = QtGui.QCheckBox("check pivot")
		self.checkbox_sym = QtGui.QCheckBox("check symmetry")

		self.push_button = QtGui.QPushButton("Check it!")
		self.label_result = QtGui.QLabel("Click on the button to check")
		self.label_result.hide()

	def create_layout(self):
		check_box_layout = QtGui.QVBoxLayout()
		check_box_layout.setContentsMargins(2, 2, 2, 2)

		check_box_layout.addWidget(self.checkbox_ft)
		check_box_layout.addWidget(self.checkbox_dh)
		check_box_layout.addWidget(self.checkbox_pivot)
		check_box_layout.addWidget(self.checkbox_sym)

		main_layout = QtGui.QVBoxLayout()
		main_layout.setContentsMargins(6,6,6,6)
		main_layout.addLayout(check_box_layout)
		main_layout.addWidget(self.push_button)
		main_layout.addWidget(self.label_result)
		main_layout.addStretch()

		self.setLayout(main_layout)

	def create_connections(self):
		self.push_button.clicked.connect(self.on_button_pressed)


	def on_button_pressed(self):
		print("checking...")
		if self.checkbox_ft.isChecked():
			Ready2RigUi.check_transformation()
		if self.checkbox_dh.isChecked():
			Ready2RigUi.check_history()
		if self.checkbox_pivot.isChecked():
			Ready2RigUi.check_pivot()
		if self.checkbox_sym.isChecked():
			Ready2RigUi.check_sym()
		self.label_result.setText("Ready to rig")
		self.label_result.show()

	@classmethod
	def check_transformation(cls):
		print("checking transformation...")
		#cmds.select( all=True )
		transforms = cmds.itemFilter(byType='transform')
		print(transforms)
		#cmds.listAttr( st=['translateX','translateY', 'translateZ'])
		# for t in transforms:
		# 	if cmds.getAttr(t+'.'+t) != 0
		# 		print("Transformation not freezed.")
	@classmethod
	def check_history(cls):
		print("deleting history...")
		cmds.select( all=True )
		cmds.delete( all=True, ch=True)

			# if h != "None":
			# 	print("History not cleaned up.")

	@classmethod
	def check_pivot(cls):
		print("checking pivot...")

	@classmethod
	def check_sym(cls):
		print("checking symmetry")


if __name__ == "__main__":
	
		
	ui = Ready2RigUi()
	ui.show()


