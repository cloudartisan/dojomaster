from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class School(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200)
    url = models.URLField(max_length=200, blank=True)
    phone = PhoneNumberField(blank=True)
    mobile = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
