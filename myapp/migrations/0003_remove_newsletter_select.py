# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-12 09:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20180412_1435'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsletter',
            name='select',
        ),
    ]
