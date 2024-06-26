import tkinter as tk

class Login:
  bg = "#edede9"

  def __init__(self, studentDataLoader, window, onGoToRegister, onGoToEnrollment):
    self.studentDataLoader = studentDataLoader
    self.onGoToRegister = onGoToRegister
    self.onGoToEnrollment = onGoToEnrollment
    self.window = window

    self.email = tk.StringVar(window)
    self.password = tk.StringVar(window)
    self.errorMessage = tk.StringVar(window)

    self.email.set("")
    self.password.set("")
    self.errorMessage.set("")

  def goToRegister(self):
    self.errorMessage.set("")
    self.onGoToRegister()
  
  def login(self):
    student = self.studentDataLoader.try_login(self.email.get(), self.password.get())
    print(student, self.email.get(), self.password.get())
    if student:
      self.errorMessage.set("")
      self.onGoToEnrollment(student.student_id)
    else:
      self.errorMessage.set('Incorrect email or password format')

  def render(self):
    frame = tk.Frame(self.window, bg=self.bg, padx=40, pady=10, bd=5, relief="groove")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    title = tk.Label(frame, text="Sign In", bg=self.bg, font=("Arial", 20))
    title.grid(row=0, column=0, pady=10, padx=2)

    emailLabel = tk.Label(frame, text = "Email", bg=self.bg)
    emailLabel.grid(row = 1, column = 0, pady = 10, padx=2)

    emailEntry = tk.Entry(frame, textvariable=self.email, width=30)
    emailEntry.grid(row = 1, column = 1, pady = 10, padx=2)

    passwordLabel = tk.Label(frame, text = "Password", bg=self.bg)
    passwordLabel.grid(row = 2, column = 0, pady = 10, padx=2)

    passwordEntry = tk.Entry(frame, textvariable=self.password, show="*", width=30)
    passwordEntry.grid(row = 2, column = 1, pady = 10, padx=2)

    errorLabel = tk.Label(frame, textvariable=self.errorMessage, bg=self.bg, fg="red")
    errorLabel.grid(row = 3, column = 0, columnspan=2, padx=2)

    loginButton = tk.Button(frame, text="Sign In", bg=self.bg, command=self.login)
    loginButton.grid(row = 4, column = 0, columnspan=2, pady = 20, padx=2)

    signUpLabel = tk.Label(frame, text = "New Student? Sign up here for new account", bg=self.bg)
    signUpLabel.grid(row = 5, column = 0, columnspan=2, padx=2)

    signUpButton = tk.Button(frame, text="Sign Up for new account", bg=self.bg, fg="black", command=self.goToRegister)
    signUpButton.grid(row = 6, column = 0, columnspan=2, padx=2, pady = 5)

    return frame