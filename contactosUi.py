# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/contactos.ui'
#
# Created: Sat Mar 16 06:13:54 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1384, 445)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(220, 222, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 222, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        Form.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../img/contactos/user-6-16.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtGui.QSplitter(Form)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.btnNuevo = QtGui.QPushButton(self.splitter)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../img/30px-Crystal_Clear_app_List_manager.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnNuevo.setIcon(icon1)
        self.btnNuevo.setObjectName("btnNuevo")
        self.btnModificar = QtGui.QPushButton(self.splitter)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../img/40px-Crystal_Clear_app_kedit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnModificar.setIcon(icon2)
        self.btnModificar.setObjectName("btnModificar")
        self.btnEliminar = QtGui.QPushButton(self.splitter)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../img/30px_1 (514).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnEliminar.setIcon(icon3)
        self.btnEliminar.setObjectName("btnEliminar")
        self.btnDeshacer = QtGui.QPushButton(self.splitter)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../img/40px_reload.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnDeshacer.setIcon(icon4)
        self.btnDeshacer.setObjectName("btnDeshacer")
        self.btnLimpiar = QtGui.QPushButton(self.splitter)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../img/erase.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnLimpiar.setIcon(icon5)
        self.btnLimpiar.setObjectName("btnLimpiar")
        self.btnExportar = QtGui.QPushButton(self.splitter)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../img/OfficeExcel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnExportar.setIcon(icon6)
        self.btnExportar.setObjectName("btnExportar")
        self.btnSalir = QtGui.QPushButton(self.splitter)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("../img/25px_exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSalir.setIcon(icon7)
        self.btnSalir.setObjectName("btnSalir")
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 16)
        self.lblId = QtGui.QLabel(Form)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(72, 32, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 32, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 126))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.lblId.setPalette(palette)
        self.lblId.setObjectName("lblId")
        self.gridLayout.addWidget(self.lblId, 1, 0, 1, 2)
        self.lblCedula = QtGui.QLabel(Form)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(72, 32, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 32, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 126))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.lblCedula.setPalette(palette)
        self.lblCedula.setObjectName("lblCedula")
        self.gridLayout.addWidget(self.lblCedula, 1, 2, 1, 2)
        self.lblCodigo = QtGui.QLabel(Form)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(72, 32, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 32, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 126))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.lblCodigo.setPalette(palette)
        self.lblCodigo.setObjectName("lblCodigo")
        self.gridLayout.addWidget(self.lblCodigo, 1, 4, 1, 1)
        self.lblNombre = QtGui.QLabel(Form)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(72, 32, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 32, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 126))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.lblNombre.setPalette(palette)
        self.lblNombre.setObjectName("lblNombre")
        self.gridLayout.addWidget(self.lblNombre, 1, 7, 1, 2)
        self.lblApellido = QtGui.QLabel(Form)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(72, 32, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 32, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 126))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.lblApellido.setPalette(palette)
        self.lblApellido.setObjectName("lblApellido")
        self.gridLayout.addWidget(self.lblApellido, 1, 11, 1, 1)
        self.lblUsuarioRed = QtGui.QLabel(Form)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(72, 32, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 32, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 126))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.lblUsuarioRed.setPalette(palette)
        self.lblUsuarioRed.setObjectName("lblUsuarioRed")
        self.gridLayout.addWidget(self.lblUsuarioRed, 1, 13, 1, 2)
        self.lblTipoContacto = QtGui.QLabel(Form)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(72, 32, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 32, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 126))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.lblTipoContacto.setPalette(palette)
        self.lblTipoContacto.setObjectName("lblTipoContacto")
        self.gridLayout.addWidget(self.lblTipoContacto, 1, 15, 1, 2)
        self.txtId = QtGui.QLineEdit(Form)
        self.txtId.setObjectName("txtId")
        self.gridLayout.addWidget(self.txtId, 2, 0, 1, 2)
        self.txtCedula = QtGui.QLineEdit(Form)
        self.txtCedula.setObjectName("txtCedula")
        self.gridLayout.addWidget(self.txtCedula, 2, 2, 1, 2)
        self.txtCodigo = QtGui.QLineEdit(Form)
        self.txtCodigo.setObjectName("txtCodigo")
        self.gridLayout.addWidget(self.txtCodigo, 2, 4, 1, 3)
        self.txtNombre = QtGui.QLineEdit(Form)
        self.txtNombre.setObjectName("txtNombre")
        self.gridLayout.addWidget(self.txtNombre, 2, 7, 1, 4)
        self.txtApellido = QtGui.QLineEdit(Form)
        self.txtApellido.setObjectName("txtApellido")
        self.gridLayout.addWidget(self.txtApellido, 2, 11, 1, 2)
        self.txtUsuario_Red = QtGui.QLineEdit(Form)
        self.txtUsuario_Red.setObjectName("txtUsuario_Red")
        self.gridLayout.addWidget(self.txtUsuario_Red, 2, 13, 1, 2)
        self.cbxTipoContacto = QtGui.QComboBox(Form)
        self.cbxTipoContacto.setEditable(False)
        self.cbxTipoContacto.setObjectName("cbxTipoContacto")
        self.gridLayout.addWidget(self.cbxTipoContacto, 2, 15, 1, 2)
        self.lblTelefonoOficina = QtGui.QLabel(Form)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(72, 32, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 32, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 126))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.lblTelefonoOficina.setPalette(palette)
        self.lblTelefonoOficina.setObjectName("lblTelefonoOficina")
        self.gridLayout.addWidget(self.lblTelefonoOficina, 3, 0, 1, 3)
        self.lblTelefonoMovil = QtGui.QLabel(Form)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(72, 32, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 32, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 126))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.lblTelefonoMovil.setPalette(palette)
        self.lblTelefonoMovil.setObjectName("lblTelefonoMovil")
        self.gridLayout.addWidget(self.lblTelefonoMovil, 3, 3, 1, 2)
        self.lblEmail = QtGui.QLabel(Form)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(72, 32, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 32, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 126))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.lblEmail.setPalette(palette)
        self.lblEmail.setObjectName("lblEmail")
        self.gridLayout.addWidget(self.lblEmail, 3, 5, 1, 4)
        self.lblDpto = QtGui.QLabel(Form)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(72, 32, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 32, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 126))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.lblDpto.setPalette(palette)
        self.lblDpto.setObjectName("lblDpto")
        self.gridLayout.addWidget(self.lblDpto, 3, 9, 1, 3)
        self.lblLocalidad = QtGui.QLabel(Form)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(72, 32, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 32, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 126))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.lblLocalidad.setPalette(palette)
        self.lblLocalidad.setObjectName("lblLocalidad")
        self.gridLayout.addWidget(self.lblLocalidad, 3, 13, 1, 2)
        self.txtTelefono_Oficina = QtGui.QLineEdit(Form)
        self.txtTelefono_Oficina.setObjectName("txtTelefono_Oficina")
        self.gridLayout.addWidget(self.txtTelefono_Oficina, 4, 0, 1, 3)
        self.txtTelefono_Movil = QtGui.QLineEdit(Form)
        self.txtTelefono_Movil.setObjectName("txtTelefono_Movil")
        self.gridLayout.addWidget(self.txtTelefono_Movil, 4, 3, 1, 2)
        self.txtEmail = QtGui.QLineEdit(Form)
        self.txtEmail.setObjectName("txtEmail")
        self.gridLayout.addWidget(self.txtEmail, 4, 5, 1, 4)
        self.txtIdDepartamento = QtGui.QLineEdit(Form)
        self.txtIdDepartamento.setFocusPolicy(QtCore.Qt.NoFocus)
        self.txtIdDepartamento.setObjectName("txtIdDepartamento")
        self.gridLayout.addWidget(self.txtIdDepartamento, 4, 9, 1, 1)
        self.txtDepartamento = QtGui.QLineEdit(Form)
        self.txtDepartamento.setObjectName("txtDepartamento")
        self.gridLayout.addWidget(self.txtDepartamento, 4, 10, 1, 2)
        self.btnBuscarDpto = QtGui.QPushButton(Form)
        self.btnBuscarDpto.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("../img/contactos/apartment-2-16.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBuscarDpto.setIcon(icon8)
        self.btnBuscarDpto.setObjectName("btnBuscarDpto")
        self.gridLayout.addWidget(self.btnBuscarDpto, 4, 12, 1, 1)
        self.txtIdLocalidad = QtGui.QLineEdit(Form)
        self.txtIdLocalidad.setFocusPolicy(QtCore.Qt.NoFocus)
        self.txtIdLocalidad.setObjectName("txtIdLocalidad")
        self.gridLayout.addWidget(self.txtIdLocalidad, 4, 13, 1, 1)
        self.txtLocalidad = QtGui.QLineEdit(Form)
        self.txtLocalidad.setObjectName("txtLocalidad")
        self.gridLayout.addWidget(self.txtLocalidad, 4, 14, 1, 2)
        self.btnBuscarLocalidad = QtGui.QPushButton(Form)
        self.btnBuscarLocalidad.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("../img/contactos/map-4-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBuscarLocalidad.setIcon(icon9)
        self.btnBuscarLocalidad.setObjectName("btnBuscarLocalidad")
        self.gridLayout.addWidget(self.btnBuscarLocalidad, 4, 16, 1, 1)
        self.lblUbicacion = QtGui.QLabel(Form)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(72, 32, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 32, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 126))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.lblUbicacion.setPalette(palette)
        self.lblUbicacion.setObjectName("lblUbicacion")
        self.gridLayout.addWidget(self.lblUbicacion, 5, 0, 1, 4)
        self.lblObservacion = QtGui.QLabel(Form)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(72, 32, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 32, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 126))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.lblObservacion.setPalette(palette)
        self.lblObservacion.setObjectName("lblObservacion")
        self.gridLayout.addWidget(self.lblObservacion, 5, 8, 1, 4)
        self.txtIdUbicacion = QtGui.QLineEdit(Form)
        self.txtIdUbicacion.setFocusPolicy(QtCore.Qt.NoFocus)
        self.txtIdUbicacion.setObjectName("txtIdUbicacion")
        self.gridLayout.addWidget(self.txtIdUbicacion, 6, 0, 1, 1)
        self.txtUbicacion = QtGui.QLineEdit(Form)
        self.txtUbicacion.setObjectName("txtUbicacion")
        self.gridLayout.addWidget(self.txtUbicacion, 6, 1, 1, 5)
        self.btnUbicacionBuscar = QtGui.QPushButton(Form)
        self.btnUbicacionBuscar.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("../img/contactos/building-5-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnUbicacionBuscar.setIcon(icon10)
        self.btnUbicacionBuscar.setObjectName("btnUbicacionBuscar")
        self.gridLayout.addWidget(self.btnUbicacionBuscar, 6, 6, 1, 2)
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 6, 8, 1, 9)
        spacerItem = QtGui.QSpacerItem(20, 30, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem, 7, 3, 1, 1)
        self.tableWidget = QtGui.QTableWidget(Form)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 8, 0, 1, 17)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.btnNuevo.setText(QtGui.QApplication.translate("Form", "   &Nuevo", None, QtGui.QApplication.UnicodeUTF8))
        self.btnModificar.setText(QtGui.QApplication.translate("Form", "&Modificar", None, QtGui.QApplication.UnicodeUTF8))
        self.btnEliminar.setText(QtGui.QApplication.translate("Form", " &Eliminar", None, QtGui.QApplication.UnicodeUTF8))
        self.btnDeshacer.setText(QtGui.QApplication.translate("Form", " &Deshacer", None, QtGui.QApplication.UnicodeUTF8))
        self.btnLimpiar.setText(QtGui.QApplication.translate("Form", "  &Limpiar", None, QtGui.QApplication.UnicodeUTF8))
        self.btnExportar.setText(QtGui.QApplication.translate("Form", " &Exportar", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSalir.setText(QtGui.QApplication.translate("Form", "    &Salir", None, QtGui.QApplication.UnicodeUTF8))
        self.lblId.setText(QtGui.QApplication.translate("Form", "ID", None, QtGui.QApplication.UnicodeUTF8))
        self.lblCedula.setText(QtGui.QApplication.translate("Form", "Cedula", None, QtGui.QApplication.UnicodeUTF8))
        self.lblCodigo.setText(QtGui.QApplication.translate("Form", "Codigo", None, QtGui.QApplication.UnicodeUTF8))
        self.lblNombre.setText(QtGui.QApplication.translate("Form", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.lblApellido.setText(QtGui.QApplication.translate("Form", "Apellido", None, QtGui.QApplication.UnicodeUTF8))
        self.lblUsuarioRed.setText(QtGui.QApplication.translate("Form", "Usuario de Red", None, QtGui.QApplication.UnicodeUTF8))
        self.lblTipoContacto.setText(QtGui.QApplication.translate("Form", "Tipo de Contacto", None, QtGui.QApplication.UnicodeUTF8))
        self.lblTelefonoOficina.setText(QtGui.QApplication.translate("Form", "Telefono Oficina", None, QtGui.QApplication.UnicodeUTF8))
        self.lblTelefonoMovil.setText(QtGui.QApplication.translate("Form", "Telefono Movil", None, QtGui.QApplication.UnicodeUTF8))
        self.lblEmail.setText(QtGui.QApplication.translate("Form", "Correo electronico", None, QtGui.QApplication.UnicodeUTF8))
        self.lblDpto.setText(QtGui.QApplication.translate("Form", "Departamento", None, QtGui.QApplication.UnicodeUTF8))
        self.lblLocalidad.setText(QtGui.QApplication.translate("Form", "Localidad", None, QtGui.QApplication.UnicodeUTF8))
        self.lblUbicacion.setText(QtGui.QApplication.translate("Form", "Ubicacion: Area o Piso", None, QtGui.QApplication.UnicodeUTF8))
        self.lblObservacion.setText(QtGui.QApplication.translate("Form", "Observacion", None, QtGui.QApplication.UnicodeUTF8))

