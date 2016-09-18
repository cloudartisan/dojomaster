from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class School(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200)
    phone = PhoneNumberField(blank=True)
    mobile = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
