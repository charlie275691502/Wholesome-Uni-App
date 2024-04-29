from Login import Login
from Register import Register
from Enrollment import Enrollment
import tkinter as tk
import sys

sys.path.insert(1, '../Common')
from StudentDataLoader import StudentDataLoader

class App:
  def __init__(self):
    self.studentDataLoader = StudentDataLoader()

    self.window = tk.Tk()
    self.window.geometry("600x600")
    self.window.title("Login")
    self.window.configure(bg="#edede9")
    self.frame = None
  
  def goToLogin(self):
    if (self.frame): 
      self.frame.destroy()
    login = Login(studentDataLoader=self.studentDataLoader, window=self.window, onGoToRegister=self.goToRegister, onGoToEnrollment=self.goToEnrollment)
    self.window.title("Login")
    self.frame = login.render()

  def goToRegister(self):
    if (self.frame): 
      self.frame.destroy()
    register = Register(studentDataLoader=self.studentDataLoader, window=self.window, onGoToLogin=self.goToLogin, onGoToEnrollment=self.goToEnrollment)
    self.window.title("Register")
    self.frame = register.render()

  def goToEnrollment(self, studentId="199711"):
    if (self.frame): 
      self.frame.destroy()
    enrollment = Enrollment(window=self.window, studentDataLoader=self.studentDataLoader, studentId=studentId, onGoToLogin=self.goToLogin)
    self.window.title("Enrollment")
    self.frame = enrollment.render()

  def start(self):
    self.goToLogin()
    self.window.mainloop()

App().start()