import os
import tkinter as tk
import sys

sys.path.insert(1, os.sep.join(os.path.realpath(__file__).split(os.sep)[0:-2]) + os.sep + "Common")

from Validator import Validator

class Register:
  bg = "#edede9"

  def __init__(self, studentDataLoader, window, onGoToLogin, onGoToEnrollment):
    self.studentDataLoader = studentDataLoader
    self.onGoToLogin = onGoToLogin
    self.onGoToEnrollment = onGoToEnrollment
    self.window = window

    self.email = tk.StringVar(window)
    self.password = tk.StringVar(window)
    self.name = tk.StringVar(window)
    self.errorMessage = tk.StringVar(window)

    self.email.set("")
    self.password.set("")
    self.name.set("")
    self.errorMessage.set("")

  def goToLogin(self):
    self.errorMessage.set("")
    self.onGoToLogin()

  def register(self):
    email = self.email.get()
    password = self.password.get()
    name = self.name.get()

    print(email, password, name)
    if name == '':
       self.errorMessage.set("Name cannot be empty")
    elif Validator.Email(email) and Validator.Password(password):
      self.errorMessage.set("")
      student_by_email = self.studentDataLoader.get_student_by_email(email)
      if student_by_email != None :
        self.errorMessage.set(f"Student {student_by_email.name} already exists")
      else:
        self.studentDataLoader.add_student(email, password, name)
        self.goToLogin()
    else:
      self.errorMessage.set("Incorrect email or password format")

  def render(self):
    frame = tk.Frame(self.window, bg=self.bg, padx=40, pady=10, bd=5, relief="groove")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    title = tk.Label(frame, text="Sign Up", bg=self.bg, font=("Arial", 20))
    title.grid(row=0, column=0, pady=10, padx=2)

    emailLabel = tk.Label(frame, text = "Email", bg=self.bg)
    emailLabel.grid(row = 1, column = 0, pady = 10, padx=2)

    emailEntry = tk.Entry(frame, textvariable=self.email, width=30)
    emailEntry.grid(row = 1, column = 1, pady = 10, padx=2)

    passwordLabel = tk.Label(frame, text = "Password", bg=self.bg)
    passwordLabel.grid(row = 2, column = 0, pady = 10, padx=2)

    passwordEntry = tk.Entry(frame, textvariable=self.password, width=30)
    passwordEntry.grid(row = 2, column = 1, pady = 10, padx=2)

    nameLabel = tk.Label(frame, text = "Name", bg=self.bg)
    nameLabel.grid(row = 3, column = 0, pady = 10, padx=2)

    nameEntry = tk.Entry(frame, textvariable=self.name, width=30)
    nameEntry.grid(row = 3, column = 1, pady = 10, padx=2)

    errorLabel = tk.Label(frame, textvariable=self.errorMessage, bg=self.bg, fg="red")
    errorLabel.grid(row = 4, column = 0, columnspan=2, pady = 10, padx=2)

    registerButton = tk.Button(frame, text="Sign Up", bg=self.bg, command=self.register)
    registerButton.grid(row = 5, column = 0, columnspan=2, pady = 10, padx=2)

    loginLabel = tk.Label(frame, text = "Already have an account? Login here", bg=self.bg)
    loginLabel.grid(row = 6, column = 0, columnspan=2, padx=2)

    loginButton = tk.Button(frame, text="Login with existing account", bg=self.bg, fg="black", command=self.goToLogin)
    loginButton.grid(row = 7, column = 0, columnspan=2, padx=2, pady = 5)

    return frame