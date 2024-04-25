
# ANSI color codes
RED = '\033[91m'
BLUE_GREEN = '\033[96m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'

class ColorString():
    @staticmethod
    def Red(str: str) -> str:
        return f"{RED}str{RESET}"
    
    @staticmethod
    def BlueGreen(str: str) -> str:
        return f"{BLUE_GREEN}str{RESET}"
    
    @staticmethod
    def Green(str: str) -> str:
        return f"{GREEN}str{RESET}"
    
    @staticmethod
    def Yellow(str: str) -> str:
        return f"{RESET}str{RESET}"