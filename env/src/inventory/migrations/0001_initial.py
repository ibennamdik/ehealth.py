# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_identification_number', models.IntegerField(serialize=False, primary_key=True)),
                ('category_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('manufacturer_identification_number', models.IntegerField(serialize=False, primary_key=True)),
                ('manufacturer_name', models.CharField(max_length=30)),
                ('manufacturer_phone', models.CharField(max_length=30)),
                ('manufacturer_address', models.CharField(max_length=30, blank=True)),
                ('manufacturer_email', models.EmailField(max_length=30, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_identification_number', models.IntegerField(serialize=False, primary_key=True)),
                ('product_name', models.CharField(max_length=30)),
                ('product_description', models.CharField(max_length=50, blank=True)),
                ('product_price_per_unit', models.IntegerField()),
                ('product_quantity_in_stock', models.IntegerField()),
                ('product_category', models.ForeignKey(to='inventory.Category')),
                ('product_manufacturer', models.ForeignKey(to='inventory.Manufacturer')),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('supplier_identification_number', models.IntegerField(serialize=False, primary_key=True)),
                ('supplier_name', models.CharField(max_length=30)),
                ('supplier_phone', models.CharField(max_length=30)),
                ('supplier_address', models.CharField(max_length=30, blank=True)),
                ('supplier_email', models.EmailField(max_length=30, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='product_supplier',
            field=models.ForeignKey(to='inventory.Supplier'),
        ),
    ]
