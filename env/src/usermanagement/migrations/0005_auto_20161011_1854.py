# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usermanagement', '0004_auto_20161011_1208'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='staff_first_name',
            field=models.CharField(max_length=30, blank=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='staff_last_name',
            field=models.CharField(max_length=30, blank=True),
        ),
    ]
