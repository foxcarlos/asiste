#-*-coding: utf-8 -*-

# Created: Fri Feb 22 10:25:34 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# pyside-uic -o windowUi.py src/pymanati.ui
#
# WARNING! All changes made in this file will be lost!

import sys
import datetime
from PySide import QtCore, QtGui
from rutinas.varias import *
from practicaUi import Ui_Form

ruta_arch_conf = os.path.dirname(sys.argv[0])
archivo_configuracion = os.path.join(ruta_arch_conf, 'config.conf')
fc = FileConfig(archivo_configuracion)


class ControlMainWindow(QtGui.QMainWindow):
    '''
    '''
    def __init__(self, parent=None):
        super(ControlMainWindow, self).__init__(parent)
        # Esto es siempre lo mismo
        self.ui = Ui_Form()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mySW = ControlMainWindow()
    mySW.show()
    sys.exit(app.exec_())
