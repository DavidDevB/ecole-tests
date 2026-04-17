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


def test_set_teacher(mocker):
    course = Course("Français", date(2024, 1, 29), date(2024, 2, 16))
    teacher = mocker.Mock()

    course.set_teacher(teacher)

    assert course.teacher == teacher

def test_add_student(mocker):
    course = Course("Français", date(2024, 1, 29), date(2024, 2, 16))
    student = mocker.Mock()

    student.courses_taken = mocker.Mock()
    course.add_student(student)

    assert student in course.students_taking_it
    student.courses_taken.append.assert_called_once_with(course)

