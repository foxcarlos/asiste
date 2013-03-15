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
from contactosUi import Ui_Form

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
        self.main()

    def main(self):
        host,  db, user, clave = fc.opcion_consultar('POSTGRESQL')
        self.cadconex = "host='%s' dbname='%s' user='%s' password='%s'" % (host[1], db[1], user[1], clave[1])

        self.iniciarForm()
        self.Buscar()

    def iniciarForm(self):
        '''
        '''

        #Activar la Busqueda al escribir el los textbox
        self.activarBuscar = True

        #Activar Bandera para saber cuando el boton Nuevo funciona como Boton Nuevo
        self.banderaNuevo = True
        self.banderaModificar = True

        #Deshabilitar y Habilitar botones
        self.ui.btnNuevo.setEnabled(True)
        self.ui.btnModificar.setEnabled(False)
        self.ui.btnEliminar.setEnabled(False)
        self.ui.btnLimpiar.setEnabled(True)
        self.ui.btnDeshacer.setEnabled(False)
        self.ui.btnSalir.setEnabled(True)

        #Cambiar el Caption o Text del Boton
        self.ui.btnNuevo.setText("&Nuevo")
        self.ui.btnModificar.setText('&Modificar')

        #Cambiar icono del Boton Nuevo por Nuevo
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/contactos/30px-Crystal_Clear_app_List_manager.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ui.btnNuevo.setIcon(icon1)
        
        #Cambiar icono del Boton Modificar por Modificar
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/contactos/40px-Crystal_Clear_app_kedit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ui.btnModificar.setIcon(icon2)

        if sys.platform == 'win32':
            self.ui.btnNuevo.setIconSize(QtCore.QSize(45, 45))
            self.ui.btnModificar.setIconSize(QtCore.QSize(35, 35))
            self.ui.btnEliminar.setIconSize(QtCore.QSize(35, 35))
            self.ui.btnLimpiar.setIconSize(QtCore.QSize(35, 35))
            self.ui.btnDeshacer.setIconSize(QtCore.QSize(35, 35))
            self.ui.btnSalir.setIconSize(QtCore.QSize(35, 35))

    def Buscar(self):
        '''
        Metodo que se utiliza para realizar la busqueda segun lo que
        ingresa el usuario en las cajas de texto.
        '''
        
        if self.activarBuscar:
            cadsq = self.armar_select()
            lista = self.obtener_datos(cadsq)
            self.PrepararTableWidget(len(lista))  # Configurar el tableWidget
            self.InsertarRegistros(lista)  # Insertar los Registros en el TableWidget

    def armar_select(self):
        '''
        Metodo que permite armar la consulta select a medica que el usuario
        va tecleando en los textbox
        Parametro devuelto(1) String con la cadena sql de busqueda    
        '''

        lcNombre = ''  # self.ui.txtNombre.text()
        lcDepartamento = ''  # self.ui.txtDepartamento.text()
        lcTelefono = ''  # self.ui.txtTelefono.text()

        valorNombre =  "upper(nombre) like '%%%s%%' AND " % (lcNombre.upper()) if lcNombre else ''
        valorDepartamento =  " upper(departamento) like '%%%s%%' AND " % (lcDepartamento.upper()) if lcDepartamento else ''
        valorTelefono = " telefono like '%%%s%%' AND " % (lcTelefono) if lcTelefono else ''

        campos = valorNombre + valorDepartamento + valorTelefono
        
        cadSelect = 'select c.*, d.sym as dpto, l.sym as localidad, u.sym as ubicacion \
                from asiste.contactos c \
                left join asiste.departamento d on c.departamento_id = d.id \
                left join asiste.localidad l on c.localidad_id = l.id \
                left join asiste.ubicacion u on c.ubicacion_id = u.id '

        cadenaSql = '{0} where {1} c.del = 0 order by c.nombre, c.apellido desc'.format(cadSelect, campos)
        return cadenaSql

    def PrepararTableWidget(self, CantidadReg=0):
        '''
        Meotod que permite asignar y ajustar  las columnas que tendra el tablewidget
        basados en la cantidad de conlumnas y la cantidad de registros que le son
        pasados como parametro
        #Ej: lista = ((0, 'Carlos Garcia', 'Sistemas', '41075'), (1, 'Nairesther Gomez', 'Docencia', '41075')) 
        '''

        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(245, 244, 226))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)

        brush = QtGui.QBrush(QtGui.QColor(254, 206, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)

        brush = QtGui.QBrush(QtGui.QColor(255, 255, 203))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)

        lista = CantidadReg
        
        #Indicar los nombres que tendran las cabeceras de los campos o columnas
        #cabecera = ["ID", "Nombre", "Departamento", "Telefono"]
        cabecera = ['id', 'cedula', 'nombre', 'apellido', 'usuario_red', 'email', 'telefono_oficina', 'telefono_movil', 'Departamento']
        
        self.ui.tableWidget.setColumnCount(len(cabecera))
        self.ui.tableWidget.setRowCount(lista)

        self.ui.tableWidget.setHorizontalHeaderLabels(cabecera)
        self.ui.tableWidget.setPalette(palette)

        #Ajustar el ancho de las columnas
        self.ui.tableWidget.horizontalHeader().resizeSection(0, 40)
        self.ui.tableWidget.horizontalHeader().resizeSection(1, 206)
        self.ui.tableWidget.horizontalHeader().resizeSection(2, 216)
        self.ui.tableWidget.horizontalHeader().resizeSection(3, 90)

        self.ui.tableWidget.setAutoFillBackground(False)
        self.ui.tableWidget.setAlternatingRowColors(True)

        self.ui.tableWidget.setSelectionMode(QtGui.QTableWidget.SingleSelection)
        self.ui.tableWidget.setSelectionBehavior(QtGui.QTableView.SelectRows)

        #ciudades = ["Valencia","Maracay","Barquisimeto","Merida","Caracas"]
        #self.combo.addItems(ciudades)
        #deshabilitar() 

    def InsertarRegistros(self, cursor):
        '''
        Metodo que permite asignarle registros al tablewidget
        parametros recibitos (1) Tipo (Lista)
        Ej:RowSource(['0', 'Carlos', 'Garcia'], ['1', 'Nairesther', 'Gomez'])
        '''

        ListaCursor = cursor
        for pos, fila in enumerate(ListaCursor):
            for posc, columna in enumerate(fila):
                self.ui.tableWidget.setItem(pos, posc, QtGui.QTableWidgetItem(str(columna)))

    def obtener_datos(self, cadena_pasada):
        '''
        Ejecuta la Consulta SQl a el servidor PostGreSQL segun la cadena SQL
        pasada como parametro
        parametros recibidos: (1) String
        parametros devueltos: (1) Lista

        Ej: obtener_datos('select *from tabla where condicion')
        '''

        try:
            pg = ConectarPG(self.cadconex)
            self.registros = pg.ejecutar(cadena_pasada)
            pg.cur.close()
            pg.conn.close()
        except:
            self.registros = []
        return self.registros

    def limpiar_text(self):
        '''
        Limpia los QlineEdit o Textbox
        '''
        self.txtId.clear()
        self.txtNombre.clear()
        self.txtDepartamento.clear()
        self.txtTelefono.clear()
        self.iniciarForm()

    def clickEnTabla(self):
        '''
        Este metodo se activa al momento de hace click en el tableWidget y permite
        mostrar el contenido de los campos de la fila seleccionada en el tableWidget
        en los textbox bien sea para Verlos, modificarlos o Eliminarlos
        '''

        self.activarBuscar = False
         
        fila = self.tableWidget.currentRow()
        #total_columnas = self.tableWidget.columnCount()
        
        id = self.ui.tableWidget.item(fila, 0).text()
        nombre = self.ui.tableWidget.item(fila, 1).text()
        dpto = self.ui.tableWidget.item(fila, 2).text()
        tlf = self.ui.tableWidget.item(fila, 3).text()

        self.txtId.setText(id)
        self.txtNombre.setText(nombre)
        self.txtDepartamento.setText(dpto)
        self.txtTelefono.setText(tlf) 

        self.ui.btnModificar.setEnabled(True)
        self.ui.btnEliminar.setEnabled(True)

    def nuevoGuardar(self):
        '''
        El metodo nuevo cumple dos funciones, una es de boton nuevo y otra es de boton guardar,
        la Variables self.banderaNuevo es el swith que me permite saber cuando el 
        boton nuevo hace la funcion de nuevo o de guardar, cuando la variable
        banderaNuevo es True entonces el boton debe actuar como Boton Nuevo de
        lo contrario cuando banderaNuevo es false entonces el boton nuevo debe 
        actuar como boton Guardar
        
        lcMensaje = 'Hola'  # self.combo.currentText()
        msgBox = QtGui.QMessageBox(QtGui.QMessageBox.Question, 'Titulo',lcMensaje)
        msgBox.exec_()
        '''

        if self.banderaNuevo:
            #Prepara los Botones
            self.habilitarNuevo()
        else:
            #Ejecurar sentencia SQL para guardar en PostGreSQL
            nombre = self.txtNombre.text()
            dpto = self.txtDepartamento.text()
            telf = self.txtTelefono.text()

            sqlInsert = " insert into agenda (nombre, departamento, telefono) values ('%s', '%s', '%s') " % (nombre, dpto, telf)
            
            try:
                pg = ConectarPG(self.cadconex)
                pg.ejecutar(sqlInsert)
                pg.conn.commit()

                lcMensaje = 'Registro Guardaro Satisfactoriamente'  # self.combo.currentText()
                msgBox = QtGui.QMessageBox(QtGui.QMessageBox.Information, 'Felicidades',lcMensaje)
                msgBox.exec_()
            except:
                print exceptionValue
            
            #Restaurar todos los Iconos y Botones
            self.iniciarForm()
            self.limpiar_text()


    def habilitarNuevo(self):
        ''' 
         Este metodo permite preparar los botones, los text y los iconos.
         Cuando se presiona el boton nuevo por primera vez este cambia para Boton Guardar asi como  
         tanmbien el icono y el texto del boton y desabilita el resto de los botonos, dejando solo 
         el boton Guardar,deshacer y salir
        '''

        #Limpar los TextBox
        self.limpiar_text()

        #Desactivar la Busqueda al escribir el los textbox
        self.activarBuscar = False

        #Activar Bandera para saber cuando el boton Nuevo funciona como Boton Nuevo o Como Boton Guardar
        self.banderaNuevo = False

        #Deshabilitar y Habilitar botonoes
        self.btnModificar.setEnabled(False)
        self.btnEliminar.setEnabled(False)
        self.btnLimpiar.setEnabled(False)
        self.btnDeshacer.setEnabled(True)
            
        #Cambiar el Caption o Text del Boton
        self.btnNuevo.setText("&Guardar")
            
        #Cambiar icono del Boton Nuevo  de Nuevo por Guardar
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/contactos/40px_3floppy_unmount.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnNuevo.setIcon(icon1)
        self.txtNombre.setFocus()

    def modificarGuardar(self):
        '''
        El metodo modificarGuardar cumple dos funciones, una es de boton Modificar y otra es de boton guardar,
        la Variables self.banderaModificar es el swith que me permite saber cuando el 
        boton Modificar hace la funcion de Modificar o de guardar, cuando la variable
        banderaModificar es True entonces el boton debe actuar como Boton Guardar de
        lo contrario cuando banderaModificar es false entonces el boton nuevo debe 
        actuar como boton Guardar
        '''

        if self.banderaModificar:
            #Prepara los Botones
            self.habilitarModificar()
        else:            
            #Ejecurar sentencia SQL para guardar en PostGreSQL
            id = self.txtId.text()
            nombre = self.txtNombre.text()
            dpto = self.txtDepartamento.text()
            telf = self.txtTelefono.text()

            sqlUpdate = " update agenda set nombre = '%s', departamento = '%s', telefono = '%s' where id = %s " % (nombre, dpto, telf, id)
            print sqlUpdate

            try:
                pg = ConectarPG(self.cadconex)
                pg.ejecutar(sqlUpdate)
                pg.conn.commit()

                lcMensaje = 'Registro Guardaro Satisfactoriamente'  # self.combo.currentText()
                msgBox = QtGui.QMessageBox(QtGui.QMessageBox.Information, 'Felicidades',lcMensaje)
                msgBox.exec_()
            except:
                print exceptionValue
            
            #Restaurar los Botones a su normalidad
            self.iniciarForm()
            self.limpiar_text()


    def habilitarModificar(self):
        ''' 
         Este metodo permite habilitar el Boton Modificar.
         Cuando se presiona el boton Modificar por primera vez este cambia para Boton Guardar asi como  
         tanmbien el icono y el texto del boton y desabilita el resto de los botonos, dejando solo el 
         boton Guardar,deshacer y salir
        '''

        #Desactivar la Busqueda al escribir el los QlineEdit o TextBox
        self.activarBuscar = False

        #Activar Bandera para saber cuando el boton Nuevo funciona como Boton Nuevo o Como Boton Guardar
        self.banderaModificar = False
            
        #Deshabilitar y Habilitar botonoes y TextBox
        self.txtId.setEnabled(False)

        self.btnNuevo.setEnabled(False)
        self.btnEliminar.setEnabled(False)
        self.btnLimpiar.setEnabled(False)
        self.btnDeshacer.setEnabled(True)
            
        #Cambiar el Caption o Text del Boton
        self.btnModificar.setText("&Guardar")
            
        #Cambiar icono del Boton Nuevo  de Nuevo por Guardar
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/contactos/40px_3floppy_unmount.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnModificar.setIcon(icon1)
        self.txtNombre.setFocus()

    def preguntarEliminar(self):
        '''
        Metodo que permite Consultar si se desea eliminar un registro de la Agenda
        '''
        msgBox = QtGui.QMessageBox(QtGui.QMessageBox.Question, 'Informacion', 'Este Registro sera Eliminado')
        msgBox.setInformativeText(u"¿Esta Seguro que desea eliminar este registro?")
        
        GuardarButton = msgBox.addButton("&Aceptar", QtGui.QMessageBox.ActionRole)
        CancelarButton = msgBox.addButton("&Cancelar", QtGui.QMessageBox.ActionRole)
        msgBox.exec_()
        
        if msgBox.clickedButton() == GuardarButton:
            print 'Aceptar'
            self.eliminar()
        
        elif msgBox.clickedButton() == CancelarButton:
            #print 'Cancelar'
            pass

    def eliminar(self):
        '''
        Metodo que permite eliminar de la base de datos un registro de la agenda
        '''
        
        id = self.txtId.text()
        sqlDelete = " update agenda set del = 1 where id = %s " % (id)
        print sqlDelete

        try:
            pg = ConectarPG(self.cadconex)
            pg.ejecutar(sqlDelete)
            pg.conn.commit()

            lcMensaje = 'Registro Eliminado Satisfactoriamente'
            msgBox = QtGui.QMessageBox(QtGui.QMessageBox.Information, 'Felicidades',lcMensaje)
            msgBox.exec_()
        except:
            print exceptionValue
        
        #Restaurar los Botones a su normalidad
        self.iniciarForm()
        self.limpiar_text()

    def salir(self):
        pass

    def borrar(self):
        msgBox = QtGui.QMessageBox(QtGui.QMessageBox.Question, 'Titulo', 'Prueba')
        #msgBox.setStandardButtons(QtGui.QMessageBox.Save | QtGui.QMessageBox.Discard | QtGui.QMessageBox.Cancel)
        GuardarButton = msgBox.addButton("Guardar", QtGui.QMessageBox.ActionRole)
        AbortarButton = msgBox.addButton("Cancelar", QtGui.QMessageBox.ActionRole)
        msgBox.exec_()
        print GuardarButton
        print AbortarButton

    def GoFocus(self):
        lcMensaje = 'Hola'  # self.combo.currentText()
        msgBox = QtGui.QMessageBox(QtGui.QMessageBox.Question, 'Titulo',lcMensaje)
        msgBox.exec_()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mySW = ControlMainWindow()
    mySW.show()
    sys.exit(app.exec_())
