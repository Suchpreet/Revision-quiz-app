import sys, os, webbrowser # I imported modules os , sys which start and close programs with GUI  #
import sqlite3 as lite
from PyQt5 import QtCore, QtGui, uic  # imports all the releavnt functions of modules pyqt5 so the    #    
from PyQt5.QtCore import *            # graphical user interface can be created in QtDesigner which   #   
from PyQt5.QtGui import *             # will include widgets such buttons,entryboxes and messageboxes #   
from PyQt5 import QtWidgets          # and which will be linked with main framework in python.       # 
from PyQt5.QtWidgets import QApplication,QWidget, QPushButton, QMessageBox
from PyQt5 import uic  # uic function is to load the Qtdesigner file and link it with the main program #
from PyQt5.QtWidgets import QLineEdit
import random
import csv

def csv2List(fileName):
    listName = []
    with open(fileName) as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            listName.append(row)
    return listName


#GLOBAL VARIABLES#

MainScreen = uic.loadUiType("mainScreen.ui")[0]
# To load Qtdesigner file of the Main window, a global variable MainScreen is decleared #

LoginScreen = uic.loadUiType("loginScreen.ui")[0]
# To load Qtdesigner file of the Login window, a global variable LoginScreen is decleared #  

RegisterScreen = uic.loadUiType("registerScreen.ui")[0]
# To load Qtdesigner file of the Register window, a global variable RegisterScreen is decleared #

InfoScreen = uic.loadUiType("infoScreen.ui")[0]
# To load Qtdesigner file of the Information window, a global variable InfoScreen is decleared # 

HomeScreen = uic.loadUiType("homeScreen.ui")[0]
# To load Qtdesigner file of the Home window, a global variable HomeScreen is decleared #  

BlogScreen = uic.loadUiType("blogScreen.ui")[0]
# To load Qtdesigner file of the Blog window, a global variable BlogScreen is decleared #   

QuizScreen = uic.loadUiType("quizScreen.ui")[0]
# To load Qtdesigner file of the Quiz window, a global variable QuizScreen is decleared #   

ReportScreen = uic.loadUiType("reportScreen.ui")[0]
# To load Qtdesigner file of the Report window, a global variable MainScreen is decleared #    

ExamScreen = uic.loadUiType("examScreen.ui")[0]
# To load Qtdesigner file of the Exam window, a global variable MainScreen is decleared #  

FilterScreen = uic.loadUiType("filterScreen.ui")[0]
# To load Qtdesigner file of the Filter window, a global variable MainScreen is decleared #

AdminScreen = uic.loadUiType("adminScreen.ui")[0]
# To load Qtdesigner file of the Filter window, a global variable MainScreen is decleared #   



class MainClass(QtWidgets.QMainWindow, MainScreen):
     #This will be the class to creat the GUI for the Main Window #
    # the parameter is the variable decleared as MainScreen to load the Qtdesigner file for the Main Window# 
        def __init__(self, parent=None): # initiating the class
            QtWidgets.QMainWindow.__init__(self, parent)
            self.setupUi(self)
            
            #variables & constants
           
            
            #title
            self.setWindowTitle('RevisionBuddy')
            
            #Buttons
            self.LoginBut.clicked.connect(self.OpenLoginWindow)
            
            self.SignUpBut.clicked.connect(self.OpenRegisterWindow)
            
            self.InfoBut.clicked.connect(self.OpenInfoWindow)
            
            
        def OpenLoginWindow(self):
            MainWindow.hide()
            LoginWindow.show()
            
            
        def OpenRegisterWindow(self):
            MainWindow.hide()
            RegisterWindow.show()
            
        def OpenInfoWindow(self):
            MainWindow.hide()
            InfoWindow.show()
             
