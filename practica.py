# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtCore, QtGui
from rutinas.varias import *
import os

ruta_arch_conf = os.path.dirname(sys.argv[0])
archivo_configuracion = os.path.join(ruta_arch_conf, 'config.conf')
fc = FileConfig(archivo_configuracion)


class miQLineEdit(QtGui.QLineEdit):
    def __init__(self):
        super(miQLineEdit, self).__init__()
        self.foreColor()
        self.backColor()

    def autoCompletado(self, lista):
        '''
        Este metodo permite iniciar el autocompletado en el QlineEdit.
        Ej: autoCompletado([('Carlos',),  ('Nairesther',), ( 'Paola',), ( Carla,)])
        
        Parametro recibidos 1:
        1-) Tipo Lista, La lista que se desea mostrar en el autocompletado
       '''       
        self.listaPalabras = [f[0] for f in lista]
        completer = QtGui.QCompleter(self.listaPalabras, self)
        completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.setCompleter(completer)

    def infocus():
        pass

    def foreColor(self, color = QtGui.QColor(0, 0, 0)):
        paletteC = QtGui.QPalette()
        paletteC.setColor(QtGui.QPalette.Active, QtGui.QPalette.Text, color)
        self.setPalette(paletteC)
    
    def backColor(self, color = QtGui.QColor(254, 230, 150)):
        paletteB = QtGui.QPalette()
        paletteB.setColor(QtGui.QPalette.Active, QtGui.QPalette.Base, color)
        self.setPalette(paletteB)

