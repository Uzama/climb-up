# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-01-05 17:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streames', '0003_auto_20190105_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stream',
            name='stream',
            field=models.CharField(choices=[('bio', 'biological_science'), ('maths', 'physical_science'), ('commerce', 'commerce'), ('arts', 'arts'), ('btech', 'bio_technology'), ('etech', 'engineering_technology'), ('ict', 'ict'), ('others', 'others')], default=None, max_length=120),
        ),
    ]
