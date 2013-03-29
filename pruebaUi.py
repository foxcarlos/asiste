# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/prueba.ui'
#
# Created: Fri Mar 29 00:41:43 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(60, 120, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.checkBox = QtGui.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(70, 230, 84, 19))
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.checkBox, QtCore.SIGNAL("stateChanged(int)"), self.checkBox.click)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit.setToolTip(QtGui.QApplication.translate("Form", "click aqui ", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit.setStatusTip(QtGui.QApplication.translate("Form", "status tipp", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("Form", "CheckBox", None, QtGui.QApplication.UnicodeUTF8))

