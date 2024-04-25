import re

# ANSI color codes
RED = '\033[91m'
BLUE_GREEN = '\033[96m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'

class Utils:
    EMAIL_REGEX = r'^[a-zA-Z]+[.][a-zA-Z]+@university\.com$'
    PASSWORD_REGEX = r'^(?=.*[A-Z])(?=.*\d{3,})[a-zA-Z\d]{6,}$'

def validate_email(email):
    return re.match(Utils.EMAIL_REGEX, email)

def validate_password(password):
    return re.match(Utils.PASSWORD_REGEX, password)

def admin_system():
    while True:
        action = input(BLUE_GREEN + "Admin System (c/g/p/r/s/x): " + RESET).lower()
        if action == 'x':
            break  # Exit the admin system
        # Handle other actions as needed
        else:
            print(BLUE_GREEN + "Invalid action. Please try again." + RESET)

def student_system():
    while True:
        action = input(BLUE_GREEN + "Student System (l/r/x): " + RESET).lower()
        if action == 'x':
            break  # Exit the student system
        elif action == 'l':
            print(GREEN + "Student Sign In" + RESET)
            email = input("Email: ")
            password = input("Password: ")
            if validate_email(email) and validate_password(password):
                print(YELLOW + "email and password formats acceptable" + RESET)
                name = input("Name: ")
                print(YELLOW + f"Enrolling Student {name}" + RESET)
            else:
                print(RED + "Incorrect email or password format" + RESET)
        elif action == 'r':
            print(GREEN + "Student Sign Up" + RESET)
            email = input("Email: ")
            password = input("Password: ")
            if validate_email(email) and validate_password(password):
                print(YELLOW + "email and password formats acceptable" + RESET)
                name = input("Name: ")
                print(YELLOW + f"Enrolling Student {name}" + RESET)
            else:
                print(RED + "Incorrect email or password format" + RESET)
        else:
            print(BLUE_GREEN + "Invalid action." + RESET)

def university_system():
    while True:
        user_type = input(BLUE_GREEN + "University System: (A) dmin, (S) tudent, or X : " + RESET).lower()
        if user_type == 'a':
            admin_system()
        elif user_type == 's':
            student_system()
        elif user_type == 'x':
            print(YELLOW + "Thank You" + RESET)
            break  # Exit the university system
        else:
            print(BLUE_GREEN + "Invalid user type." + RESET)

# Run the university system
university_system()
