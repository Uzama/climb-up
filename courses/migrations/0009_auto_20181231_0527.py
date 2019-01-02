# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-12-31 05:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_auto_20181231_0517'),
    ]

    operations = [
        migrations.CreateModel(
            name='Requirement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(blank=True, max_length=200)),
                ('zscore', models.DecimalField(blank=True, decimal_places=4, default=0, max_digits=5)),
            ],
        ),
        migrations.RemoveField(
            model_name='course',
            name='district',
        ),
        migrations.RemoveField(
            model_name='course',
            name='zscore',
        ),
        migrations.AddField(
            model_name='requirement',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course'),
        ),
    ]
