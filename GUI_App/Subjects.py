import tkinter as tk

class Subjects:
  bg = "#edede9"

  def __init__(self, studentDataLoader, studentId, window, onGoToLogin):
    self.studentDataLoader = studentDataLoader
    self.window = window
    self.onGoToLogin = onGoToLogin
    self.studentId = studentId
    self.studentData = self.studentDataLoader.get_student(studentId)

    self.studentName = tk.StringVar(window)
    self.errorMessage = tk.StringVar(window)
    self.frame = None
    self.subjectFrame = None

    self.studentName.set(self.studentData.name)
    self.errorMessage.set("")

  def refreshStudentData(self):
    self.studentData = self.studentDataLoader.get_student(self.studentId)

    if (self.subjectFrame): self.subjectFrame.destroy()
    self.subjectFrame = tk.Frame(self.frame, bg="white")
    self.subjectFrame.grid(row=5, column=0, pady=10, padx=2)

    if (len(self.studentData.subjects) == 0):
      subjectLabel = tk.Label(self.subjectFrame, text="No subjects enrolled", bg=self.bg, bd=2, relief="groove")
      subjectLabel.grid(row=0, column=0, pady=10, padx=2)
    else:
      for idx, subject in enumerate(self.studentData.subjects) :
        subjectLabel = tk.Label(self.subjectFrame, text=f"Subject {subject.id} -- Mark: {subject.mark} -- Grade: {subject.grade} -- {'FAIL' if subject.is_fail else 'PASS'}", bg="white")
        subjectLabel.grid(row=idx, column=0, pady=10, padx=2)

        deleteSubjectButton = tk.Button(self.subjectFrame, text="Delete", bg="white", command=lambda: self.deleteSubject(subject.id))
        deleteSubjectButton.grid(row=idx, column=1, pady=10, padx=2)

  def deleteSubject(self, subjectId):
    print("DELETING SUBJECT", subjectId)
    self.errorMessage.set("")
    self.studentDataLoader.student_remove_subject(self.studentId, subjectId)
    self.studentDataLoader.save_to_pkl()
    self.refreshStudentData()

  def render(self):
    frame = tk.Frame(self.window, bg=self.bg, padx=40, pady=10)
    frame.place(relx=0.5, rely=0.5, anchor="center")
    self.frame = frame

    greeting = tk.Label(frame, textvariable=f"{self.studentName}'s Subjects")
    greeting.grid(row=1, column=0, padx=2)

    title = tk.Label(frame, text="Subject Enrollments", font=("Arial", 20))
    title.grid(row=2, column=0, pady=10, padx=2)

    errorLabel = tk.Label(frame, textvariable=self.errorMessage, fg="red")
    errorLabel.grid(row=3, column = 0, pady = 10, padx=2)

    self.refreshStudentData()

    return frame