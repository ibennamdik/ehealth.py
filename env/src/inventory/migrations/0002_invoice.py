# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_auto_20161031_1410'),
        ('usermanagement', '0007_auto_20161011_2024'),
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('invoice_identification_number', models.IntegerField(serialize=False, primary_key=True)),
                ('total_amount', models.IntegerField()),
                ('patient', models.ForeignKey(to='patient.Patient')),
                ('recipient', models.ForeignKey(to='usermanagement.Staff')),
            ],
        ),
    ]
