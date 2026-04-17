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


def test_add_course(mocker):
    student = Student("Dupont", "Paul", 35)
    course = mocker.Mock()

    student.add_course(course)

    assert student.courses_taken == [course]

def test_str_student():
    Student.students_nb = 0
    student = Student("Dupont", "Paul", 35)
    assert str(student) == "Paul Dupont, n° étudiant : 1"