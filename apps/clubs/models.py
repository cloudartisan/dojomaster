from __future__ import unicode_literals

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from organizations.models import Organization


class Club(Organization):
    updated = models.DateTimeField(auto_now=True)
    url = models.URLField(max_length=200, blank=True)
    phone = PhoneNumberField(blank=True)
    mobile = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
