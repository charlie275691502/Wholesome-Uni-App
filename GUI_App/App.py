from Login import Login
from Register import Register
from Enrollment import Enrollment
import tkinter as tk

class App:
  def __init__(self):
    self.window = tk.Tk()
    self.window.geometry("600x600")
    self.window.title("Sign Up")
    self.window.configure(bg="white")
    self.frame = None
  
    self.login = Login(window=self.window, onGoToRegister=self.goToRegister, onGoToEnrollment=self.goToEnrollment)
    self.register = Register(window=self.window, onGoToLogin=self.goToLogin)
    self.enrollment = Enrollment(window=self.window, onGoToLogin=self.goToLogin, onGoToSubjects=self.goToSubjects)

  def start(self):
    self.goToLogin()
    self.window.mainloop()
  
  def goToLogin(self):
    if (self.frame): 
      self.frame.destroy()
    self.frame = self.login.render()

  def goToRegister(self):
    if (self.frame): 
      self.frame.destroy()
    self.frame = self.register.render()

  def goToEnrollment(self):
    if (self.frame): 
      self.frame.destroy()
    self.frame = self.enrollment.render()

App().start()