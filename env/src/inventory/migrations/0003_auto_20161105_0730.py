# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_invoice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invoice',
            old_name='recipient',
            new_name='staff',
        ),
    ]
