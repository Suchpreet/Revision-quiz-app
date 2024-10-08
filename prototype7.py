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
import matplotlib.pyplot as plt
import time


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
            
            self.AdminLoginBut.clicked.connect(self.AdminLoginNow)
            
            self.ShowPasswordBut.setCheckable(True)
            
            self.ShowPasswordBut.clicked.connect(self.ShowPassword)
            
            self.PasswordEntry1.returnPressed.connect(self.LoginNow)
            
#             attributes
            self.username = 0
            
            
            
   
                    
            
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
            usersDatasql = "select username, password from users"
            cur.execute(usersDatasql)              
            ExistingUsers = cur.fetchall()

#           print(ExistingUsers)
            username = (self.UsernameEntry1.text()).lower()
            password = self.PasswordEntry1.text()
            self.username = username

        
            
            loginToCheck = (username,password)
            print(username)


            succesful = False

            for dataPair in ExistingUsers:
                if dataPair == loginToCheck:
                    succesful = True
                    
                    
                

            if succesful == True:
                HomeWindow.show()
                LoginWindow.hide()
                FilterWindow.AllTopicButton.setChecked(True)
# When the home window open the AllTopicButton and the CheckAllTopics method is called                  
                FilterWindow.CheckAllTopics()
                
                self.UsernameEntry1.setText("") # Clears the username entry box
                self.PasswordEntry1.setText("") # Clears the password entry box
                
                


            else:
                QMessageBox.warning(self, 'Error', 'Wrong Username or password .')
                return
            
        def AdminLoginNow(self):
            username = self.UsernameEntry1.text()
            password = self.PasswordEntry1.text()
            loginToCheck = (username,password)
            
            DataPair=('admin','sach')

            succesful = False
            
            if DataPair == loginToCheck:
                    succesful = True
            if succesful == True:
                AdminWindow.show()
                LoginWindow.hide()
                self.UsernameEntry1.setText("") # Clears the username entry box
                self.PasswordEntry1.setText("") # Clears the password entry box

            else:
                QMessageBox.warning(self, 'Error', 'Wrong Login details and This is for admin')
                return
            
            
                
                
            
               
class AdminClass(QtWidgets.QMainWindow, AdminScreen):
      #This will be the class to creat the GUI for the Login Window #
    # the parameter is the variable decleared as LoginScreen to load the Qtdesigner file for the Login Window# 
        def __init__(self, parent=None): # initiating the class
            QtWidgets.QMainWindow.__init__(self, parent)
            self.setupUi(self)
            
            #title
            self.setWindowTitle('RevisionBuddy/Admin')
            
                 #Button
            self.GoBackBut.clicked.connect(self.OpenMainWindow)
#   GoBackBut button called OpenMainWindow method when clicked            
            self.SubmitButton.clicked.connect(self.Submit)

#   SubmitButton button called Submit method when clicked           
            
            
            # Methords
            
        def OpenMainWindow(self):
            AdminWindow.hide()
            MainWindow.show()
            
#             method to create QuestionId
        def GetQuestionId(self):
            con = lite.connect("Database.db")
            cur = con.cursor()
            questionsDatasql = "select question_id from questions"
            cur.execute(questionsDatasql)              
            MyQuestions = cur.fetchall()
            QuestionId = int(len(MyQuestions)+1)

#            print(QuestionId)
            return QuestionId
        
        def Submit(self):
            #it gets question the database table
            QuestionId =self.GetQuestionId()
            #print(self.GetQuestionId())
            Question = self.QuestionEntry.text()
            Answer = self.AnswerEntry.text()
            Option2 = self.Option1Entry.text()
            Option3 = self.Option2Entry.text()
            Option4 = self.Option3Entry.text()
                        
            Topic = self.comboBoxTopics.currentText() 
            
            if not Question or not Answer or not Option2 or not Option3 or not Option4 or not Topic:
        # If any entry boxes are left empty , show error message
                QMessageBox.warning(self, 'Error', 'Cannot leave any thing empty.')
                return
            
            # Check if question already exists in the database
            con = lite.connect("Database.db")
            cur = con.cursor()
            existing_question_sql = "SELECT * FROM questions WHERE question=?"
            cur.execute(existing_question_sql, (Question,))
            if cur.fetchone():
        # If question already exists, show error message
                QMessageBox.warning(self, 'Error', 'Question already exists.')
                return
            
            con = lite.connect("Database.db")
            curInsert = con.cursor()
            sqlInsert = "INSERT INTO questions VALUES(?,?,?,?,?,?,?)"
            curInsert.execute(sqlInsert, (QuestionId,Question,Answer,Option2,Option3,Option4,Topic))
            con.commit()
            QMessageBox.information(self, 'Done', 'This question has been added to the database .')
            # Clears the entry boxes
            self.QuestionEntry.setText("")
            self.AnswerEntry.setText("")
            self.Option1Entry.setText("")
            self.Option2Entry.setText("")
            self.Option3Entry.setText("")
          
            
                
            
            
                    
            
            
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
            self.ShowPasswordBut.setCheckable(True)

            self.ShowPasswordBut.clicked.connect(self.ShowPassword)
            
            
            # Methords