class ui_(QtGui.QWidget):
    def __init__(self):
        super(ui_, self).__init__()
        #Se crean los Botones de mantenimiento superiores
        
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(228, 247, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        self.setPalette(palette)
       
        self.btnNuevo = QtGui.QPushButton()
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/30px-Crystal_Clear_app_List_manager.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnNuevo.setIcon(icon1)
        self.btnNuevo.setText('  &Nuevo  ')

        self.btnModificar = QtGui.QPushButton()
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/40px-Crystal_Clear_app_kedit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnModificar.setIcon(icon2)
        self.btnModificar.setText('&Modificar')
        self.btnModificar.setIcon(icon2)

        self.btnEliminar = QtGui.QPushButton()
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("img/30px_1 (514).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnEliminar.setIcon(icon3)
        self.btnEliminar.setText('&Eliminar ')

        self.btnDeshacer = QtGui.QPushButton()
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("img/40px_reload.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnDeshacer.setIcon(icon4)
        self.btnDeshacer.setText('&Deshacer ')

        self.btnLimpiar = QtGui.QPushButton()
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("img/erase.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnLimpiar.setIcon(icon5)
        self.btnLimpiar.setText(' &Limpiar ')

        self.btnExportar = QtGui.QPushButton()
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("img/OfficeExcel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnExportar.setIcon(icon6)
        self.btnExportar.setText('&Exportar ')

        self.btnSalir = QtGui.QPushButton()
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("img/25px_exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSalir.setIcon(icon7)
        self.btnSalir.setText('  &Salir  ')

        #Crear un Espacio entre Objetos con SpaceItem
        spacerItem1 = QtGui.QSpacerItem(400, 20)

        #Se crea un Layout Horizontal para los Botones
        self.hl = QtGui.QHBoxLayout()

        #Agregar los Botones superiores al Layout Horizontal
        self.hl.addWidget(self.btnNuevo)
        self.hl.addWidget(self.btnModificar)
        self.hl.addWidget(self.btnEliminar)
        self.hl.addWidget(self.btnDeshacer)
        self.hl.addWidget(self.btnLimpiar)
        self.hl.addWidget(self.btnExportar)
        self.hl.addItem(spacerItem1)  # Insertar un spaceIntem entre los Botones
        self.hl.addWidget(self.btnSalir)

        #Se Crea la Linea Horizontal que estara debajo de los Botones Superiores
        self.line = QtGui.QFrame()
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)

        '''Aqui se crean las Etiquetas y las cajas de Edicion'''
        
        #Definir los Colores de Texto y de Fondo de los QLineEdit
        self.colorTexto = QtGui.QColor(0, 0, 0)
        self.colorFondo = QtGui.QColor(254, 230, 150)
        palette = QtGui.QPalette()

        #Campo ID
        self.hlId = QtGui.QHBoxLayout()
        self.lblId = QtGui.QLabel('ID:')
        self.txtId = miQLineEdit()
        self.txtId.autoCompletado([('Carlos',), ( 'Carla Patricia',), ( 'Camen Diaz',)])
        self.spacerId = QtGui.QSpacerItem(500, 20)
        self.hlId.addWidget(self.txtId)
        self.hlId.addItem(self.spacerId)

        #Campo Cedula
        self.hlCedula = QtGui.QHBoxLayout()
        self.lblCedula = QtGui.QLabel('Cedula:')
        self.txtCedula = miQLineEdit()
        self.spacerCedula = QtGui.QSpacerItem(400, 20)
        self.hlCedula.addWidget(self.txtCedula)
        self.hlCedula.addItem(self.spacerCedula)

        #Campo Codigo
        self.hlCodigo = QtGui.QHBoxLayout()
        self.lblCodigo = QtGui.QLabel('Codigo:')
        self.txtCodigo = miQLineEdit()
        self.spacerCodigo = QtGui.QSpacerItem(400, 20)
        self.hlCodigo.addWidget(self.txtCodigo)
        self.hlCodigo.addItem(self.spacerCodigo)

        #Campo Nombre
        self.lblNombre = QtGui.QLabel('Nombre')
        self.txtNombre = miQLineEdit()
        self.hlNombre = QtGui.QHBoxLayout()
        self.hlNombre.addWidget(self.txtNombre)

        #Campo Apellido
        self.lblApellido = QtGui.QLabel('Apellido')
        self.txtApellido = miQLineEdit()
        self.hlApellido = QtGui.QHBoxLayout()
        self.hlApellido.addWidget(self.txtApellido)

        #Campo Usuario
        self.hlUsuarioRed = QtGui.QHBoxLayout()
        self.lblUsuarioRed = QtGui.QLabel('Usuario de Red')
        self.txtUsuarioRed = miQLineEdit()
        self.spacerUsuarioRed = QtGui.QSpacerItem(400, 20)
        self.hlUsuarioRed.addWidget(self.txtUsuarioRed)
        self.hlUsuarioRed.addItem(self.spacerUsuarioRed)

        #Campo Tipo Contacto
        self.lblTipoContacto = QtGui.QLabel('Tipo de Contacto')
        self.cbxTipoContacto = QtGui.QComboBox()
        self.hlTipoContacto = QtGui.QHBoxLayout()
        self.spacerTipoContacto = QtGui.QSpacerItem(400, 20)
        self.hlTipoContacto.addWidget(self.cbxTipoContacto)
        self.hlTipoContacto.addItem(self.spacerTipoContacto)

        #Campo Telef Oficina
        self.lblTelefOficina = QtGui.QLabel('Telef. Oficina')
        self.txtTelefOficina = miQLineEdit()
 
        #Campo Telef Movil
        self.lblTelefMovil = QtGui.QLabel('Telef. Movil')
        self.txtTelefMovil = miQLineEdit()
 
        #Campo Email
        self.lblEmail = QtGui.QLabel('Email')
        self.txtEmail = miQLineEdit()
 
        #Campo Departamento
        self.lblDepartamento = QtGui.QLabel('Departamento:')
        self.txtDepartamento = miQLineEdit()
        self.btnDptoBuscar = QtGui.QPushButton()

        self.iconBtnBuscarDpto = QtGui.QIcon()
        self.iconBtnBuscarDpto.addPixmap(QtGui.QPixmap('img/contactos/apartment-2-16.png'))
        self.btnDptoBuscar.setIcon(self.iconBtnBuscarDpto)
        self.spacerDepartamento = QtGui.QSpacerItem(400, 20)
        self.hlDepartamento = QtGui.QHBoxLayout()
        self.hlDepartamento.addWidget(self.txtDepartamento)
        self.hlDepartamento.addWidget(self.btnDptoBuscar)
        self.hlDepartamento.addItem(self.spacerDepartamento)

        #Campo Localidad
        self.lblLocalidad = QtGui.QLabel('Localidad')
        self.txtLocalidad = miQLineEdit()
        self.btnLocalBuscar = QtGui.QPushButton()

        self.iconBtnBuscarLocal = QtGui.QIcon()
        self.iconBtnBuscarLocal.addPixmap(QtGui.QPixmap('img/contactos/map-4-24.png'))
        self.btnLocalBuscar.setIcon(self.iconBtnBuscarLocal)
        
        self.spacerLocal = QtGui.QSpacerItem(400, 20)
        self.hlLocal = QtGui.QHBoxLayout()
        self.hlLocal.addWidget(self.txtLocalidad)
        self.hlLocal.addWidget(self.btnLocalBuscar)
        self.hlLocal.addItem(self.spacerLocal)

        #Campo Ubicacion
        self.lblUbicacion = QtGui.QLabel('Ubicacion:')
        self.txtUbicacion = miQLineEdit()
        self.btnUbicaBuscar = QtGui.QPushButton()

        self.iconBtnBuscarUbica = QtGui.QIcon()
        self.iconBtnBuscarUbica.addPixmap(QtGui.QPixmap('img/contactos/building-5-24.png'))
        self.btnUbicaBuscar.setIcon(self.iconBtnBuscarUbica)
        self.spacerUbica = QtGui.QSpacerItem(400, 20)
        
        self.hlUbica = QtGui.QHBoxLayout()
        self.hlUbica.addWidget(self.txtUbicacion)
        self.hlUbica.addWidget(self.btnUbicaBuscar)
        self.hlUbica.addItem(self.spacerUbica)

        #Campo Observacion
        self.lblObservacion = QtGui.QLabel('Observacion:')
        self.txtObservacion = miQLineEdit()

        #La Tabla
        self.tableWidget = QtGui.QTableWidget()

        #Se insertan los Objetos en el Grid Loyouts de todo el Formulario
        self.gl = QtGui.QGridLayout()
        self.gl.addLayout(self.hl, 0, 1, 1, 8)
        self.gl.addWidget(self.line, 1, 1, 1, 8)

        self.gl.addWidget(self.lblId, 2, 1)
        self.gl.addLayout(self.hlId, 2, 2)

        self.gl.addWidget(self.tableWidget, 2, 3, 14, 1)

        self.gl.addWidget(self.lblCedula, 3, 1)
        self.gl.addLayout(self.hlCedula, 3, 2)

        self.gl.addWidget(self.lblCodigo, 4, 1)
        self.gl.addLayout(self.hlCodigo, 4, 2)

        self.gl.addWidget(self.lblNombre, 5, 1)
        self.gl.addLayout(self.hlNombre, 5, 2)

        self.gl.addWidget(self.lblApellido, 6, 1)
        self.gl.addLayout(self.hlApellido, 6, 2)

        self.gl.addWidget(self.lblUsuarioRed, 7, 1)
        self.gl.addLayout(self.hlUsuarioRed, 7, 2)

        self.gl.addWidget(self.lblTipoContacto, 8, 1)
        self.gl.addLayout(self.hlTipoContacto, 8, 2)

        self.gl.addWidget(self.lblTelefOficina, 9, 1)
        self.gl.addWidget(self.txtTelefOficina, 9, 2)

        self.gl.addWidget(self.lblTelefMovil, 10, 1)
        self.gl.addWidget(self.txtTelefMovil, 10, 2)

        self.gl.addWidget(self.lblEmail, 11, 1)
        self.gl.addWidget(self.txtEmail, 11, 2)

        self.gl.addWidget(self.lblDepartamento, 12, 1)
        self.gl.addLayout(self.hlDepartamento, 12, 2)

        self.gl.addWidget(self.lblLocalidad, 13, 1)
        self.gl.addLayout(self.hlLocal, 13, 2)

        self.gl.addWidget(self.lblUbicacion, 14, 1)
        self.gl.addLayout(self.hlUbica, 14, 2)

        self.gl.addWidget(self.lblObservacion, 15, 1)
        self.gl.addWidget(self.txtObservacion, 15, 2)

        self.setGeometry(0, 0, 1091, 496)

        self.setLayout(self.gl)
        
        #Hasta Aqui:
        #Eventos de los Botones.
        self.connect(self.btnLimpiar, QtCore.SIGNAL("clicked()"), self.limpiarText)

        #Eventos de los QLineEdit
        self.connect(self.txtId, QtCore.SIGNAL("textChanged(QString)"), self.Buscar)
        self.connect(self.txtCedula, QtCore.SIGNAL("textChanged(QString)"), self.Buscar)
        self.connect(self.txtCodigo, QtCore.SIGNAL("textChanged(QString)"), self.Buscar)
        self.connect(self.txtNombre, QtCore.SIGNAL("textChanged(QString)"), self.Buscar)
        self.connect(self.txtApellido, QtCore.SIGNAL("textChanged(QString)"), self.Buscar)
        self.connect(self.txtUsuarioRed, QtCore.SIGNAL("textChanged(QString)"), self.Buscar)
        #self.connect(self.txtTipoContacto, QtCore.SIGNAL("textChanged(QString)"), self.Buscar)
        self.connect(self.txtTelefOficina, QtCore.SIGNAL("textChanged(QString)"), self.Buscar)
        self.connect(self.txtTelefMovil, QtCore.SIGNAL("textChanged(QString)"), self.Buscar)
        self.connect(self.txtEmail, QtCore.SIGNAL("textChanged(QString)"), self.Buscar)
        self.connect(self.txtDepartamento, QtCore.SIGNAL("textChanged(QString)"), self.Buscar)
        self.connect(self.txtLocalidad, QtCore.SIGNAL("textChanged(QString)"), self.Buscar)
        self.connect(self.txtUbicacion, QtCore.SIGNAL("textChanged(QString)"), self.Buscar)
        self.connect(self.txtObservacion, QtCore.SIGNAL("textChanged(QString)"), self.Buscar)

        QtCore.QObject.connect(self.tableWidget, QtCore.SIGNAL("itemClicked(QTableWidgetItem*)"), self.clickEnTabla)

        self.establecerOrder()
        self.inicio()


    def establecerOrder(self):
        '''
        Metodo que permite establecer el orden a los objetos
        dentro de Form
        '''
        #Botones Superiores
        self.setTabOrder(self.btnNuevo, self.btnModificar)
        self.setTabOrder(self.btnModificar, self.btnEliminar)
        self.setTabOrder(self.btnEliminar, self.btnDeshacer)
        self.setTabOrder(self.btnDeshacer, self.btnLimpiar)
        self.setTabOrder(self.btnLimpiar, self.btnExportar)
        self.setTabOrder(self.btnExportar, self.btnSalir)
        
        #LineEdit 
        self.setTabOrder(self.btnSalir, self.txtId)
        self.setTabOrder(self.txtId, self.txtCedula)
        self.setTabOrder(self.txtCedula, self.txtCodigo)
        self.setTabOrder(self.txtCodigo, self.txtNombre)
        self.setTabOrder(self.txtNombre, self.txtApellido)
        self.setTabOrder(self.txtApellido, self.txtUsuarioRed)
        self.setTabOrder(self.txtUsuarioRed, self.cbxTipoContacto)
        self.setTabOrder(self.cbxTipoContacto, self.txtTelefOficina)
        self.setTabOrder(self.txtTelefOficina, self.txtTelefMovil)
        self.setTabOrder(self.txtTelefMovil, self.txtEmail)
        self.setTabOrder(self.txtEmail, self.txtDepartamento)
        self.setTabOrder(self.txtDepartamento, self.txtLocalidad)
        self.setTabOrder(self.txtLocalidad, self.txtUbicacion)
        self.setTabOrder(self.txtUbicacion, self.txtObservacion)

    def inicio(self):
        '''
        '''
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
        self.btnNuevo.setEnabled(True)
        self.btnModificar.setEnabled(False)
        self.btnEliminar.setEnabled(False)
        self.btnLimpiar.setEnabled(True)
        self.btnDeshacer.setEnabled(False)
        self.btnSalir.setEnabled(True)

        #Cambiar el Caption o Text del Boton
        self.btnNuevo.setText("&Nuevo")
        self.btnModificar.setText('&Modificar')

        #Cambiar icono del Boton Nuevo por Nuevo
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/30px-Crystal_Clear_app_List_manager.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnNuevo.setIcon(icon1)
        
        #Cambiar icono del Boton Modificar por Modificar
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/40px-Crystal_Clear_app_kedit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnModificar.setIcon(icon2)

        if sys.platform == 'win32':
            self.btnNuevo.setIconSize(QtCore.QSize(45, 45))
            self.btnModificar.setIconSize(QtCore.QSize(35, 35))
            self.btnEliminar.setIconSize(QtCore.QSize(35, 35))
            self.btnLimpiar.setIconSize(QtCore.QSize(35, 35))
            self.btnDeshacer.setIconSize(QtCore.QSize(35, 35))
            self.btnSalir.setIconSize(QtCore.QSize(35, 35))

    def Buscar(self):
        '''
        Metodo que se utiliza para realizar la busqueda segun lo que
        ingresa el usuario en las cajas de texto.
        ''' 
        #Crear aqui la Cabecera del TableWidget con el Nombre del campo y el Ancho
        listaCabecera = [('Id' ,40),
                ('Cedula' ,75),
                ('Cod' ,40 ),
                ('Nombre' , 100),
                ('Apellido' ,100),
                ('Usuario_red' ,85),
                ('Email' , 100),
                ('Telf Ofic' , 85),
                ('Telf Movil' , 95),
                ('Tipo Contacto Id' ,95),
                ('Observacion' , 150),
                ('Dpto Id' , 80),
                ('Departamento', 170),
                ('Loc Id' , 80),
                ('Localidad', 170),
                ('Ubic Id' , 80),
                ('Ubicacion', 170),
                ('Foto', 170 )]

        if self.activarBuscar:
            cadsq = self.armar_select()
            lista = self.obtener_datos(cadsq)
            self.PrepararTableWidget(len(lista), listaCabecera)  # Configurar el tableWidget
            self.InsertarRegistros(lista)  # Insertar los Registros en el TableWidget
        
    def armar_select(self):
        '''
        Metodo que permite armar la consulta select a medica que el usuario
        va tecleando en los textbox
        Parametro devuelto(1) String con la cadena sql de busqueda    
        '''

        #Campturar lo que tienne los LineEdit
        lcId = self.txtId.text()
        lcCedula = self.txtCedula.text()
        lcCodigo = self.txtCodigo.text()
        lcNombre = self.txtNombre.text()
        lcApellido = self.txtApellido.text()
        lcUsuarioRed = self.txtUsuarioRed.text()
        lcTipoContacto = self.cbxTipoContacto.currentText()
        lcTelefOficina = self.txtTelefOficina.text()
        lcTelefMovil = self.txtTelefMovil.text()
        lcEmail = self.txtEmail.text()
        lcDepartamento = self.txtDepartamento.text()
        lcLocalidad = self.txtLocalidad.text()
        lcUbicacion = self.txtUbicacion.text()
        lcObservacion = self.txtObservacion.text()
        #print 'El Nombre es:%s' % (self.txtNombre.text().toUpper())

        vId = " c.id = {0} AND ".format(lcId) if lcId else ''
        vCed = " c.cedula = {0} AND ".format(lcCedula) if lcCedula else ''
        vCod = "upper(c.codigo)  = '{0}' AND ".format(lcCodigo.toUpper()) if lcCodigo else ''
        vNom = "upper(c.nombre) like '%{0}%' AND ".format(lcNombre.toUpper()) if lcNombre else ''
        vApe = "upper(c.apellido) like '%{0}%' AND ".format(lcApellido.toUpper()) if lcApellido else ''
        vUsu = "upper(c.usuario_red) like '%{0}%' AND ".format(lcUsuarioRed.toUpper()) if lcUsuarioRed else ''
        vTipc = "upper(c.tipo_contacto) like '%{0}%' AND ".format(lcTipoContacto.toUpper()) if lcTipoContacto else ''
        vTlfO = "c.telefono_oficina like '%{0}%' AND ".format(lcTelefOficina) if lcTelefOficina else ''
        vTlfM = "c.telefono_movil like '%{0}%' AND ".format(lcTelefMovil) if lcTelefMovil else ''
        vEma = "upper(c.email) like '%{0}%' AND ".format(lcEmail.toUpper()) if lcEmail else ''
        vDpto = "upper(d.sym) like '%{0}%' AND ".format(lcDepartamento.toUpper()) if lcDepartamento else ''
        vLoc = "upper(l.sym) like '%{0}%' AND ".format(lcLocalidad.toUpper()) if lcLocalidad else ''
        vUbi = "upper(u.sym) like '%{0}%' AND ".format(lcUbicacion.toUpper()) if lcUbicacion else ''
        vObs = "upper(c.observacion) like '%{0}%' AND ".format(lcObservacion.toUpper()) if lcObservacion else ''

        campos = vId + vCed + vCod + vNom + vApe + vUsu + vTipc + vTlfO + vTlfM + vEma + vDpto + vLoc + vUbi + vObs
        
        cadenaSql = '''select 
        c.id ,c.cedula, c.codigo, c.nombre, c.apellido,c.usuario_red,
        c.email, c.telefono_oficina, c.telefono_movil, 
        c.tipo_contacto_id,
        c.observacion, 
        c.departamento_id, d.sym,
        c.localidad_id, l.sym,
        c.ubicacion_id, u.sym,
        c.foto 
        from asiste.contactos c
        left join asiste.departamento d on c.departamento_id = d.id
        left join asiste.localidad l on c.localidad_id = l.id
        left join asiste.ubicacion u on c.ubicacion_id = u.id
         where {0} c.del = 0 order by c.apellido, c.nombre
        '''.format(campos)
        
        return cadenaSql

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
    
    def PrepararTableWidget(self, cantidadReg = 0, Columnas = []):
        '''
        Parametros pasados (2) (CantidadReg: Entero) y (Columnas :Lista)
        Ej: PrepararTableWidget(50, ['ID', 'FECHA', 'PUERTO'])

        Meotodo que permite asignar y ajustar  las columnas que tendra el tablewidget
        basados en la cantidad de conlumnas y la cantidad de registros que le son
        pasados como parametro
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

        self.tableWidget.setColumnCount(len(Columnas))
        self.tableWidget.setRowCount(cantidadReg)

        #Armar Cabeceras de las Columnas
        cabecera = []
        for f in Columnas:
            nombreCampo = f[0]
            cabecera.append(nombreCampo)

        for f in Columnas:
            posicion = Columnas.index(f)
            nombreCampo = f[0]
            ancho = f[1]
            self.tableWidget.horizontalHeader().resizeSection(posicion, ancho)

        self.tableWidget.setPalette(palette)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setHorizontalHeaderLabels(cabecera)

        self.tableWidget.setSelectionMode(QtGui.QTableWidget.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtGui.QTableView.SelectRows)

    def InsertarRegistros(self, cursor):
        '''
        Metodo que permite asignarle registros al tablewidget
        parametros recibitos (1) Tipo (Lista)
        Ej:RowSource(['0', 'Carlos', 'Garcia'], ['1', 'Nairesther', 'Gomez'])
        '''

        ListaCursor = cursor
        for pos, fila in enumerate(ListaCursor):
            for posc, columna in enumerate(fila):
                self.tableWidget.setItem(pos, posc, QtGui.QTableWidgetItem(str(columna)))

    def clickEnTabla(self):
        '''
        Este metodo se activa al momento de hace click en el tableWidget y permite
        mostrar el contenido de los campos de la fila seleccionada en el tableWidget
        en los textbox bien sea para Verlos, modificarlos o Eliminarlos
    

        self.activarBuscar = False
         
        fila = self.tableWidget.currentRow()
        #total_columnas = self.tableWidget.columnCount()
        
        id = self.tableWidget.item(fila, 0).text()
        nombre = self.tableWidget.item(fila, 1).text()
        dpto = self.tableWidget.item(fila, 2).text()
        tlf = self.tableWidget.item(fila, 3).text()

        self.txtId.setText(id)
        self.txtNombre.setText(nombre)
        self.txtDepartamento.setText(dpto)
        self.txtTelefono.setText(tlf) 

        self.btnModificar.setEnabled(True)
        self.btnEliminar.setEnabled(True)
        '''
        pass

    def limpiarText(self):
        '''
        Limpia los QlineEdit o Textbox
        '''
        self.txtId.clear()
        self.txtCedula.clear()
        self.txtCodigo.clear()
        self.txtNombre.clear()
        self.txtApellido.clear()
        self.txtUsuarioRed.clear()
        self.cbxTipoContacto.clear()
        self.txtTelefOficina.clear()
        self.txtTelefMovil.clear()
        self.txtEmail.clear()
        self.txtDepartamento.clear()
        self.txtLocalidad.clear()
        self.txtUbicacion.clear()
        self.txtObservacion.clear()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    forma = ui_()
    forma.show()
    sys.exit(app.exec_())
