from __future__ import unicode_literals

from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'apps.accounts'
    verbose_name = 'RunMyDojo Accounts'

    def ready(self):
        from . import signals
