# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_auto_20161031_1410'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prescription',
            name='diagnosis',
        ),
        migrations.AddField(
            model_name='prescription',
            name='dispense_status',
            field=models.BooleanField(default=datetime.datetime(2016, 11, 11, 2, 48, 8, 778587, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
