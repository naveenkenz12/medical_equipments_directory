# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-05 15:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medical_equipments', '0002_auto_20160605_2029'),
    ]

    operations = [
        migrations.RenameField(
            model_name='district_admin',
            old_name='age',
            new_name='agex',
        ),
        migrations.RenameField(
            model_name='request_for_district_admin',
            old_name='age',
            new_name='agex',
        ),
        migrations.RenameField(
            model_name='state_admin',
            old_name='age',
            new_name='agex',
        ),
    ]