class LoginClass(QtWidgets.QMainWindow, LoginScreen):
      #This will be the class to creat the GUI for the Login Window #
    # the parameter is the variable decleared as LoginScreen to load the Qtdesigner file for the Login Window# 
        def __init__(self, parent=None): # initiating the class
            QtWidgets.QMainWindow.__init__(self, parent)
            self.setupUi(self)
            
            #title
            self.setWindowTitle('RevisionBuddy/Login')
            

            
            #Button
            self.GoBackBut.clicked.connect(self.OpenMainWindow)
            self.LoginBut.clicked.connect(self.LoginNow)
            
            self.ShowPasswordBut.setCheckable(True)
            self.ShowPasswordBut.toggle()
            
            self.ShowPasswordBut.clicked.connect(self.ShowPassword)
            
            self.PasswordEntry1.returnPressed.connect(self.LoginNow)
            self.uname = 0
            
            
            
   
                    
            
            # Methords
            
        def OpenMainWindow(self):
            LoginWindow.hide()
            MainWindow.show()
            
        def ShowPassword(self, state):
            if state:
                self.PasswordEntry1.setEchoMode(QLineEdit.Normal)
            else:
                self.PasswordEntry1.setEchoMode(QLineEdit.Password)
                

        
        def LoginNow(self):
            
            con = lite.connect("Database.db")
            cur = con.cursor()
            clientsDatasql = "select username, password from clients"
            cur.execute(clientsDatasql)              
            myClients = cur.fetchall()

#           print(myClients)
            uname = self.UsernameEntry1.text()
            pword = self.PasswordEntry1.text()
            self.uname = self.UsernameEntry1.text()

        
            
            loginToCheck = (uname,pword)


            succesful = False

            for dataPair in myClients:
                if dataPair == loginToCheck:
                    succesful = True
                    
                    
                

            if succesful == True:
                HomeWindow.show()
                LoginWindow.hide()
                FilterWindow.AllTopicButton.setChecked(True)
                FilterWindow.CheckAllTopics()
                self.UsernameEntry1.setText("") # Clears the username entry box
                self.PasswordEntry1.setText("") # Clears the password entry box
                
                


            else:
                QMessageBox.warning(self, 'Error', 'Wrong Username or password .')
                return
                
                
            
               
            
            
            
class InfoClass(QtWidgets.QMainWindow, InfoScreen):
      #This will be the class to creat the GUI for the Login Window #
    # the parameter is the variable decleared as LoginScreen to load the Qtdesigner file for the Login Window# 
        def __init__(self, parent=None): # initiating the class
            QtWidgets.QMainWindow.__init__(self, parent)
            self.setupUi(self)
            
            #title
            self.setWindowTitle('RevisionBuddy/Info')
            
                 #Button
            self.GoBackBut.clicked.connect(self.OpenMainWindow)
            
            # Methords
            
        def OpenMainWindow(self):
            InfoWindow.hide()
            MainWindow.show()
            

class RegisterClass(QtWidgets.QMainWindow, RegisterScreen):
      #This will be the class to creat the GUI for the Register Window #
    # the parameter is the variable decleared as RegisterScreen to load the Qtdesigner file for the Register Window#
        def __init__(self, parent=None):# initiating the class
            QtWidgets.QMainWindow.__init__(self, parent)
            self.setupUi(self)
            
            
        #title
            self.setWindowTitle('RevisionBuddy/Register')
            
             #Button
            self.GoBackBut.clicked.connect(self.OpenMainWindow)
            self.RegisterBut.clicked.connect(self.RegisterMe)
            # Methords
            
        def OpenMainWindow(self):
            RegisterWindow.hide()
            MainWindow.show()
            
        def RegisterMe(self):           
            con = lite.connect("Database.db")
            cur = con.cursor()
            clientsDatasql = "select client_id from clients"
            cur.execute(clientsDatasql)              
            myClients = cur.fetchall()

            ClientId = int(len(myClients)+1)