#
# takes a parameter which is the state of the button ,when state is true the password
# can be seen by changing to normal mode and when the state is false the password is hidden.
        def ShowPassword(self, state):
            if state:
                self.PasswordEntry.setEchoMode(QLineEdit.Normal)
            else:
                self.PasswordEntry.setEchoMode(QLineEdit.Password)
            
        def OpenMainWindow(self):
            RegisterWindow.hide()
            MainWindow.show()
            
        def ShowPassword(self, state):
            if state:
                self.PasswordEntry.setEchoMode(QLineEdit.Normal)
            else:
                self.PasswordEntry.setEchoMode(QLineEdit.Password)
            
        def RegisterMe(self):           
            con = lite.connect("Database.db")
            cur = con.cursor()
            usersDatasql = "select user_id from users"
            cur.execute(usersDatasql)              
            ExistingUsers = cur.fetchall()

            NewUserId = int(len(ExistingUsers)+1)
#             print(ClientId)

            username = (self.UsernameEntry.text()).lower()
            password = self.PasswordEntry.text()
            cpassword = self.ConfirmPasswordEntry.text()
            #self.username = username
            print(username)
            
            
            if password != cpassword :
        # If username or password is empty, show error message
                QMessageBox.warning(self, 'Error', 'passwords are not same .')
                return
           
    
            if not username or not password:
        # If username or password is empty, show error message
                QMessageBox.warning(self, 'Error', 'Username or password cannot be empty.')
                return
            
            if "'" in username or "'" in password:
        # If username or password contain single quotes, show error message
                QMessageBox.warning(self, 'Error', "Username or password can't contain single quotes.")
                return
    
            if len(password) < 8:
        # If password length is less than 8 characters, show error message
                QMessageBox.warning(self, 'Error', 'Password must be at least 8 characters long for security.')
                return
    
    # Check if username already exists in the database
            existing_username_sql = "SELECT * FROM users WHERE username=?"
            cur.execute(existing_username_sql, (username,))
            if cur.fetchone():
        # If username already exists, show error message
                QMessageBox.warning(self, 'Error', 'Username already exists.')
                return
    
    # If all checks passed, insert the data into the database
            
            con = lite.connect("Database.db")
            cur = con.cursor()
            new_user_sql = "INSERT INTO users VALUES(?,?,?,?,?,?)"
            cur.execute(new_user_sql, (NewUserId,username, password,('0'),('0'),('0')))
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
            QuizWindow.StartingTime =time.time()
            
            
            
            
        
        def OpenReportWindow(self):
            HomeWindow.hide()
            ReportWindow.show()
            ReportWindow.GetData()
            ReportWindow.GetTime()
            
            
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
#             attributes

            self.DisplayedQuestions = []
            self.SelectedTopics = []
            self.StartingTime = 0
            
            self.hideEvent = self.windowHidden
            
               # Button
            
            self.HomeBut.clicked.connect(self.OpenHomeWindow)
            self.OptionBut1.clicked.connect(lambda: self.CheckAnswer(self.OptionBut1.text()))
            self.OptionBut2.clicked.connect(lambda: self.CheckAnswer(self.OptionBut2.text()))
            self.OptionBut3.clicked.connect(lambda: self.CheckAnswer(self.OptionBut3.text()))
            self.OptionBut4.clicked.connect(lambda: self.CheckAnswer(self.OptionBut4.text()))
            self.IDKBut.clicked.connect(self.DisplayQuestion)
            self.NextQuestionBut.hide()
            
            self.NextQuestionBut.clicked.connect(self.DisplayQuestion)
            
        def CheckAnswer(self,option):
            self.NextQuestionBut.show()
            attempts= self.GetAttempts()
            self.UpgradeAttempts(attempts)
            
            self.IDKBut.hide()
            
            if option == self.question[2]:
                self.DisplayedQuestions.append(self.question[1])
                #self.DisplayQuestion()
                self.ResultLabel.setText("Yes,that's correct")
                score = self.GetScore()
                self.UpgradeScore(score)
                print(self.DisplayedQuestions)
                print(score)
            else:
                self.ResultLabel.setText('The correct answer is ,'+ str(self.question[2]))
                print(self.DisplayedQuestions)
                print(score)

            
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
#             print(self.SelectedTopics)
            self.NextQuestionBut.hide()
            self.IDKBut.show()
            
            self.ResultLabel.setText("  ")
            
            if questions:
                self.question = random.choice(questions)
                while self.question[1] in self.DisplayedQuestions or self.question[6] not in self.SelectedTopics:
                    self.question = random.choice(questions)
                self.QuestionBrowser.setText(self.question[6] +')  '+ self.question[1])
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
            score_sql = "SELECT score FROM users WHERE username=?"
            cur.execute(score_sql, (LoginWindow.username,))
            score = cur.fetchone()
            return score
            
        def GetAttempts(self): 
    # Retrieve the current score from the database
            con = lite.connect("Database.db")
            cur = con.cursor()
            attempts_sql = "SELECT attempts FROM users WHERE username=?"
            cur.execute(attempts_sql, (LoginWindow.username,))
            attempts = cur.fetchone()
            return attempts
        
        def UpgradeScore(self, score):
            score = (score[0] + 1,)
            con = lite.connect("Database.db")
            cur = con.cursor()
            update_score_sql = "UPDATE users SET score =? WHERE username=?"
            cur.execute(update_score_sql, (score[0], LoginWindow.username))
            con.commit()
        
        def UpgradeAttempts(self, attempts):
            attempts = (attempts[0] + 1,)
            con = lite.connect("Database.db")
            cur = con.cursor()
            update_score_sql = "UPDATE users SET attempts =? WHERE username=?"
            cur.execute(update_score_sql, (attempts[0], LoginWindow.username))
            con.commit()
        
        
          
          
        def windowHidden(self, event):
            EndTime = time.time()
            TimeSpent = round(EndTime - self.StartingTime)
            print("Time spent in QuizWindow:", round(TimeSpent), "seconds")

            con = lite.connect("Database.db")
            cur = con.cursor()
            TimeSql = "SELECT time FROM users WHERE username=?"
            cur.execute(TimeSql, (LoginWindow.username,))
            CurrentTime = cur.fetchone()[0]
            print(CurrentTime)
            updateTimeSql = "UPDATE users SET time =? WHERE username=?"
            UpdatedTime = (CurrentTime + TimeSpent)
            print(UpdatedTime)
            cur.execute(updateTimeSql, (UpdatedTime, LoginWindow.username))
            con.commit()
            
    

            
                
        def CheckAnswer(self,option):
            self.NextQuestionBut.show()
            attempts= self.GetAttempts()
            self.UpgradeAttempts(attempts)
            
            self.IDKBut.hide()
            
            if option == self.question[2]:
                self.DisplayedQuestions.append(self.question[1])
                self.ResultLabel.setText("Yes,that's correct")
