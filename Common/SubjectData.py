import json
import random

class SubjectData():
    def __init__(self) -> None:
        self.id = "{:03d}".format(random.randint(1, 999))
        self.mark = random.randint(25, 100)
        self.grade = SubjectData.mark_to_grade(self.mark)
        self.is_fail = self.grade == 'F'
        
    @staticmethod
    def mark_to_grade(mark):
        if mark >= 85:
            return 'HD'
        elif mark >= 75:
            return 'D'
        elif mark >= 65:
            return 'C'
        elif mark >= 50:
            return 'P'
        else:
            return 'F'
        
    def __str__(self):
        return f"[ Subject::{self.id} -- mark = {self.mark} -- grade = {self.grade}]"
        