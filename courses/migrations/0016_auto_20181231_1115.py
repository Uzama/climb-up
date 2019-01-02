# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-12-31 11:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0015_remove_course_ordinary_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='english',
            field=models.CharField(blank=True, choices=[('75', 'A'), ('65', 'B'), ('55', 'C'), ('35', 'S'), ('0', 'W')], default='S', max_length=1),
        ),
        migrations.AlterField(
            model_name='course',
            name='maths',
            field=models.CharField(blank=True, choices=[('75', 'A'), ('65', 'B'), ('55', 'C'), ('35', 'S'), ('0', 'W')], default='S', max_length=1),
        ),
        migrations.AlterField(
            model_name='course',
            name='result1',
            field=models.CharField(choices=[('75', 'A'), ('65', 'B'), ('55', 'C'), ('35', 'S'), ('0', 'W')], default='S', max_length=1),
        ),
        migrations.AlterField(
            model_name='course',
            name='result2',
            field=models.CharField(choices=[('75', 'A'), ('65', 'B'), ('55', 'C'), ('35', 'S'), ('0', 'W')], default='S', max_length=1),
        ),
        migrations.AlterField(
            model_name='course',
            name='result3',
            field=models.CharField(choices=[('75', 'A'), ('65', 'B'), ('55', 'C'), ('35', 'S'), ('0', 'W')], default='S', max_length=1),
        ),
        migrations.AlterField(
            model_name='course',
            name='science',
            field=models.CharField(blank=True, choices=[('75', 'A'), ('65', 'B'), ('55', 'C'), ('35', 'S'), ('0', 'W')], default='S', max_length=1),
        ),
    ]