#             print(ClientId)

            uname = self.UsernameEntry.text()
            pword = self.PasswordEntry.text()
            cpword = self.ConfirmPasswordEntry.text()
            self.username = uname
            
            
            if pword != cpword :
        # If username or password is empty, show error message
                QMessageBox.warning(self, 'Error', 'passwords are not same .')
                return
           
    
            if not uname or not pword:
        # If username or password is empty, show error message
                QMessageBox.warning(self, 'Error', 'Username or password cannot be empty.')
                return
            
            if "'" in uname or "'" in pword:
        # If username or password contain single quotes, show error message
                QMessageBox.warning(self, 'Error', "Username or password can't contain single quotes.")
                return
    
            if len(pword) < 1:
        # If password length is less than 8 characters, show error message
                QMessageBox.warning(self, 'Error', 'Password must be at least 1 characters long.')
                return
    
    # Check if username already exists in the database
            existing_username_sql = "SELECT * FROM clients WHERE username=?"
            cur.execute(existing_username_sql, (uname,))
            if cur.fetchone():
        # If username already exists, show error message
                QMessageBox.warning(self, 'Error', 'Username already exists.')
                return
    
    # If all checks passed, insert the data into the database
            
            con = lite.connect("Database.db")
            cur = con.cursor()
            sql = "INSERT INTO clients VALUES(?,?,?,?,?,?)"
            cur.execute(sql, (ClientId,uname, pword,('0'),('0'),('0')))
            con.commit()
            
            self.UsernameEntry.setText("") # Clears the username entry box
            self.PasswordEntry.setText("") # Clears the password entry box
            RegisterWindow.hide()
            MainWindow.show()
            
        



class HomeClass(QtWidgets.QMainWindow, HomeScreen):
  #This will be the class to creat the GUI for the Home Window #
    # the parameter is the variable decleared as HomeScreen to load the Qtdesigner file for the Home Window# 
 
        def __init__(self, parent=None): # initiating the class
            QtWidgets.QMainWindow.__init__(self, parent)
            self.setupUi(self)
            
            #title
            self.setWindowTitle('RevisionBuddy/Home')
            #buttons
            
            self.QuizBut.clicked.connect(self.OpenQuizWindow)
            
            self.ReportBut.clicked.connect(self.OpenReportWindow)
            
            self.TopicFilterBut.clicked.connect(self.OpenFilterWindow)
            
            self.SignOutBut.clicked.connect(self.OpenMainWindow)
            
            self.ExamBut.clicked.connect(self.OpenExam)
            
            self.BlogBut.clicked.connect(self.OpenBlog)
            
                    
            
        def OpenQuizWindow(self):
            HomeWindow.hide()
            QuizWindow.show()
            QuizWindow.DisplayQuestion()
            QuizWindow.GetScore()
            QuizWindow.GetAttempts()
            
            
            
            
        
        def OpenReportWindow(self):
            HomeWindow.hide()
            ReportWindow.show()
            
            
        def OpenFilterWindow(self):
            HomeWindow.hide()
            FilterWindow.show()
            
        def OpenMainWindow(self):
            HomeWindow.hide()
            MainWindow.show()
            
            
        def OpenExam(self):
            webbrowser.open("https://www.physicsandmathstutor.com/past-papers/a-level-computer-science/")
            
        def OpenBlog(self):
            webbrowser.open("https://www.pmt.education/blog/")
            
        
            
            
