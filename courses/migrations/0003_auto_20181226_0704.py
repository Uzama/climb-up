# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-12-26 07:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0001_initial'),
        ('courses', '0002_auto_20181226_0647'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='subject1',
        ),
        migrations.AddField(
            model_name='course',
            name='subject1',
            field=models.ManyToManyField(default=None, related_name='subject1', to='subjects.Subject'),
        ),
        migrations.RemoveField(
            model_name='course',
            name='subject2',
        ),
        migrations.AddField(
            model_name='course',
            name='subject2',
            field=models.ManyToManyField(default=None, related_name='subject2', to='subjects.Subject'),
        ),
        migrations.RemoveField(
            model_name='course',
            name='subject3',
        ),
        migrations.AddField(
            model_name='course',
            name='subject3',
            field=models.ManyToManyField(default=None, related_name='subject3', to='subjects.Subject'),
        ),
        migrations.RemoveField(
            model_name='course',
            name='subject4',
        ),
        migrations.AddField(
            model_name='course',
            name='subject4',
            field=models.ManyToManyField(default=None, related_name='subject4', to='subjects.Subject'),
        ),
        migrations.RemoveField(
            model_name='course',
            name='subject5',
        ),
        migrations.AddField(
            model_name='course',
            name='subject5',
            field=models.ManyToManyField(default=None, related_name='subject5', to='subjects.Subject'),
        ),
    ]
