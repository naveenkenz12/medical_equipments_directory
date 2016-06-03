# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-03 08:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical_equipments', '0011_hospital'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='district',
            field=models.CharField(default=12456, max_length=100, verbose_name='District'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hospital',
            name='pincode',
            field=models.CharField(default=12556, max_length=12, verbose_name='Pin Code'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hospital',
            name='state',
            field=models.CharField(default=14855, max_length=30, verbose_name='State'),
            preserve_default=False,
        ),
    ]