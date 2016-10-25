from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from .models import Student


class StudentTests(TestCase):
    """Student model tests."""

    def test_full_name(self):
        student = Student(first_name='John', last_name='Smith')
        self.assertEquals(student.full_name, 'John Smith')

    def test_str(self):
        student = Student(first_name='John', last_name='Smith')
        self.assertEquals(str(student), 'John Smith')


def redirect_url(url_name, next_url_name=None, *args, **kwargs):
    url = reverse(url_name) + "?next=" + reverse(next_url_name, kwargs=kwargs)
    return url


class StudentsLoginRequiredTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_students_list(self):
        response = self.client.get(reverse('students-list'))
        expected_redirect = redirect_url('account_login', 'students-list')
        self.assertRedirects(response, expected_redirect)
