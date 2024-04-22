import json

class SubjectData():
    def __init__(self) -> None:
        self.id = ""
        self.mark = 0
        self.grade = ""
        self.is_fail = True
        
    def __str__(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__, 
            indent=2)

class StudentData():
    def __init__(self) -> None:
        self.student_id = ""
        self.name = ""
        self.email = ""
        self.password = ""
        self.subjects = []
        
    def __str__(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__, 
            indent=2)
        