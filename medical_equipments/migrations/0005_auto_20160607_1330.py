# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-07 08:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('medical_equipments', '0004_auto_20160606_2226'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='amc_upto',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='AMC Upto'),
        ),
        migrations.AddField(
            model_name='equipment',
            name='country',
            field=models.CharField(default='India', max_length=100, verbose_name='Country'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='equipment',
            name='equipment_category',
            field=models.CharField(choices=[('Surgical/Operation Theater(OT)', 'Surgical/Operation Theater(OT)'), ('Laboratory', 'Laboratory'), ('radiology', 'radiology'), ('Dental', 'Dental'), ('ENT', 'ENT'), ('Sterlization Equipment', 'Sterlization Equipment'), ('Physiotherapy and Rehabilation', 'Physiotherapy and Rehabilation'), ('Emergency', 'Emergency'), ('Endoscopy/Laparoscopy', 'Endoscopy/Laparoscopy'), ('Cardiology', 'Cardiology'), ('Blood Bank', 'Blood Bank'), ('Maternal and Child Care', 'Maternal and Child Care'), ('Ophthalmology', 'Ophthalmology'), ('Out Patient Department(OPD)', 'Out Patient Department(OPD)'), ('Interiar Care Unit(ICU)', 'Interiar Care Unit(ICU)'), ('Others', 'Others')], default=datetime.datetime(2016, 6, 7, 7, 59, 49, 571623, tzinfo=utc), max_length=40, verbose_name='Equipment Category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='equipment',
            name='equipment_model',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Equipment Model'),
        ),
        migrations.AddField(
            model_name='equipment',
            name='equipment_name',
            field=models.CharField(default=datetime.datetime(2016, 6, 7, 8, 0, 3, 295577, tzinfo=utc), max_length=100, verbose_name='Equipment Name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='equipment',
            name='id_available',
            field=models.CharField(choices=[('No', 'No'), ('Yes', 'Yes')], default=datetime.datetime(2016, 6, 7, 8, 0, 28, 7686, tzinfo=utc), max_length=3, verbose_name='Equipment ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='equipment',
            name='installation_date',
            field=models.CharField(default=datetime.datetime(2016, 6, 7, 8, 0, 34, 230027, tzinfo=utc), max_length=15, verbose_name='Date of Installation'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='equipment',
            name='is_warranty',
            field=models.CharField(choices=[('No', 'No'), ('Yes', 'Yes')], default=datetime.datetime(2016, 6, 7, 8, 0, 36, 925670, tzinfo=utc), max_length=3, verbose_name='Warranty Status'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='equipment',
            name='manufacturar',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Manufacturar'),
        ),
        migrations.AddField(
            model_name='equipment',
            name='not_working_since',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Not Working Since'),
        ),
        migrations.AddField(
            model_name='equipment',
            name='remarks',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Remarks'),
        ),
        migrations.AddField(
            model_name='equipment',
            name='under_amc',
            field=models.CharField(choices=[('No', 'No'), ('Yes', 'Yes')], default=datetime.datetime(2016, 6, 7, 8, 0, 39, 919913, tzinfo=utc), max_length=3, verbose_name='Under AMC/CMC'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='equipment',
            name='warranty_expiry',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Warranty Expiray Date'),
        ),
        migrations.AddField(
            model_name='equipment',
            name='working_condition',
            field=models.CharField(choices=[('Working', 'Working'), ('Not Working', 'Not Working')], default=datetime.datetime(2016, 6, 7, 8, 0, 41, 720021, tzinfo=utc), max_length=12, verbose_name='Working Condition'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='equipment',
            name='equipment_id',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Enter Equipment ID'),
        ),
    ]