#               print(self.DisplayedQuestions) 
#               print(self.GetScore())
                score = self.GetScore()
                self.UpgradeScore(score)
#                 print(score)
            else:
                self.ResultLabel.setText('The correct answer is ,'+ str(self.question[2]))
                #self.DisplayQuestion()
#                 print(self.DisplayedQuestions)
#                 print(self.GetScore())
                
            
                
                
                
        
        
            

                    
class ReportClass(QtWidgets.QMainWindow, ReportScreen):
       #This will be the class to creat the GUI for the Report Window #
    # the parameter is the variable decleared as ReportScreen to load the Qtdesigner file for the Report Window#
        def __init__(self, parent=None): # initiating the class
            QtWidgets.QMainWindow.__init__(self, parent)
            self.setupUi(self)
            
             #title
            self.setWindowTitle('RevisionBuddy/Report')
            # Attributes
            
            self.AnsweredCorrect=0
            self.AnsweredIncorrect=0
            
               # Button
            
            self.HomeBut.clicked.connect(self.OpenHomeWindow)
             # HomeBut is a push button that executes 'OpenBlog' method  when it is clicked.
            
            self.GraphBut.clicked.connect(lambda: self.MakeGraph(self.AnsweredCorrect,self.AnsweredIncorrect))
             # GraphBut is a push button that executes 'MakeGraph' method  when it is clicked.
            
            #Methords
            
        def GetData(self):
