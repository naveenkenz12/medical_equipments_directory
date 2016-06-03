# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-02 07:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical_equipments', '0006_auto_20160602_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state_admin',
            name='email',
            field=models.EmailField(max_length=100, unique=True, verbose_name='Email ID/Username'),
        ),
        migrations.AlterField(
            model_name='state_admin',
            name='state',
            field=models.CharField(max_length=30, verbose_name='State'),
        ),
    ]
