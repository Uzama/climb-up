# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-12-26 07:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20181226_0704'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='result1',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('S', 'S'), ('W', 'W')], default='S', max_length=1),
        ),
        migrations.AddField(
            model_name='course',
            name='result2',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('S', 'S'), ('W', 'W')], default='S', max_length=1),
        ),
        migrations.AddField(
            model_name='course',
            name='result3',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('S', 'S'), ('W', 'W')], default='S', max_length=1),
        ),
        migrations.AddField(
            model_name='course',
            name='result4',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('S', 'S'), ('W', 'W')], default='S', max_length=1),
        ),
        migrations.AddField(
            model_name='course',
            name='result5',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('S', 'S'), ('W', 'W')], default='S', max_length=1),
        ),
    ]
