import tkinter as tk
import sys

sys.path.insert(1, '../CLI_App')
from StudentDataLoader import StudentDataLoader

class Login:
  errorMessage = 'Wrong password'

  def __init__(self, window, onGoToRegister, onGoToEnrollment):
    self.studentDataLoader = StudentDataLoader()
    self.onGoToRegister = onGoToRegister
    self.onGoToEnrollment = onGoToEnrollment
    self.window = window

    self.email = tk.StringVar(window)
    self.password = tk.StringVar(window)

  def goToRegister(self):
    self.onGoToRegister()
  
  def login(self):
    student = self.studentDataLoader.try_login(self.email.get(), self.password.get())
    print(student, self.email.get(), self.password.get())
    if student:
      self.onGoToEnrollment()
    else:
      self.errorMessage = 'Incorrect email or password format'

  def render(self):
    frame = tk.Frame(self.window, bg="white", padx=40, pady=10, bd=5, relief="groove")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    greeting = tk.Label(frame, text="Sign In", bg="white", font=("Arial", 20))
    greeting.grid(row=0, column=0, pady=10, padx=2)

    emailLabel = tk.Label(frame, text = "Email", bg="white")
    emailLabel.grid(row = 1, column = 0, pady = 10, padx=2)

    emailEntry = tk.Entry(frame, textvariable=self.email)
    emailEntry.grid(row = 1, column = 1, pady = 10, padx=2)

    passwordLabel = tk.Label(frame, text = "Password", bg="white")
    passwordLabel.grid(row = 2, column = 0, pady = 10, padx=2)

    passwordEntry = tk.Entry(frame, textvariable=self.password, show="*")
    passwordEntry.grid(row = 2, column = 1, pady = 10, padx=2)

    errorLabel = tk.Label(frame, text = self.errorMessage, bg="white", fg="red")
    errorLabel.grid(row = 3, column = 0, columnspan=2, pady = 10, padx=2)

    loginButton = tk.Button(frame, text="Sign In", bg="white", command=self.login)
    loginButton.grid(row = 4, column = 0, columnspan=2, pady = 10, padx=2)

    signUpLabel = tk.Label(frame, text = "New Student? Sign up here for new account", bg="white")
    signUpLabel.grid(row = 5, column = 0, columnspan=2, padx=2)

    signUpButton = tk.Button(frame, text="Sign Up for new account", bg="white", fg="black", command=self.goToRegister)
    signUpButton.grid(row = 6, column = 0, columnspan=2, padx=2, pady = 5)

    return frame