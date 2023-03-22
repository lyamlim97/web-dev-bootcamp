from typing import List


class Student:
    def __init__(self, name: str, grades: List[int] = []):
        self.name = name
        self.grades = grades

    def take_exam(self, result: int):
        self.grades.append(result)


bob = Student('Bob')
rolf = Student('Rolf')
bob.take_exam(90)
print(bob.grades)
print(rolf.grades)


class Student:
    def __init__(self, name: str, grades: List[int] = None):
        self.name = name
        self.grades = grades or []

    def take_exam(self, result):
        self.grades.append(result)


bob = Student('Bob')
rolf = Student('Rolf')
bob.take_exam(90)
print(bob.grades)
print(rolf.grades)
