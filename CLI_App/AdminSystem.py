import itertools
from ColorString import ColorString
from StudentDataLoader import StudentDataLoader
from StudentData import StudentData
from SubjectData import SubjectData

class AdminSystem:
    class AverageGrade :
        def __init__(self, student: StudentData) :
            self.student = student
            self.mark = sum([subject.mark for subject in student.subjects]) / len(student.subjects)
            self.grade = SubjectData.mark_to_grade(self.mark)
            self.is_fail = self.grade == 'F'
              
        def __str__(self) -> str:
            return f"{self.student.name} :: {self.student.student_id} --> GRADE: {self.grade} - MARK: {round(self.mark, 2)}"
    
    def __init__(self, student_data_loader: StudentDataLoader) -> None:
        self.student_data_loader = student_data_loader
        pass

    def admin_start(self):
        
        prompt = ColorString.BlueGreen("Admin System (c/g/p/r/s/x): ")
        command = input(prompt).lower()
        while(command != "x") :
            if command == "c" :
                self.admin_clear()
            elif command == "g" :
                self.admin_group()
            elif command == "p":
                self.admin_partition()
            elif command == "r":
                self.admin_remove()
            elif command == "s":
                self.admin_show()
            command = input(prompt).lower()
    
    def admin_clear(self):
        print(ColorString.Yellow("Clearing students database"))
        prompt = ColorString.Red("Are you sure you want to clear the database (Y)ES/(N)O:")
        command = input(prompt).lower()
        while(command != "n") :
            if command == "y" :           
                is_success = self.student_data_loader.remove_all_student()       #code for cleaning all student data
                if  is_success == True:
                    print(ColorString.Yellow("Student data cleared"))
                break
            command = input(prompt).lower()

    def admin_group(self):
        print(ColorString.Yellow("Grade Grouping"))
        
        students = self.student_data_loader.get_students()         #code for showing all student by Grade
        
        student_average_grades = [self.AverageGrade(student) for student in students]
        for grade, group in itertools.groupby(student_average_grades, lambda student_average_grade : student_average_grade.grade): 
            print(f"{grade} --> [{', '.join(str(item) for item in group)}]") 
        

    def admin_partition(self):
        print(ColorString.Yellow("PASS/FAIL Partition"))
        
        students = self.student_data_loader.get_students()         #code for showing all student by Grade
        student_average_grades = [self.AverageGrade(student) for student in students]
        
        fail_group = [student_average_grade for student_average_grade in student_average_grades if student_average_grade.is_fail]
        pass_group = [student_average_grade for student_average_grade in student_average_grades if not student_average_grade.is_fail]
        print(f"FAIL --> [{', '.join(str(item) for item in fail_group)}]")
        print(f"PASS --> [{', '.join(str(item) for item in pass_group)}]")

    def admin_remove(self):
        prompt = "Remove by ID: "
        student_id = input(prompt)
        student = self.student_data_loader.remove_student(student_id)
        if student == None :
            print(ColorString.Red(f"Student {(student_id)} does not exist"))
        else :
            print(ColorString.Yellow(f"Removing Student {(student_id)} Account"))      #code for remove ONE student data

    def admin_show(self):
        print(ColorString.Yellow("Student List"))
        students = self.student_data_loader.get_students()        #code for showing all student data
        if len(students) > 0 :
            for student in students :
                print(student)
        else :
            print("<Nothing to Display>")



