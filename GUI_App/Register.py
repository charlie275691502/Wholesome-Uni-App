import tkinter as tk
import sys
sys.path.insert(1, '../CLI_App')
from Validator import Validator

class Register:

  def __init__(self, studentDataLoader, window, onGoToLogin, onGoToEnrollment):
    self.studentDataLoader = studentDataLoader
    self.onGoToLogin = onGoToLogin
    self.onGoToEnrollment = onGoToEnrollment
    self.window = window

    self.email = tk.StringVar(window)
    self.password = tk.StringVar(window)
    self.name = tk.StringVar(window)
    self.errorMessage = tk.StringVar(window)

  def goToLogin(self):
    self.errorMessage.set("")
    self.onGoToLogin()

  def register(self):
    email = self.email.get()
    password = self.password.get()
    name = self.name.get()

    print(email, password, name)
    if Validator.Email(email) and Validator.Password(password):
      self.errorMessage.set("")
      self.studentDataLoader.add_student(email, password, name)
      self.goToLogin()
    elif self.studentDataLoader.is_email_exist(email) :
      self.errorMessage.set("Email has already been registered")
    else:
      self.errorMessage.set("Incorrect email or password format")

  def render(self):
    frame = tk.Frame(self.window, bg="white", padx=40, pady=10, bd=5, relief="groove")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    title = tk.Label(frame, text="Sign Up", bg="white", font=("Arial", 20))
    title.grid(row=0, column=0, pady=10, padx=2)

    emailLabel = tk.Label(frame, text = "Email", bg="white")
    emailLabel.grid(row = 1, column = 0, pady = 10, padx=2)

    emailEntry = tk.Entry(frame, textvariable=self.email)
    emailEntry.grid(row = 1, column = 1, pady = 10, padx=2)

    passwordLabel = tk.Label(frame, text = "Password", bg="white")
    passwordLabel.grid(row = 2, column = 0, pady = 10, padx=2)

    passwordEntry = tk.Entry(frame, textvariable=self.password)
    passwordEntry.grid(row = 2, column = 1, pady = 10, padx=2)

    nameLabel = tk.Label(frame, text = "Name", bg="white")
    nameLabel.grid(row = 3, column = 0, pady = 10, padx=2)

    nameEntry = tk.Entry(frame, textvariable=self.name)
    nameEntry.grid(row = 3, column = 1, pady = 10, padx=2)

    errorLabel = tk.Label(frame, textvariable=self.errorMessage, bg="white", fg="red")
    errorLabel.grid(row = 4, column = 0, columnspan=2, pady = 10, padx=2)

    registerButton = tk.Button(frame, text="Sign Up", bg="white", command=self.register)
    registerButton.grid(row = 5, column = 0, columnspan=2, pady = 10, padx=2)

    loginLabel = tk.Label(frame, text = "Already have an account? Login here", bg="white")
    loginLabel.grid(row = 6, column = 0, columnspan=2, padx=2)

    loginButton = tk.Button(frame, text="Login", bg="white", fg="black", command=self.goToLogin)
    loginButton.grid(row = 7, column = 0, columnspan=2, padx=2, pady = 5)

    return frame