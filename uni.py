from PyQt5 import QtCore, QtGui, uic  # imports all the releavnt functions of modules pyqt5 so the    #    
from PyQt5.QtCore import *            # graphical user interface can be created in QtDesigner which   #   
from PyQt5.QtGui import *             # will include widgets such buttons,entryboxes and messageboxes #   
from PyQt5 import QtWidgets           # and which will be linked with main framework in python.       # 
from PyQt5.QtWidgets import QApplication,QWidget, QPushButton, QMessageBox 
from PyQt5 import uic  # uic function is to load the Qtdesigner file and link it with the main program #


LoginScreen = uic.loadUiType('# The name of the file that need to be loaded #' ) [0] 
# to load Qtdesigner file a global variable will decleared #  

class LoginClass(QtWidgets.QMainWindow, window1):
    #This will be the class to creat all the GUI windows , the name of the class will diffrent
    #will correspond to the it's function. #
    # the parameter will the variable decleared to load the Qtdesigner file# 
    def __init__(self, parent=None): # initiating the class 
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
             
        #############################################################################################
        # Code for diffrent classes will tailored for each window as it's the blueprint 
        ##############################################################################################
        
        # screen title
        self.setWindowTitle('   ')
        
        ## WIDGETS ##
        
        # all the relevant widgets for the GUI window will linked below using self. #
    
        ## METHORDS ##
        #all the methords will below with the parameter self and specific parameter
        # for each methord#     

             
#########################################################################################################
# code to create app and launch it
########################################################################################################
app = QtWidgets.QApplication(sys.argv)
LoginWindow = LoginClass(None) #All the specific window will be created as object of the relevant WindowClass #
LoginWindow.show()  # This is an attibute for all the classes which will display the GUI window # 
app.exec_()
