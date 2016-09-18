# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-18 13:19
from __future__ import unicode_literals

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128)),
                ('mobile', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128)),
                ('fax', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
