from __future__ import unicode_literals

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Student(models.Model):
    # International standard codes for the representation of human sexes
    # http://en.wikipedia.org/wiki/ISO/IEC_5218
    GENDER_CHOICES = (
        (0, "Not Known"),
        (1, "Male"),
        (2, "Female"),
        (9, "Not Applicable"),
    )
    CONTACT_RELATION_CHOICES = (
        ("unknown", "Unknown"),
        ("parent", "Parent"),
        ("guardian", "Guardian"),
        ("family", "Family"),
        ("other", "Other"),
    )
    school = models.ForeignKey('school.School', on_delete=models.CASCADE)
    joined = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0)
    dob = models.DateField('Date of Birth',
            auto_now=False, auto_now_add=False,
            blank=True, null=True)
    email = models.EmailField('E-mail Address', blank=True)
    home_phone = PhoneNumberField(blank=True)
    work_phone = PhoneNumberField(blank=True)
    mobile_phone = PhoneNumberField(blank=True)
    contact = models.ForeignKey('students.Contact', null=True)
    contact_relation = models.CharField(max_length=10,
            choices=CONTACT_RELATION_CHOICES, default="unknown")

    class Meta:
        ordering = ('last_name',)

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name).title()


class Contact(models.Model):
    # International standard codes for the representation of human sexes
    # http://en.wikipedia.org/wiki/ISO/IEC_5218
    GENDER_CHOICES = (
        (0, "Not Known"),
        (1, "Male"),
        (2, "Female"),
        (9, "Not Applicable"),
    )
    updated = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    home_phone = PhoneNumberField(blank=True)
    work_phone = PhoneNumberField(blank=True)
    mobile_phone = PhoneNumberField(blank=True)
    email = models.EmailField('E-mail Address', blank=True)
    gender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0)

    class Meta:
        ordering = ('last_name',)

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name).title()
