import tkinter as tk
from Subjects import Subjects

class Enrollment:
  bg = "#edede9"

  def __init__(self, studentDataLoader, studentId, window, onGoToLogin):
    self.studentDataLoader = studentDataLoader
    self.window = window
    self.onGoToLogin = onGoToLogin
    self.studentId = studentId
    self.studentData = self.studentDataLoader.get_student(studentId)

    self.studentName = tk.StringVar(window)
    self.errorMessage = tk.StringVar(window)
    self.noOfSubjectsMessage = tk.StringVar(window)
    self.frame = None
    self.subjects = None
    self.subjectWindow = None

    self.studentName.set(f"Welcome, {self.studentData.name}")
    self.errorMessage.set("")

  def refreshStudentData(self):
    self.studentData = self.studentDataLoader.get_student(self.studentId)

  def goToLogin(self):
    self.onGoToLogin()

  def addSubject(self):
    if len(self.studentData.subjects) >= 4 :
      self.errorMessage.set("Enrol fail. Subject limit exceed.")
      return None
    else:
      self.errorMessage.set("")
      self.studentDataLoader.student_enrol_subject(self.studentId)
      self.refreshStudentData()
      self.showSubjectList()

  def updateSubjectList(self):
    subjects = Subjects(studentDataLoader=self.studentDataLoader, studentId=self.studentId, window=self.subjectWindow, onGoToLogin=self.goToLogin)
    self.subjects = subjects.render()

  def onClosedSubjectList(self):
    self.subjectWindow.destroy()
    self.subjectWindow = None
    self.subjects = None
  
  def showSubjectList(self):
    if not (self.subjectWindow):
      self.subjectWindow = tk.Tk()
      self.subjectWindow.geometry("300x400")
      self.subjectWindow.title("Subject List")
      self.subjectWindow.configure(bg="#edede9")
      self.subjectWindow.protocol("WM_DELETE_WINDOW", self.onClosedSubjectList)
    self.updateSubjectList()

  def render(self):
    frame = tk.Frame(self.window, bg=self.bg, padx=40, pady=10)
    frame.place(relx=0.5, rely=0.5, anchor="center")
    self.frame = frame

    logoutButton = tk.Button(frame, text="Logout", bg=self.bg, command=self.goToLogin)
    logoutButton.grid(row=0, column=2, pady=10, padx=2)

    title = tk.Label(frame, textvariable=self.studentName, font=("Arial", 20))
    title.grid(row=2, column=0, columnspan=2, pady=10, padx=2)

    errorLabel = tk.Label(frame, textvariable=self.errorMessage, fg="red")
    errorLabel.grid(row=4, column = 0, columnspan=2, pady = 10, padx=2)

    addSubjectButton = tk.Button(frame, text="Enroll in Subject", command=self.addSubject)
    addSubjectButton.grid(row = 5, column = 0, pady = 10, padx=2)

    goToSubjectListButton = tk.Button(frame, text="Show Subjects List", command=self.showSubjectList)
    goToSubjectListButton.grid(row = 5, column = 1, pady = 10, padx=2)

    self.refreshStudentData()

    return frame