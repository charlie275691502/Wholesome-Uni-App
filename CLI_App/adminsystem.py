


class AdminSystem:
    def admin_start(self):
        
        prompt = "\033[0;36m Admin System (c/g/p/r/s/x): \033[0m"
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
        print("\033[0;33m Clearing students database \033[0m")
        prompt = "\033[0;31m Are you sure you want to clear the database (Y)ES/(N)O: \033[0m"
        command = input(prompt).lower()
        while(command != "n") :
            if command == "y" :
                print("*****Clear code put here******")                   #code for cleaning all student data
                print("\033[0;33m Student data cleared \033[0m")
                AdminSystem().admin_start()
            command = input(prompt).lower()

    def admin_group(self):
        print("\033[0;33m Grade Grouping \033[0m")
        print("Selected Admin group student")           #code for showing all student by Grade

    def admin_partition(self):
        print("\033[0;33m PASS/FAIL Partition \033[0m")
        print("Selected Admin partition student")       #code for listing PASS+FAIL student all student data

    def admin_remove(self):
        prompt = "Remove by ID: "
        command = input(prompt)
        print("\033[0;33m Removing Student " + command + " Account \033[0m")
        print("Selected Admin remove")      #code for remove ONE student data

    def admin_show(self):
        print("\033[0;33m Student List \033[0m")
        print("Selected Admin show")        #code for showing all student data




