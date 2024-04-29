import json

class StudentData():
    def __init__(self, student_id, email, password, name) -> None:
        self.student_id = student_id
        self.name = name
        self.email = email
        self.password = password
        self.subjects = []
        
    def __str__(self):
        return f"{self.name} :: {self.student_id} --> Email: {self.email}"
        