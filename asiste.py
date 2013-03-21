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
        Aqui se conectan todos los objetos con sus slot:

        QtCore.QObject.connect(self.ui.txtCreadoPor, QtCore.SIGNAL("editingFinished()"), self.quitarIdCreadoPor)
        '''

        parId1 = self.ui.txtIdCreadoPor
        parText1 = self.ui.txtCreadoPor
        parFoco1 = self.ui.txtReportadoPor
        parText1.editingFinished.connect(lambda: self.quitarId(parId1, parText1, parFoco1))
        #parText1.returnPressed.connect(lambda: self.quitarId(parId1, parText1, parFoco1))
 
        parId2 = self.ui.txtIdReportadoPor
        parText2 = self.ui.txtReportadoPor
        parFoco2 = self.ui.txtAfectado
        parText2.editingFinished.connect(lambda: self.quitarId(parId2, parText2, parFoco2))
        #parText2.returnPressed.connect(lambda: self.quitarId(parId2, parText2, parFoco2))

        parId3 = self.ui.txtIdAfectado
        parText3 = self.ui.txtAfectado
        parFoco3 = self.ui.txtIncidente
        parText3.editingFinished.connect(lambda: self.quitarId(parId3, parText3, parFoco3))
        #parText3.returnPressed.connect(lambda: self.quitarId(parId3, parText3, parFoco3))

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
        self.ui.txtFechaApertura.setDateTime(datetime.datetime.now())
        self.registros = []
        self.llenarCombo()
        self.prepararAutoCompletar()
        self.ui.txtCreadoPor.setFocus()
        
    def prepararAutoCompletar(self):
        pg = ConectarPG(self.cadconex)

        regContactos0 = pg.ejecutar("Select nombre||' '||apellido||','||id as contacto from asiste.contactos order by nombre")
        regContactos1 = pg.ejecutar("Select apellido||' '||nombre||','||id as contacto from asiste.contactos order by apellido")
        regContactos2 = pg.ejecutar("Select cedula || ','||nombre||' '||apellido||','||id as contacto from asiste.contactos order by cedula")
        
        regContactos = regContactos0 + regContactos1 + regContactos2
        print regContactos
        
        self.autoCompletado(self.ui.txtCreadoPor, regContactos)
        self.autoCompletado(self.ui.txtReportadoPor, regContactos)
        self.autoCompletado(self.ui.txtAfectado, regContactos)
        
    def autoCompletado(self, objeto, lista):
        '''
        Este metodo permite iniciar el autocompletado de alguno de los textbox 
        o QlineEdit
        
        Ej: autoCompletado(self.lineEditNombre, ('Carlos', 'Nairesther', 'Paola', Carla))
        
        Parametro recibidos 2:
        1-) tipo Obj QlineEdit con el nombre del objeto al cual se le va aplicar el 
        autocompletado
        2-) Tipo Lista, La lista que se desea mostrar en el autocompletado
       '''       
        self.listaPalabras = [f[0] for f in lista]
        lineEdit = objeto
        completer = QtGui.QCompleter(self.listaPalabras, self)
        completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        lineEdit.setCompleter(completer)

    def quitarId(self, objeto1, objeto2, objeto3):
        '''
        '''
        objId = objeto1
        objTexto = objeto2
        objFoco = objeto3

        id = ''
        nombre = ''

        valorId = objId.text()
        valorPasado = objTexto.text()
        listaCod = valorPasado.split(',')
        
        if valorPasado:
            if len(listaCod) == 1:
                id = valorId
                nombre = valorPasado
    
            elif len(listaCod) == 2:
                nombre = listaCod[0] 
                id = listaCod[1]
    
            elif len(listaCod) == 3:         
                id = listaCod[2]
                nombre = listaCod[1]
               
            conseguido = False
            for f in self.listaPalabras:
                if nombre in f.split(','):
                    conseguido = True
    
            if conseguido:
                objId.setText(id)
                objTexto.setText(nombre)
                objFoco.setFocus()
            else:
                objId.setText('')
                objTexto.setText('')
                mi = QtGui.QMessageBox(QtGui.QMessageBox.Warning, 'Mensage de Sistema *** Atencion *** ', 
                        'El contacto ingresado no Existe, Favor verifique el conactacto')
                mi.exec_()

    def llenarCombo(self):
        '''
        '''  
        try:
            pg = ConectarPG(self.cadconex)
            cadenaPasada = "select id, sym from asiste.estado where del = 0"
            registros = pg.ejecutar(cadenaPasada)
            #print registros
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
    def nombrepc(self):
        return os.uname()[1]
    
    def login(self):
        return os.getlogin()

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
