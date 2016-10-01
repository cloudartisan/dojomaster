from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _
from phonenumber_field.modelfields import PhoneNumberField
from organizations.models import Organization


class Club(Organization):
    date_created = models.DateTimeField(
        verbose_name=_('Date Created'),
        auto_now_add=True
    )
    date_updated = models.DateTimeField(
        verbose_name=_('Date Updated'),
        auto_now=True
    )
    url = models.URLField(max_length=200, blank=True)
    phone = PhoneNumberField(blank=True)
    mobile = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
