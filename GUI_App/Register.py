import tkinter as tk

class Register:
  errorMessage = 'Wrong password'

  def __init__(self, window, onGoToLogin):
    self.onGoToLogin = onGoToLogin
    self.window = window

  def goToLogin(self):
    self.onGoToLogin()

  def render(self):
    frame = tk.Frame(self.window, bg="white", padx=40, pady=10, bd=5, relief="groove")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    greeting = tk.Label(frame, text="Sign Up", bg="white", font=("Arial", 20))
    greeting.grid(row=0, column=0, pady=10, padx=2)

    emailLabel = tk.Label(frame, text = "Email", bg="white")
    emailLabel.grid(row = 1, column = 0, pady = 10, padx=2)

    emailEntry = tk.Entry(frame)
    emailEntry.grid(row = 1, column = 1, pady = 10, padx=2)

    passwordLabel = tk.Label(frame, text = "Password", bg="white")
    passwordLabel.grid(row = 2, column = 0, pady = 10, padx=2)

    passwordEntry = tk.Entry(frame, show="*")
    passwordEntry.grid(row = 2, column = 1, pady = 10, padx=2)

    errorLabel = tk.Label(frame, text = self.errorMessage, bg="white", fg="red")
    errorLabel.grid(row = 3, column = 0, columnspan=2, pady = 10, padx=2)

    registerButton = tk.Button(frame, text="Sign Up", bg="white")
    registerButton.grid(row = 4, column = 0, columnspan=2, pady = 10, padx=2)

    loginLabel = tk.Label(frame, text = "Already have an account? Login here", bg="white")
    loginLabel.grid(row = 5, column = 0, columnspan=2, padx=2)

    loginButton = tk.Button(frame, text="Login", bg="white", fg="black", command=self.goToLogin)
    loginButton.grid(row = 6, column = 0, columnspan=2, padx=2, pady = 5)

    return frame