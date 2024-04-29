from StudentApplication import StudentApplication
from StudentDataLoader import StudentDataLoader
from Validator import Validator
from ColorString import ColorString

class StudentAunthentication(): 
    def __init__(self, student_data_loader: StudentDataLoader, studentApplication: StudentApplication):
        self.student_data_loader = student_data_loader
        self.studentApplication = studentApplication
        pass

    def start_system(self):
        while True:
            action = input(ColorString.BlueGreen("Student System (l/r/x): ")).lower()
            if action == 'x':
                break  # Exit the student system
            elif action == 'l':
                print(ColorString.Green("Student Sign In"))
                
                email = input("Email: ")
                password = input("Password: ")
                while not Validator.Email(email) or not Validator.Password(password):
                    print(ColorString.Red(f"Incorrect email or password format"))
                    email = input("Email: ")
                    password = input("Password: ")
                    
                print(ColorString.Yellow(f"email and password formats acceptable"))
                
                student = self.student_data_loader.try_login(email, password)
                if student == None :
                    print(ColorString.Red(f"Student does not exist"))
                else :
                    self.studentApplication.start(student.student_id)
                    
            elif action == 'r':
                print(ColorString.Green("Student Sign Up"))
                email = input("Email: ")
                password = input("Password: ")
                if Validator.Email(email) and Validator.Password(password):
                    print(ColorString.Yellow("email and password formats acceptable"))
                    
                    student_by_email = self.student_data_loader.get_student_by_email(email)
                    if student_by_email != None :
                        print(ColorString.Red(f"Student {1} already exists"))
                    else :
                        name = input("Name: ")
                        print(ColorString.Yellow(f"Enrolling Student {name}"))
                        self.student_data_loader.add_student(email, password, name)
                else:
                    print(ColorString.Red(f"Incorrect email or password format"))
            else:
                print(ColorString.BlueGreen("Invalid action"))