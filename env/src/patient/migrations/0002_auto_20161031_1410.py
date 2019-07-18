# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='admission',
            old_name='doctor',
            new_name='admission_admitting_doctor',
        ),
    ]
