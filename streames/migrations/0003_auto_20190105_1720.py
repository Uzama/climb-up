# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-01-05 17:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streames', '0002_auto_20190105_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stream',
            name='stream',
            field=models.CharField(choices=[('Bio Science', 'biological_science'), ('Physcial Science', 'physical_science'), ('Commerce', 'commerce'), ('Arts', 'arts'), ('Btech', 'bio_technology'), ('Etech', 'engineering_technology'), ('ICT (Technology)', 'ict'), ('others', 'others')], default=None, max_length=120),
        ),
    ]