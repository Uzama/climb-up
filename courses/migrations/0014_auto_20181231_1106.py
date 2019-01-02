# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-12-31 11:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0013_auto_20181231_0852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='english',
            field=models.PositiveIntegerField(blank=True, choices=[(75, 'A'), (65, 'B'), (55, 'C'), (35, 'S'), (0, 'W')], default='S'),
        ),
        migrations.AlterField(
            model_name='course',
            name='maths',
            field=models.PositiveIntegerField(blank=True, choices=[(75, 'A'), (65, 'B'), (55, 'C'), (35, 'S'), (0, 'W')], default='S'),
        ),
        migrations.AlterField(
            model_name='course',
            name='result1',
            field=models.PositiveIntegerField(choices=[(75, 'A'), (65, 'B'), (55, 'C'), (35, 'S'), (0, 'W')], default='S'),
        ),
        migrations.AlterField(
            model_name='course',
            name='result2',
            field=models.PositiveIntegerField(choices=[(75, 'A'), (65, 'B'), (55, 'C'), (35, 'S'), (0, 'W')], default='S'),
        ),
        migrations.AlterField(
            model_name='course',
            name='result3',
            field=models.PositiveIntegerField(choices=[(75, 'A'), (65, 'B'), (55, 'C'), (35, 'S'), (0, 'W')], default='S'),
        ),
        migrations.AlterField(
            model_name='course',
            name='science',
            field=models.PositiveIntegerField(blank=True, choices=[(75, 'A'), (65, 'B'), (55, 'C'), (35, 'S'), (0, 'W')], default='S'),
        ),
    ]
