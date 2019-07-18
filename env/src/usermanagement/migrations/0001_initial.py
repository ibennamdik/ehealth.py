# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('staff_identification_number', models.IntegerField(serialize=False, primary_key=True)),
                ('staff_middle_name', models.CharField(default=b'', max_length=30)),
                ('staff_title', models.CharField(default=b' ', max_length=12, choices=[(b'DOCTOR', b'Doct.'), (b'PHARMACIST', b'Pharm.'), (b'NURSE', b'Nur.'), (b'LAB TECH', b'Tech.'), (b'ACCOUNTANT', b'Acct.')])),
                ('staff_sex', models.CharField(max_length=9, choices=[(b'MALE', b'Male'), (b'FEMALE', b'Female')])),
                ('staff_tribe', models.CharField(max_length=30, blank=True)),
                ('staff_religion', models.CharField(max_length=30, blank=True)),
                ('staff_occupation', models.CharField(max_length=30, blank=True)),
                ('staff_marital_status', models.CharField(max_length=10, choices=[(b'SINGLE', b'Single'), (b'MARRIED', b'Married'), (b'WIDOWED', b'Widdowed'), (b'SEPERATED', b'Separated')])),
                ('staff_email', models.EmailField(max_length=30, blank=True)),
                ('staff_address', models.CharField(max_length=50, blank=True)),
                ('staff_known_allergy', models.CharField(max_length=50, blank=True)),
                ('staff_next_of_kin_name', models.CharField(max_length=30, blank=True)),
                ('staff_next_of_relationship', models.CharField(max_length=30, blank=True)),
                ('staff_next_of_kin_number', models.CharField(max_length=30, blank=True)),
                ('staff_next_of_kin_email', models.EmailField(max_length=30, blank=True)),
                ('staff_phone', models.CharField(max_length=11, blank=True)),
                ('staff_phone2', models.CharField(max_length=11, blank=True)),
                ('date_registered', models.DateTimeField(default=django.utils.timezone.now)),
                ('staff_blood_group_and_genotype', models.CharField(max_length=11, blank=True)),
                ('staff_pulse_rate', models.CharField(max_length=30, blank=True)),
                ('staff_blood_pressure', models.CharField(max_length=30, blank=True)),
                ('staff_respiratory_rate', models.CharField(max_length=30, blank=True)),
                ('staff_temperature', models.CharField(max_length=30, blank=True)),
                ('staff_weight', models.CharField(max_length=30, blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
