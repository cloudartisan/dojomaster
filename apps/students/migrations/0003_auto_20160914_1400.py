# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-14 14:00
from __future__ import unicode_literals

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20160914_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='dob',
            field=models.DateField(blank=True, null=True, verbose_name='Date of Birth'),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='E-mail Address'),
        ),
        migrations.AlterField(
            model_name='student',
            name='home_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='student',
            name='mobile_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='student',
            name='work_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128),
        ),
    ]
