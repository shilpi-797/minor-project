# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-12 23:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20180413_0515'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newsletter',
            old_name='select',
            new_name='find',
        ),
    ]
