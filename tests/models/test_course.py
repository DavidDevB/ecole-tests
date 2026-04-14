import pytest

from models.address import Address
from models.course import Course
from models.person import Person
from models.student import Student
from models.teacher import Teacher
from datetime import date

def test_course():
    course = Course("Français", date(2024, 1, 29), date(2024, 2, 16))

    assert course.name == "Français"
    assert course.start_date == date(2024, 1, 29)
    assert course.end_date == date(2024, 2, 16)
    assert course.teacher is None


def test_set_teacher():
    sut = Course("Français", date(2024, 1, 29), date(2024, 2, 16))
    teacher = Teacher("Dupont", "Paul", 35, date(2024, 1, 29))

    sut.set_teacher(teacher)

    assert sut.teacher == teacher

def test_add_student():
    sut = Course("Français", date(2024, 1, 29), date(2024, 2, 16))
    student = Student("Dupont", "Paul", 35)

    sut.add_student(student)

    assert sut.students_taking_it == [student]


