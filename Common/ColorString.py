
class ColorString():
    RED = '\033[91m'
    BLUE_GREEN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RESET = '\033[0m'

    @staticmethod
    def Red(str: str) -> str:
        return f"{ColorString.RED}{str}{ColorString.RESET}"
    
    @staticmethod
    def BlueGreen(str: str) -> str:
        return f"{ColorString.BLUE_GREEN}{str}{ColorString.RESET}"
    
    @staticmethod
    def Green(str: str) -> str:
        return f"{ColorString.GREEN}{str}{ColorString.RESET}"
    
    @staticmethod
    def Yellow(str: str) -> str:
        return f"{ColorString.YELLOW}{str}{ColorString.RESET}"