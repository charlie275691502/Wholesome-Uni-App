from ColorString import ColorString
from StudentDataLoader import StudentDataLoader

class AdminSystem:
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
        print("Selected Admin group student")           
        students = self.student_data_loader.get_students()         #code for showing all student by Grade
        sorted(students, key=lambda student : student.subjects)

        # check the criteria next class

    def admin_partition(self):
        print(ColorString.Yellow("PASS/FAIL Partition"))
        print("Selected Admin partition student")       #code for listing PASS+FAIL student all student data
        # avg. marks for all the subject of ONE student?

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



