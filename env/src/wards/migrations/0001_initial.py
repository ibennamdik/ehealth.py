# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bed',
            fields=[
                ('bed_identification_number', models.IntegerField(serialize=False, primary_key=True)),
                ('bed_type', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('ward_identification_number', models.IntegerField(serialize=False, primary_key=True)),
                ('ward_name', models.CharField(max_length=30)),
                ('ward_type', models.CharField(max_length=30)),
                ('ward_location', models.CharField(max_length=30)),
                ('total_beds', models.IntegerField()),
                ('available_beds', models.IntegerField()),
                ('total_rooms', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='bed',
            name='ward',
            field=models.ForeignKey(to='wards.Ward'),
        ),
    ]
