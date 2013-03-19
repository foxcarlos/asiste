# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtCore, QtGui


class ui_(QtGui.QWidget):
    def __init__(self):
        super(ui_, self).__init__()
        
        #Se crean los Botones de mantenimiento superiores
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

        #Campo ID
        self.hlId = QtGui.QHBoxLayout() 
        self.lblId = QtGui.QLabel('ID:')
        self.txtId = QtGui.QLineEdit()
        self.spacerId = QtGui.QSpacerItem(500, 20)
        self.hlId.addWidget(self.txtId)
        self.hlId.addItem(self.spacerId)

        #Campo Cedula
        self.hlCedula = QtGui.QHBoxLayout()
        self.lblCedula = QtGui.QLabel('Cedula:')
        self.txtCedula = QtGui.QLineEdit()
        self.spacerCedula = QtGui.QSpacerItem(400, 20)
        self.hlCedula.addWidget(self.txtCedula)
        self.hlCedula.addItem(self.spacerCedula)

        #Campo Codigo
        self.hlCodigo = QtGui.QHBoxLayout()
        self.lblCodigo = QtGui.QLabel('Codigo:')
        self.txtCodigo = QtGui.QLineEdit()
        self.spacerCodigo = QtGui.QSpacerItem(400, 20)
        self.hlCodigo.addWidget(self.txtCodigo)
        self.hlCodigo.addItem(self.spacerCodigo)

        #Campo Nombre
        self.lblNombre = QtGui.QLabel('Nombre')
        self.txtNombre = QtGui.QLineEdit()
        self.hlNombre = QtGui.QHBoxLayout()
        self.hlNombre.addWidget(self.txtNombre)

        #Campo Apellido
        self.lblApellido = QtGui.QLabel('Apellido')
        self.txtApellido = QtGui.QLineEdit()
        self.hlApellido = QtGui.QHBoxLayout()
        self.hlApellido.addWidget(self.txtApellido)

        #Campo Usuario
        self.hlUsuarioRed = QtGui.QHBoxLayout()
        self.lblUsuarioRed = QtGui.QLabel('Usuario de Red')
        self.txtUsuarioRed = QtGui.QLineEdit()
        self.spacerUsuarioRed = QtGui.QSpacerItem(400, 20)
        self.hlUsuarioRed.addWidget(self.txtUsuarioRed)
        self.hlUsuarioRed.addItem(self.spacerUsuarioRed)


        #Campo Tipo Contacto
        self.lblTipoContacto = QtGui.QLabel('Tipo de Contacto')
        self.txtTipoContacto = QtGui.QLineEdit()

        #Campo Telef Oficina
        self.lblTelefOficina = QtGui.QLabel('Telef. Oficina')
        self.txtTelefOficina = QtGui.QLineEdit()

        #Campo Telef Movil
        self.lblTelefMovil = QtGui.QLabel('Telef. Movil')
        self.txtTelefMovil = QtGui.QLineEdit()

        #Campo Email
        self.lblEmail = QtGui.QLabel('Email')
        self.txtEmail = QtGui.QLineEdit()

        #Campo Departamento
        self.lblDepartamento = QtGui.QLabel('Departamento')
        self.txtDepartamento = QtGui.QLineEdit()

        #Campo Localidad
        self.lblLocalidad = QtGui.QLabel('Localidad')
        self.txtLocalidad = QtGui.QLineEdit()

        #Campo Ubicacion
        self.lblUbicacion = QtGui.QLabel('Ubicacion:')
        self.txtUbicacion = QtGui.QLineEdit()

        #Campo Observacion
        self.lblObservacion = QtGui.QLabel('Observacion:')
        self.txtObservacion = QtGui.QLineEdit()

        self.tableWidget = QtGui.QTableWidget()

        #Se insertan los Objetos en el Grid Loyouts de todo el Formulario
        self.gl = QtGui.QGridLayout()
        self.gl.addLayout(self.hl, 0, 1, 1, 8)
        self.gl.addWidget(self.line, 1, 1, 1, 8)
        
        self.gl.addWidget(self.lblId, 2, 1)
        self.gl.addLayout(self.hlId, 2,2)
        
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
        self.gl.addWidget(self.txtTipoContacto, 8, 2)

        self.gl.addWidget(self.lblTelefOficina, 9, 1)
        self.gl.addWidget(self.txtTelefOficina, 9, 2)

        self.gl.addWidget(self.lblTelefMovil, 10, 1)
        self.gl.addWidget(self.txtTelefMovil, 10, 2)

        self.gl.addWidget(self.lblEmail, 11, 1)
        self.gl.addWidget(self.txtEmail, 11, 2)

        self.gl.addWidget(self.lblDepartamento, 12, 1)
        self.gl.addWidget(self.txtDepartamento, 12, 2)

        self.gl.addWidget(self.lblLocalidad, 13, 1)
        self.gl.addWidget(self.txtLocalidad, 13, 2)

        self.gl.addWidget(self.lblUbicacion, 14, 1)
        self.gl.addWidget(self.txtUbicacion, 14, 2)

        self.gl.addWidget(self.lblObservacion, 15, 1)
        self.gl.addWidget(self.txtObservacion, 15, 2)

        self.setGeometry(0, 0, 1091, 496)

        self.setLayout(self.gl)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    forma = ui_()
    forma.show()
    sys.exit(app.exec_())