class QuizClass(QtWidgets.QMainWindow, QuizScreen):
       #This will be the class to creat the GUI for the Quiz Window #
    # the parameter is the variable decleared as QuizScreen to load the Qtdesigner file for the Quiz Window#
        def __init__(self, parent=None): # initiating the class
            
            QtWidgets.QMainWindow.__init__(self, parent)
            self.setupUi(self)
            
            #title
            self.setWindowTitle('RevisionBuddy/Quiz')
            self.DisplayedQuestions = []
            self.SelectedTopics = []
            
            # Button
            
            self.HomeBut.clicked.connect(self.OpenHomeWindow)
            self.OptionBut1.clicked.connect(lambda: self.CheckAnswer(self.OptionBut1.text()))
            self.OptionBut2.clicked.connect(lambda: self.CheckAnswer(self.OptionBut2.text()))
            self.OptionBut3.clicked.connect(lambda: self.CheckAnswer(self.OptionBut3.text()))
            self.OptionBut4.clicked.connect(lambda: self.CheckAnswer(self.OptionBut4.text()))
            
            
           #Methords
            
        def OpenHomeWindow(self):
            QuizWindow.hide()
            HomeWindow.show()

        def GetQuestions(self):
            with lite.connect("Database.db") as con:
                cur = con.cursor()
                questions_sql = "SELECT * FROM questions"
                cur.execute(questions_sql)
                questions = cur.fetchall()
                return questions
        
        
        def DisplayQuestion(self):
            questions = self.GetQuestions()
            print(self.SelectedTopics)
            self.SelectedTopics=['1.2','1.3','1.4']
            if questions:
                self.question = random.choice(questions)
                while self.question[1] in self.DisplayedQuestions or self.question[6] not in self.SelectedTopics:
                    self.question = random.choice(questions)
                self.QuestionLabel.setText(self.question[1])
                options = [self.question[2], self.question[3], self.question[4], self.question[5]]
                random.shuffle(options)
                self.OptionBut1.setText(options[0])
                self.OptionBut2.setText(options[1])
                self.OptionBut3.setText(options[2])
                self.OptionBut4.setText(options[3])
                
                
        
        
                
                
                
        def GetScore(self):
 # Retrieve the current score from the database    
            con = lite.connect("Database.db")
            cur = con.cursor()
            score_sql = "SELECT score FROM clients WHERE username=?"
            cur.execute(score_sql, (LoginWindow.uname,))
            score = cur.fetchone()
            return score
            
        def GetAttempts(self): 
    # Retrieve the current score from the database
            con = lite.connect("Database.db")
            cur = con.cursor()
            attempts_sql = "SELECT attempts FROM clients WHERE username=?"
            cur.execute(attempts_sql, (LoginWindow.uname,))
            attempts = cur.fetchone()
            return attempts
        
        def UpgradeScore(self, score):
            score = (score[0] + 1,)
            con = lite.connect("Database.db")
            cur = con.cursor()
            update_score_sql = "UPDATE clients SET score =? WHERE username=?"
            cur.execute(update_score_sql, (score[0], LoginWindow.uname))
            con.commit()
        
        def UpgradeAttempts(self, attempts):
            attempts = (attempts[0] + 1,)
            con = lite.connect("Database.db")
            cur = con.cursor()
            update_score_sql = "UPDATE clients SET attempts =? WHERE username=?"
            cur.execute(update_score_sql, (attempts[0], LoginWindow.uname))
            con.commit()
        

            
                
        def CheckAnswer(self,option):
            attempts= self.GetAttempts()
            self.UpgradeAttempts(attempts)
            if option == self.question[2]:
                self.DisplayedQuestions.append(self.question[1])
                self.DisplayQuestion()
                print("Yes")
                print(self.DisplayedQuestions)
#               print(self.GetScore())
                score = self.GetScore()
                self.UpgradeScore(score)
#                 print(score)
            else:
                print("No")
                self.DisplayQuestion()
                print(self.DisplayedQuestions)
                print(self.GetScore())
                
            
                
                
                
        
        
            

                    
class ReportClass(QtWidgets.QMainWindow, ReportScreen):
       #This will be the class to creat the GUI for the Report Window #
    # the parameter is the variable decleared as ReportScreen to load the Qtdesigner file for the Report Window#
        def __init__(self, parent=None): # initiating the class
            QtWidgets.QMainWindow.__init__(self, parent)
            self.setupUi(self)
            
             #title
            self.setWindowTitle('RevisionBuddy/Report')
            
               # Button
            
            self.HomeBut.clicked.connect(self.OpenHomeWindow)
            
            #Methords
            
        def OpenHomeWindow(self):
            ReportWindow.hide()
            HomeWindow.show()
            
            
        
            
            
        



