# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-14 17:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pallevelugu', '0010_auto_20170914_1721'),
    ]

    operations = [
        migrations.AddField(
            model_name='farms',
            name='crop',
            field=models.CharField(max_length=20, null=True),
        ),
    ]