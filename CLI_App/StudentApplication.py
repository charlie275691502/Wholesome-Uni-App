from StudentData import StudentData
from StudentDataLoader import StudentDataLoader


class StudentApplication():
    def __init__(self, student_data: StudentData , student_data_loader: StudentDataLoader):
        self.student_data = student_data
        self.student_data_loader = student_data_loader
        
    def refresh_student_data(self):
        self.student_data = self.student_data_loader.get_student(self.student_data.student_id)
    
    def start(self):
        prompt = "Student Course Menu (c, e, r, s, x): "
        command = input(prompt).lower()
        while(command != "x") :
            if command == "c" :
                new_password = input("New Password: ")
                self.student_data_loader.student_change_password(
                    self.student_data.student_id,
                    new_password)
                
            elif command == "e" :
                subject = self.student_data_loader.student_enrol_subject(
                    self.student_data.student_id)
                self.refresh_student_data()
                
                if subject :
                    print(f"Enrolling in Subject-{subject.id}")
                print(f"You are now enrolling in {len(self.student_data.subjects)} out of 4 subjects.")

            elif command == "r" :
                subject_id = input("Id of the subject to remove: ")
                
                subject = self.student_data_loader.student_remove_subject(
                    self.student_data.student_id,
                    subject_id)
                self.refresh_student_data()
                
                if subject :
                    print(f"Droping Subject-{subject.id}")
                print(f"You are now enrolling in {len(self.student_data.subjects)} out of 4 subjects.")
                
            elif command == "s" :
                print(f"Showing {len(self.student_data.subjects)} subjects.")
                for subject in self.student_data.subjects :
                    print(subject)
                
            else :
                print("Command not found. Please try again.")
                
            command = input(prompt).lower()
            
        print("Leave Student Course System.")