import re

from CLI_App.ColorString import ColorString


class Utils:
    EMAIL_REGEX = r'^[a-zA-Z]+[.][a-zA-Z]+@university\.com$'
    PASSWORD_REGEX = r'^(?=.*[A-Z])(?=.*\d{3,})[a-zA-Z\d]{6,}$'

def validate_email(email):
    return re.match(Utils.EMAIL_REGEX, email)

def validate_password(password):
    return re.match(Utils.PASSWORD_REGEX, password)

def admin_system():
    while True:
        
        action = input(ColorString.BlueGreen("Admin System (c/g/p/r/s/x): ")).lower()
        if action == 'x':
            break  # Exit the admin system
        # Handle other actions as needed
        else:
            print(ColorString.BlueGreen("Invalid action. Please try again"))

def student_system():
    while True:
        action = input(ColorString.BlueGreen("Student System (l/r/x): ")).lower()
        if action == 'x':
            break  # Exit the student system
        elif action == 'l':
            print(ColorString.Green("Student Sign In"))
            email = input("Email: ")
            password = input("Password: ")
            if validate_email(email) and validate_password(password):
                print(ColorString.Yellow("email and password formats acceptable"))
                name = input("Name: ")
                print(ColorString.Yellow(f"Enrolling Student {name}"))
            else:
                ColorString.Red(f"Incorrect email or password format")
        elif action == 'r':
            print(ColorString.Green("Student Sign In"))
            email = input("Email: ")
            password = input("Password: ")
            if validate_email(email) and validate_password(password):
                print(ColorString.Yellow("email and password formats acceptable"))
                name = input("Name: ")
                print(ColorString.Yellow(f"Enrolling Student {name}"))
            else:
                ColorString.Red(f"Incorrect email or password format")
        else:
            print(ColorString.BlueGreen("Invalid action."))

def university_system():
    while True:
        user_type = input(ColorString.BlueGreen("University System: (A) dmin, (S) tudent, or X : ")).lower()
        if user_type == 'a':
            admin_system()
        elif user_type == 's':
            student_system()
        elif user_type == 'x':
            print(ColorString.Yellow("Thank You"))
            break  # Exit the university system
        else:
            print(ColorString.BlueGreen("Invalid user type."))

# Run the university system
university_system()
