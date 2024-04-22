import os, pickle

from CLI_App.Datas import StudentData, SubjectData

class StudentDataLoader:
    data_path = "students.pkl"
    
    def __init__(self) -> None:
        self.students = self.load_from_pkl()
        pass
    
    def save_to_pkl(self) -> None :
        with open(self.data_path, 'wb') as fp:
            pickle.dump(self.students, fp)
            
    def load_from_pkl(self) -> dict[StudentData]:
        if not os.path.isfile(self.data_path) :
            return {}
        with open(self.data_path, 'rb') as fp:
            return pickle.load(fp)
    
    def get_student(self, student_id) -> StudentData:
        if student_id in self.students :
            return self.students[student_id]
        
        print(f"Get Student Fail. Student id not found: [{student_id}]")
        return None
    
    def get_students(self) -> list[StudentData]:
        return list(self.students.values())
    
    def add_student(self, student: StudentData) -> bool:
        if student.student_id in self.students :
            print(f"Register New Student Fail. Student Id already in the database: [{student.student_id}]")
            return False
        
        self.students[student.student_id] = student
        self.save_to_pkl()
        return True
        
    def remove_student(self, student_id: str) -> bool:
        if student_id in self.students :
            del self.students[student_id]
            self.save_to_pkl()
            return True
        
        print(f"Remove Student Fail. Student id not found: [{student_id}]")
        return False
    
    def remove_all_student(self) -> bool:
        self.students = {}
        self.save_to_pkl()
        return True
    
    def student_enrol_subject(self, student_id: StudentData) -> bool:
        student = self.get_student(student_id)
        if student == None :
            return False
        
        if (student.subjects) >= 4 :
            print(f"Enrol fail. Subject limit exceed.")
            return False
        
        student.subjects.append(SubjectData())
        self.save_to_pkl()
        return True
    
    def student_remove_subject(self, student_id: StudentData) -> bool:
        student = self.get_student(student_id)
        if student == None :
            return False
        
        if (student.subjects) == 0 :
            print(f"Remove Subject fail. No subject left.")
            return False
        
        student.subjects.pop()
        self.save_to_pkl()
        return True