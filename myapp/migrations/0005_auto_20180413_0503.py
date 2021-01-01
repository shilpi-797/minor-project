# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-12 23:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_newsletter_select'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='select',
            field=models.CharField(choices=[('friends', 'Friends'), ('search', 'Search Engine'), ('add', 'Advertisement'), ('others', 'Other')], default='friends', max_length=100),
        ),
    ]
