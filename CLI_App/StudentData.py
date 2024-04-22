class SubjectData():
    def __init__(self) -> None:
        self.id = ""
        self.mark = 0
        self.grade = ""
        self.is_fail = True

class StudentData():
    def __init__(self) -> None:
        self.student_id = ""
        self.name = ""
        self.email = ""
        self.password = ""
        self.subjects = []
        