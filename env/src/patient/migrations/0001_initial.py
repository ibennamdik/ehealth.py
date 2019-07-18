# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import patient.models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Admission',
            fields=[
                ('admission_identification_number', models.IntegerField(serialize=False, primary_key=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('admission_diagnosis', models.TextField(max_length=255)),
                ('admission_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('admission_ward_type', models.CharField(blank=True, max_length=10, choices=[(b'ICU', b'Single'), (b'EPU', b'Married'), (b'GENERAL WARD', b'General ward'), (b'PRIVATE WARD', b'Private ward')])),
                ('doctor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('diagnosis_identification_number', models.IntegerField(serialize=False, primary_key=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('diagnosis_class', models.CharField(max_length=50, blank=True)),
                ('diagnosis_difinitive', models.TextField(max_length=255, blank=True)),
                ('diagnosis_differential', models.TextField(max_length=255, blank=True)),
                ('diagnosis_provincial', models.TextField(max_length=255, blank=True)),
                ('doctor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GroupAccount',
            fields=[
                ('group_identification_number', models.IntegerField(serialize=False, primary_key=True)),
                ('group_name', models.CharField(max_length=30)),
                ('group_email', models.EmailField(max_length=30)),
                ('group_phone', models.CharField(max_length=15)),
                ('group_phone2', models.CharField(max_length=15)),
                ('group_address', models.CharField(max_length=50, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Investigation',
            fields=[
                ('investigation_identification_number', models.IntegerField(serialize=False, primary_key=True)),
                ('investigation_general_state', models.TextField(max_length=255)),
                ('investigation_view_requested', models.TextField(max_length=255)),
                ('investigation_anatomical_sites', models.TextField(max_length=255)),
                ('investigation_investigation_required', models.TextField(max_length=255)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('diagnosis', models.ForeignKey(to='patient.Diagnosis')),
                ('doctor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Observation',
            fields=[
                ('observation_identification_number', models.IntegerField(serialize=False, primary_key=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('observation_details', models.TextField(max_length=255)),
                ('doctor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('image', models.FileField(upload_to=patient.models.upload_location, blank=True)),
                ('patient_identification_number', models.IntegerField(serialize=False, primary_key=True)),
                ('patient_title', models.CharField(default=b' ', max_length=9, choices=[(b'MR', b'Mr'), (b'MRS', b'Mrs'), (b'MS', b'Ms')])),
                ('patient_first_name', models.CharField(max_length=30)),
                ('patient_middle_name', models.CharField(max_length=30)),
                ('patient_last_name', models.CharField(max_length=30)),
                ('patient_sex', models.CharField(max_length=9, choices=[(b'MALE', b'Male'), (b'FEMALE', b'Female')])),
                ('patient_tribe', models.CharField(max_length=30)),
                ('patient_religion', models.CharField(max_length=30)),
                ('patient_occupation', models.CharField(max_length=30)),
                ('patient_marital_status', models.CharField(max_length=10, choices=[(b'SINGLE', b'Single'), (b'MARRIED', b'Married'), (b'WIDOWED', b'Widdowed'), (b'SEPERATED', b'Separated')])),
                ('patient_address', models.CharField(max_length=50)),
                ('patient_next_of_kin_name', models.CharField(max_length=30)),
                ('patient_next_of_kin_number', models.CharField(max_length=30)),
                ('patient_next_of_kin_email', models.EmailField(max_length=30)),
                ('patient_phone', models.CharField(max_length=11)),
                ('patient_phone2', models.CharField(max_length=11)),
                ('patient_email', models.EmailField(max_length=254, blank=True)),
                ('created_by', models.CharField(max_length=20)),
                ('date_registered', models.DateTimeField(default=django.utils.timezone.now)),
                ('patient_blood_group_and_genotype', models.CharField(max_length=11, blank=True)),
                ('patient_pulse_rate', models.CharField(max_length=30, blank=True)),
                ('patient_blood_pressure', models.CharField(max_length=30, blank=True)),
                ('patient_respiratory_rate', models.CharField(max_length=30, blank=True)),
                ('patient_temperature', models.CharField(max_length=30, blank=True)),
                ('patient_weight', models.CharField(max_length=30, blank=True)),
                ('group_identification_number', models.ForeignKey(blank=True, to='patient.GroupAccount', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('prescription_identification_number', models.IntegerField(serialize=False, primary_key=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('prescription_details', models.TextField(max_length=255)),
                ('prescription_price', models.IntegerField()),
                ('diagnosis', models.ForeignKey(to='patient.Diagnosis')),
                ('doctor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(to='patient.Patient')),
            ],
        ),
        migrations.AddField(
            model_name='observation',
            name='patient',
            field=models.ForeignKey(to='patient.Patient'),
        ),
        migrations.AddField(
            model_name='investigation',
            name='patient',
            field=models.ForeignKey(to='patient.Patient'),
        ),
        migrations.AddField(
            model_name='diagnosis',
            name='patient',
            field=models.ForeignKey(to='patient.Patient'),
        ),
        migrations.AddField(
            model_name='admission',
            name='patient',
            field=models.ForeignKey(to='patient.Patient'),
        ),
    ]
