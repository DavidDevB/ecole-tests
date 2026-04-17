import pytest

from models.address import Address
from models.person import Person
from models.student import Student
from models.teacher import Teacher
from models.course import Course
from datetime import date


def test_teacher():
    teacher = Teacher("Paul", "Dupont", 35, date(2024, 1, 29))

    assert teacher.first_name == "Paul"
    assert teacher.last_name == "Dupont"
    assert teacher.age == 35


def test_add_course(mocker):
    teacher = Teacher("Dupont", "Paul", 35, date(2024, 1, 29))
    course = mocker.Mock()

    teacher.add_course(course)

    assert teacher.courses_teached == [course]

    