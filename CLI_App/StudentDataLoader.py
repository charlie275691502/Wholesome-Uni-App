import os, pickle
import random

from StudentData import StudentData
from SubjectData import SubjectData
from Validator import Validator

class StudentDataLoader:
    data_path = "students.data"
    
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
    
    def random_generate_unique_student_id(self) -> str:
        student_id = "{:06d}".format(random.randint(1, 999999))
        while student_id in self.students :
            student_id = "{:06d}".format(random.randint(1, 999999))
        return student_id
    
    def get_student(self, student_id) -> StudentData:
        if student_id in self.students :
            return self.students[student_id]
        
        print(f"Get Student Fail. Student id not found: [{student_id}]")
        return None
    
    def get_students(self) -> list[StudentData]:
        return list(self.students.values())
    
    def add_student(self, email, password, name) -> StudentData:
        student_id = self.random_generate_unique_student_id()
        
        student = StudentData(student_id, email, password, name)
        self.students[student_id] = student
        self.save_to_pkl()
        return student
        
    def remove_student(self, student_id: str) -> StudentData:
        if student_id in self.students :
            student = self.students[student_id]
            del self.students[student_id]
            self.save_to_pkl()
            return student
        
        print(f"Remove Student Fail. Student id not found: [{student_id}]")
        return None
    
    def remove_all_student(self) -> bool:
        self.students = {}
        self.save_to_pkl()
        return True
    
    def student_enrol_subject(self, student_id: StudentData) -> SubjectData:
        student = self.get_student(student_id)
        if student == None :
            return None
        
        if len(student.subjects) >= 4 :
            print(f"Enrol fail. Subject limit exceed.")
            return None
        
        subject = SubjectData()
        student.subjects.append(subject)
        self.save_to_pkl()
        return subject
    
    def student_remove_subject(self, student_id: StudentData, subject_id: str) -> SubjectData:
        student = self.get_student(student_id)
        if student == None :
            return False
        
        subject = next((subject for subject in student.subjects if subject.id == subject_id), None)
        if subject == None :
            print(f"Remove subject fail. Subject id not found: {subject_id}")
            return False
        
        student.subjects.remove(subject)
        self.save_to_pkl()
        return subject
    
    def student_change_password(self, student_id: StudentData, new_password: str) -> bool:
        student = self.get_student(student_id)
        if student == None :
            return False
        
        if not Validator.Password(new_password):
            print(f"Change password fail. Password is not valid.")
            return False
        
        student.password = new_password
        self.save_to_pkl()
        return True
        