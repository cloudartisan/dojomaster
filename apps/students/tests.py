from django.test import TestCase

from .models import Student

class StudentTests(TestCase):
    """Student model tests."""

    def test_full_name(self):
        student = Student(first_name='John', last_name='Smith')
        self.assertEquals(student.full_name, 'John Smith')

    def test_str(self):
        student = Student(first_name='John', last_name='Smith')
        self.assertEquals(str(student), 'John Smith')

