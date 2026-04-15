import pytest


from business.school import School
from models.address import Address
from models.person import Person
from models.student import Student
from models.teacher import Teacher
from models.course import Course
from datetime import date

def test_add_course():
    school = School()
    course = Course("Français", date(2024, 1, 29), date(2024, 2, 16))

    school.add_course(course)

    assert school.courses == [course]


def test_add_teacher():
    school = School()
    teacher = Teacher("Dupont", "Paul", 35, date(2024, 1, 29))

    school.add_teacher(teacher)

    assert school.teachers == [teacher]


def test_add_student():
    school = School()
    student = Student("Dupont", "Paul", 35)

    school.add_student(student)

    assert school.students == [student]