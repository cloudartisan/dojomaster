from django.test import TestCase, Client
from django.core.urlresolvers import reverse


def redirect_url(url_name, next_url_name=None, *args, **kwargs):
    url = reverse(url_name) + "?next=" + reverse(next_url_name, kwargs=kwargs)
    return url


class ClubsLoginRequiredTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_clubs_list(self):
        response = self.client.get(reverse('clubs-list'))
        expected_redirect = redirect_url('account_login', 'clubs-list')
        self.assertRedirects(response, expected_redirect)