class FilterClass(QtWidgets.QMainWindow, FilterScreen):
      #This will be the class to creat the GUI for the Filter Window #
    # the parameter is the variable decleared as FilterScreen to load the Qtdesigner file for the Filter Window#
        def __init__(self, parent=None): # initiating the class
            QtWidgets.QMainWindow.__init__(self, parent)
            self.setupUi(self)
            
            #title
            self.setWindowTitle('RevisionBuddy/Filter')
            
#             self.SelectedTopics=[]
            
            
        
            
               # Button
            
            self.HomeBut.clicked.connect(self.OpenHomeWindow)
            # Checkboxes
            
            
            self.TopicButton11.stateChanged.connect(self.FilterQuestions)
            self.TopicButton12.stateChanged.connect(self.FilterQuestions)
            self.TopicButton13.stateChanged.connect(self.FilterQuestions)
            self.TopicButton14.stateChanged.connect(self.FilterQuestions)
            self.TopicButton15.stateChanged.connect(self.FilterQuestions)
            self.TopicButton21.stateChanged.connect(self.FilterQuestions)
            self.TopicButton22.stateChanged.connect(self.FilterQuestions)
            self.TopicButton23.stateChanged.connect(self.FilterQuestions)
            self.AllTopicButton.stateChanged.connect(self.CheckAllTopics)             
            
            
            #Methords
            
        def OpenHomeWindow(self):
            
            FilterWindow.hide()
            HomeWindow.show()
            
      
        def UncheckAllTopicsButt(self):
            if not self.TopicButton11.isChecked() or not self.TopicButton12.isChecked() or not self.TopicButton13.isChecked() or not self.TopicButton14.isChecked() or not self.TopicButton15.isChecked() or not self.TopicButton21.isChecked() or not self.TopicButton22.isChecked() or not self.TopicButton23.isChecked():
                self.AllTopicButton.setChecked(False)

            
        def FilterQuestions(self):
            self.SelectedTopics=[]
            if self.TopicButton11.isChecked():
                self.SelectedTopics.append("1.1")
            if self.TopicButton12.isChecked():
                self.SelectedTopics.append("1.2")
            if self.TopicButton13.isChecked():
                self.SelectedTopics.append("1.3")
            if self.TopicButton14.isChecked():
                self.SelectedTopics.append("1.4")
            if self.TopicButton15.isChecked():
                self.SelectedTopics.append("1.5")
            if self.TopicButton21.isChecked():
                self.SelectedTopics.append("2.1")
            if self.TopicButton22.isChecked():
                self.SelectedTopics.append("2.2")
            if self.TopicButton23.isChecked():
                self.SelectedTopics.append("2.3")
            self.UncheckAllTopicsButt()
            QuizWindow.SelectedTopics = self.SelectedTopics
        
            
            
            
            # Get the selected topics
            
  
  
            
        
            
        def CheckAllTopics(self):
            if self.AllTopicButton.isChecked():
                self.TopicButton11.setChecked(True)
                self.TopicButton12.setChecked(True)
                self.TopicButton13.setChecked(True)
                self.TopicButton14.setChecked(True)
                self.TopicButton15.setChecked(True)
                self.TopicButton21.setChecked(True)
                self.TopicButton22.setChecked(True)
                self.TopicButton23.setChecked(True)
                self.AllTopicButton.setChecked(True)
                
        
            
      
#####################################################################
#   Starting the winndows
#####################################################################
       
app = QtWidgets.QApplication(sys.argv)
# Creating all the windows as objects of their corresponding Window Class#
MainWindow = MainClass(None)
LoginWindow = LoginClass(None)
InfoWindow = InfoClass(None)
RegisterWindow = RegisterClass(None)
HomeWindow = HomeClass(None)
QuizWindow = QuizClass(None)
ReportWindow = ReportClass(None)
FilterWindow = FilterClass(None)
# Displaying the all GUI window using the methord .show() # 
MainWindow.show()

 

app.exec_()