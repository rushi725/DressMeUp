# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-10-20 18:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0007_auto_20171020_2130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='number',
        ),
    ]
