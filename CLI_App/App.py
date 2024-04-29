from StudentApplication import StudentApplication
from StudentDataLoader import StudentDataLoader
from StudentAuthentication import StudentAunthentication


from ColorString import ColorString
from AdminSystem import AdminSystem

student_data_loader = StudentDataLoader()
student_application = StudentApplication(student_data_loader)
student_authentication_system = StudentAunthentication(student_data_loader, student_application)
admin_system = AdminSystem(student_data_loader)

prompt = ColorString.BlueGreen("University System: (A) dmin, (S) tudent, or X : ")
command = input(prompt).lower()
while(command != "x") :
    if command == "a" :
        admin_system.admin_start()
    elif command == "s" :
        student_authentication_system.start_system()
    else:
        print(ColorString.BlueGreen("Invalid user type."))
    command = input(prompt).lower()

print(ColorString.Yellow("Thank You"))