# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-12-26 05:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('streames', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('level', models.CharField(choices=[('al', 'advanced_level'), ('ol', 'ordinary_level')], default=None, max_length=120)),
                ('stream', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='streames.Stream')),
            ],
        ),
    ]
