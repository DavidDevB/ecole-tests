import pytest

from models.address import Address
from models.person import Person
from models.student import Student
from models.teacher import Teacher
from models.course import Course
from datetime import date


def test_student():
    student = Student("Paul", "Dupont", 35)
    assert student.first_name == "Paul"
    assert student.last_name == "Dupont"
    assert student.age == 35


def test_add_course():
    sut = Student("Dupont", "Paul", 35)
    course = Course("Français", date(2024, 1, 29), date(2024, 2, 16))

    sut.add_course(course)

    assert sut.courses_taken == [course]