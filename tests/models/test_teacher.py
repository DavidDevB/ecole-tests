import pytest

from models.address import Address
from models.person import Person
from models.student import Student
from models.teacher import Teacher
from models.course import Course
from datetime import date


def test_teacher():
    teacher = Teacher("Dupont", "Paul", 35, date(2024, 1, 29))

    assert teacher.first_name == "Paul"
    assert teacher.last_name == "Dupont"
    assert teacher.age == 35


def test_add_course():
    sut = Teacher("Dupont", "Paul", 35, date(2024, 1, 29))
    course = Course("Français", date(2024, 1, 29), date(2024, 2, 16))

    sut.add_course(course)

    assert sut.courses_teached == [course]

    