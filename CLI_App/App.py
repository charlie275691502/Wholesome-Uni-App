from UniversitySystem import UniversitySystem

university_system = UniversitySystem()

prompt = "University System: (A)dmin, (S)tudent, or E(x)it: "
command = input(prompt).lower()
while(command != "x") :
    if command == "a" :
        university_system.Admin()
    elif command == "s" :
        university_system.Student()
    command = input(prompt).lower()
    
print("Thank you. Hi ")