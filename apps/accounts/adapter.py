from allauth.account.adapter import DefaultAccountAdapter
from django.conf import settings
from django.shortcuts import resolve_url
from datetime import datetime


class AccountAdapter(DefaultAccountAdapter):
    def get_login_redirect_url(self, request):
        """
        If the user has never logged in before we need them to
        create their club. However, last_login will be set before
        this is called, so we check if now() - last_login is suitably
        short to indicate a first-time login.
        """
        threshold = 90
        assert request.user.is_authenticated()
        if (datetime.now() - request.user.last_login).seconds < threshold:
            url = '/clubs/add/'
        else:
            url = settings.LOGIN_REDIRECT_URL
        return resolve_url(url)
