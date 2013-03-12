import sys
from PyQt4.QtCore import Qt
from PyQt4.QtGui import QApplication, QCompleter, QLineEdit, QStringListModel


if __name__ == "__main__":
    app = QApplication(sys.argv)
    edit = QLineEdit()
    lista = ('Carlos', 'Carla', 'Alberto', 'Adrian', 'garcia', 'Diaz')
    autoCompletar = QCompleter(lista)
    autoCompletar.setCaseSensitivity(Qt.CaseInsensitive)
    edit.setCompleter(autoCompletar)
    edit.show()
    sys.exit(app.exec_())
