# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('appointment_identification_number', models.IntegerField(serialize=False, primary_key=True)),
                ('created_by', models.CharField(max_length=30)),
                ('appointment_status', models.CharField(default=b'Pending', max_length=9, choices=[(b'PENDING', b'Pending'), (b'COMPLETE', b'Completed'), (b'CANCELLED', b'Cancelled')])),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('doctor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('patient', models.OneToOneField(to='patient.Patient')),
            ],
        ),
    ]
