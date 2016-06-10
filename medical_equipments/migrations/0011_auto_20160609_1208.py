# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-09 06:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical_equipments', '0010_auto_20160608_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='district',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='District'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='state',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='State'),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='district',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='District'),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='pincode',
            field=models.CharField(max_length=12, verbose_name='Pin Code/Zip Code'),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='state',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='State'),
        ),
    ]
