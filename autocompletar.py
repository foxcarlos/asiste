import sys
from PyQt4.QtCore import Qt
from PyQt4.QtGui import QApplication, QCompleter, QLineEdit, QStringListModel

class textbox(QLineEdit):
    def __init__(self):
        pass

    def focusInEvent(self, e): 
       msg = QMessageBox(QMessageBox.Waring, 'Titulo', 'Mensahe')
       msg.Exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    edit = textbox()  # QLineEdit()  # Se instancia la clase para Qlineedit
    lista = ('Carlos', 'Carla', 'Alberto', 'Adrian', 'garcia', 'Diaz')  # Se crea la lista que se mostrara
    autoCompletar = QCompleter(lista)  # se define la lista 
    autoCompletar.setCaseSensitivity(Qt.CaseInsensitive)  # se desactiva el case sensitive
    edit.setCompleter(autoCompletar)  # Se asigna la lista al QlineEdit
    edit.show()
    sys.exit(app.exec_())
