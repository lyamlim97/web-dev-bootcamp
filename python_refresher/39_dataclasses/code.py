from dataclasses import dataclass, field
from typing import List


class Student:
    def __init__(self, name: str, grades: List[int] = None):
        self.name = name
        self.grades = grades or []

    def take_exam(self, result):
        self.grades.append(result)


bob = Student('Bob')

bob.take_exam(90)
print(bob.grades)
print(bob)


# as dataclass
@dataclass
class Student:
    name: str
    grades: List[int] = field(default_factory=list)

    def take_exam(self, result):
        self.grades.append(result)


bob = Student('Bob')

bob.take_exam(90)
print(bob.grades)
print(bob)
