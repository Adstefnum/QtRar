from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import os

class zipWindow(QMainWindow):
       
   def __init__(self):
    super(zipWindow, self).__init__()
    self.setGeometry(50,50,350,80)
    self.setWindowTitle("QtRar")
    #self.setWindowIcon(QtGui.QIcon)

    destBtn = QPushButton("Choose Destination",self)
    destBtn.resize(120,30)
    destBtn.move(25,40)
    destBtn.clicked.connect(self.change_dir)

    self.label = QLabel("Extract zip",self)
    self.label.resize(300,30)
    self.label.move(25,10)


    extBtn = QPushButton("Choose Zip and Extract",self)
    extBtn.resize(120,30)
    extBtn.move(190,40)
    extBtn.clicked.connect(self.proceed)


    self.show()

   def change_dir(self):
       name = str(QFileDialog.getExistingDirectory(self,"Select Directory"))
       os.chdir(name)

       return name

   def proceed(self):
       name,dummy = QFileDialog.getOpenFileName(self,'Open File',
    options = QFileDialog.DontUseNativeDialog)
    
       try:
           os.system("tar -xf" + str(name))
           return self.label.setText(name + " has been extracted")

       except Exception as e:
           return "".format(e)

    
app = QApplication(sys.argv)
gui = zipWindow()
sys.exit(app.exec_())
