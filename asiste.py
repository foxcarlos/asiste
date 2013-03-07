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
from PyQt4.QtCore import Qt,QVariant
from rutinas.varias import *
from windowUi import Ui_Form

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

        '''
        Aqui se conectan todos los objetos con sus slot
        '''
        
        QtCore.QObject.connect(self.ui.btnCombo, QtCore.SIGNAL("clicked()"), self.mostrar)
        QtCore.QObject.connect(self.ui.txtCreadoPor, QtCore.SIGNAL("returnPressed()"), self.enterEnCreadoPor)

        '''
        QtCore.QObject.connect(self.ui.btnLimpiar, QtCore.SIGNAL("clicked()"), self.limpiarText)
        QtCore.QObject.connect(self.ui.btnExportar, QtCore.SIGNAL("clicked()"), self.exportarExcel)
        self.connect(self.ui.btnSalir, QtCore.SIGNAL('clicked()'),QtGui.qApp, QtCore.SLOT('quit()'))
        self.statusBar().showMessage("Listo")
        '''

        self.main()

    def main(self):
        '''
        Este metodo se ejecuta al iniciar la Aplicacion,
        en las variables host, db, user, clave, se almacenaran
        los valores necesarios para realizar las consultas a
        el servidor de Base de Datos PostGreSQL y estas a su vez 
        crearan una Cadena de Conexion que sera utilizada por
        toda la aplicacion como variable Publica
        '''
        host, db, user, clave = fc.opcion_consultar('POSTGRESQL')
        self.cadconex = "host='%s' dbname='%s' user='%s' password='%s'" % (host[1], db[1], user[1], clave[1])

        self.registros = []
        self.llenarCombo()

        completer = QtGui.QCompleter()
        self.ui.txtCreadoPor.setCompleter(completer)
        model = QtGui.QStringListModel()
        completer.setModel(model)
        self.get_data(model)
        print self.ui.txtCreadoPor.text()
        #edit.show()
 
    def get_data(self, model):
        model.setStringList(["carlos garcia - 01", "carlos garzon", "garzon", "carlos alberto garcia"])

    def enterEnCreadoPor(self):
        '''
        '''
        print self.ui.txtCreadoPor.text()

    def llenarCombo(self):
        '''
        '''  
        try:
            pg = ConectarPG(self.cadconex)
            cadenaPasada = "select id, sym from asiste.estado where del = 0"
            registros = pg.ejecutar(cadenaPasada)
            print registros
            pg.cur.close()
            pg.conn.close()
        except:
            registros = []
 
        '''
        ciudades = [("01","Mar"),("02","Mer"),("03", "Car")]
        self.ui.cbxEstado.addItem('Etiqueta', 'Clave')
        self.ui.cbxEstado.addItem('Etiqueta2', 'Clave2')
        self.ui.cbxEstado.addItem('Etiqueta3', 'Clave3')
        '''
        
        items = registros  # [("ABC", 'True'), ("DEF", 'False'), ("GHI", 'False')]
        self.model = QtGui.QStandardItemModel()

        for id, sym in items:
            id_item = QtGui.QStandardItem(str(id))
            sym_item = QtGui.QStandardItem(sym)
            self.model.appendRow([sym_item, id_item])

        view = QtGui.QTreeView()
        view.header().hide()
        view.setRootIsDecorated(False)
        self.ui.cbxEstado.setView(view)
        self.ui.cbxEstado.setModel(self.model)
        self.ui.cbxEstado.show()
        #self.connect(self.ui.cbxEstado, QtCore.SIGNAL('activated(QString)'), self.mostrar)
        '''
        combo = QComboBox()
        combo.setView(view)
        combo.setModel(model)
        combo.show()
        '''
       
    def mostrar(self):
        '''
        '''
        #datetime.datetime.now()
        self.ui.dateTimeEdit.setDateTime(datetime.datetime.now())


    def obtenerDatosDelCombo(self, text):
        #indice = self.ui.cbxEstado.currentIndex()
        print text

        self.ui.cbxEstado.setModelColumn(1)
        print self.ui.cbxEstado.currentText()

        self.ui.cbxEstado.setModelColumn(0)
        print self.ui.cbxEstado.currentText()
        #ms = QtGui.QMessageBox(QtGui.QMessageBox.Warning, 'Titulo', msg)
        #ms.exec_()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mySW = ControlMainWindow()
    mySW.show()
    sys.exit(app.exec_())