#   Methord to get the user data on how many questions answered correct and incorrect 
# attempts and score are fetched from the user table
# Connect to the database
            con = lite.connect("Database.db")
            cur = con.cursor()

            # Retrieve the score and attempts for a specific user
            score_sql = "SELECT score FROM users WHERE username=?"
            attempts_sql = "SELECT attempts FROM users WHERE username=?"
            cur.execute(score_sql, (LoginWindow.username,))
            score = cur.fetchone()[0]
            
            cur.execute(attempts_sql, (LoginWindow.username,))
            attempts = cur.fetchone()[0]
            
            self.AnsweredCorrect = score
            self.AnsweredIncorrect = int(attempts-score)
            self.ScoreBrowser.setText('You correctly answered ' + str(score) + " questions\n" + 'You incorrectly answered ' +
                                      str(attempts-score) + ' questions\n'+'You attempted ' + str(attempts) + ' questions')
            
        def MakeGraph(self,score,notscore):

        # Make a pie chart of score (Questions answered correct ) and attempts-score(Questions answered incorrect )
            labels = ['Questions Answered correct', 'Questions Answered\n incorrect']
            sizes = [score, notscore]
            fig1, ax1 = plt.subplots()
            ax1.pie(sizes, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)
            ax1.axis('equal')
            plt.show()
            
        def GetTime(self):
            
            con = lite.connect("Database.db")
            cur = con.cursor()
            TimeSql = "SELECT time FROM users WHERE username=?"
            cur.execute(TimeSql, (LoginWindow.username,))
            CurrentTime = cur.fetchone()[0]
            print(CurrentTime)
            Minutes = CurrentTime // 60
            Seconds = CurrentTime % 60
            self.TimeLabel.setText('You have spent '+ str(Minutes)+' minutes and\n'+ str(Seconds)+' seconds in total')
            
            

            
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
            

            
            
        
            
               # Button
            
            self.HomeBut.clicked.connect(self.OpenHomeWindow)
            
            # Checkboxes
            
#             if any checkbox is clicked on , the FilterQuestions method is called

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
            
         #    This method verifies which checkbox are checekd and corresponding Topic is added to            
        def FilterQuestions(self):
            self.SelectedTopics=[]
#       SelectedTopics is empty at the start      
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
            
#       this metod goes through te state of all the check box and if anyoone is unchecekd
# the AllTopicButton is unchecked  
        def UncheckAllTopicsButt(self):
            if not self.TopicButton11.isChecked() or not self.TopicButton12.isChecked() or not self.TopicButton13.isChecked() or not self.TopicButton14.isChecked() or not self.TopicButton15.isChecked() or not self.TopicButton21.isChecked()or not self.TopicButton22.isChecked() or not self.TopicButton23.isChecked():
                self.AllTopicButton.setChecked(False)
           
            
            
                
#          print(QuizWindow.SelectedTopics)
 
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
                
        def OpenHomeWindow(self):
            print(len(self.SelectedTopics))
            if len(self.SelectedTopics) == 0:
                QMessageBox.warning(self, 'Error', 'Please select a topic.')
            else:
                FilterWindow.hide()
                HomeWindow.show()
                
        
            
      
#####################################################################
#   Starting the winndows
#####################################################################
       
app = QtWidgets.QApplication(sys.argv)
# Creating all the windows as objects of their corresponding Window Class#
MainWindow = MainClass(None)
LoginWindow = LoginClass(None)
AdminWindow = AdminClass(None)
InfoWindow = InfoClass(None)
RegisterWindow = RegisterClass(None)
HomeWindow = HomeClass(None)
QuizWindow = QuizClass(None)
ReportWindow = ReportClass(None)
FilterWindow = FilterClass(None)
# Displaying the all GUI window using the methord .show() # 
MainWindow.show()
#AdminWindow.show()



app.exec_()