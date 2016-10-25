from django.test import TestCase, Client
from django.core.urlresolvers import reverse


def redirect_url(url_name, next_url_name=None, *args, **kwargs):
    url = reverse(url_name) + "?next=" + reverse(next_url_name, kwargs=kwargs)
    return url


class AttendanceLoginRequiredTests(TestCase):
    def setUp(self):
        self.client = Client()

    def _test_named_url(self, url_name):
        response = self.client.get(reverse(url_name))
        expected_redirect = redirect_url('account_login', url_name)
        self.assertRedirects(response, expected_redirect)

    def test_attendance_list(self):
        response = self.client.get(reverse('attendance-list'))
        expected_redirect = redirect_url('account_login', 'attendance-list')
        self.assertRedirects(response, expected_redirect)
