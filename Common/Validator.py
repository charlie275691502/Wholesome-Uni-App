import re

class Validator():
    @staticmethod
    def Email(email: str) -> bool:
        pattern = r'^[a-zA-Z]+\.[a-zA-Z]+@university\.com$'
        return bool(re.match(pattern, email))

    @staticmethod
    def Password(password: str) -> bool:
        pattern = r'^[A-Z][a-zA-Z]{5,}[0-9]{3,}$'
        return bool(re.match(pattern, password))