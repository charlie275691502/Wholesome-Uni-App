from ColorString import ColorString


class AdminSystem:
    def admin_start(self):
        
        prompt = ColorString.BlueGreen("Admin System (c/g/p/r/s/x): ")
        command = input(prompt).lower()
        while(command != "x") :
            if command == "c" :
                AdminSystem().admin_clear()
            elif command == "g" :
                AdminSystem().admin_group()
            elif command == "p":
                AdminSystem().admin_partition()
            elif command == "r":
                AdminSystem().admin_remove()
            elif command == "s":
                AdminSystem().admin_show()
            command = input(prompt).lower()
    
    def admin_clear(self):
        print(ColorString.Yellow("Clearing students database"))
        prompt = ColorString.Red("Are you sure you want to clear the database (Y)ES/(N)O:")
        command = input(prompt).lower()
        while(command != "n") :
            if command == "y" :
                print("*****Clear code put here******")                   #code for cleaning all student data
                print(ColorString.Yellow("tudent data cleared"))
            command = input(prompt).lower()

    def admin_group(self):
        print(ColorString.Yellow("Grade Grouping"))
        print("Selected Admin group student")           #code for showing all student by Grade

    def admin_partition(self):
        print(ColorString.Yellow("PASS/FAIL Partition"))
        print("Selected Admin partition student")       #code for listing PASS+FAIL student all student data

    def admin_remove(self):
        prompt = "Remove by ID: "
        command = input(prompt)
        print("\033[0;33m Removing Student " + command + " Account \033[0m") #wait to connet to database
    
        print("Selected Admin remove")      #code for remove ONE student data

    def admin_show(self):
        print(ColorString.Yellow("Student List"))
        print("Selected Admin show")        #code for showing all student data




