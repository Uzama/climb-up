# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-12-26 07:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0002_remove_subject_stream'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='level',
            field=models.CharField(choices=[('al', 'advanced_level'), ('ol', 'ordinary_level')], default='al', max_length=120),
        ),
    ]