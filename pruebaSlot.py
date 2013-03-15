import sys
import time
from PyQt4.QtCore import * 
from PyQt4.QtGui import * 

#################################################################### 
class MyWindow(QWidget): 
    def __init__(self, *args): 
        QWidget.__init__(self, *args)

        self.label = QLabel(" ")
        self.boton = QPushButton()

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.boton)
        self.setLayout(layout)
        
        objeto = self.boton
        objeto = self.label

        self.connect(objeto, SIGNAL("clicked()"),
                     self.update_label)
        
        self.boton.emit(SIGNAL("clicked()"), 3)
        

    def update_label(self, value1):
        print value1
        #self.label.setText(value1 + " " + value2)

####################################################################
if __name__ == "__main__": 
    app = QApplication(sys.argv) 
    w = MyWindow() 
    w.show() 
    sys.exit(app.exec_())
