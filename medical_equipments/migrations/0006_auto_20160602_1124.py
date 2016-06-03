# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-02 05:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical_equipments', '0005_state_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='state_admin',
            name='address',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Address'),
        ),
        migrations.AddField(
            model_name='state_admin',
            name='email2',
            field=models.EmailField(blank=True, max_length=100, null=True, verbose_name='Alternate Email ID'),
        ),
        migrations.AddField(
            model_name='state_admin',
            name='mobile2',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Alernate Mobile No'),
        ),
    ]