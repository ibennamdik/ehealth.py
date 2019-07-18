from django.db import models
from django.utils import timezone
# Create your models here.
from django.contrib.auth.models import User
from patient.models import *
from usermanagement.models import *


class Category(models.Model):
	category_identification_number = models.IntegerField(primary_key=True)
	category_name = models.CharField(max_length=30, blank=False)

	def __unicode__(self):
		return str(self.category_name)

class Manufacturer(models.Model):
	manufacturer_identification_number = models.IntegerField(primary_key=True)
	manufacturer_name = models.CharField(max_length=30, blank=False)
	manufacturer_phone = models.CharField(max_length=30, blank=False)
	manufacturer_address = models.CharField(max_length=30, blank=True)
	manufacturer_email = models.EmailField(max_length=30, blank=True)
	
	def __unicode__(self):
		return str(self.manufacturer_name)

class Supplier(models.Model):
	supplier_identification_number = models.IntegerField(primary_key=True)
	supplier_name = models.CharField(max_length=30, blank=False)
	supplier_phone = models.CharField(max_length=30, blank=False)
	supplier_address = models.CharField(max_length=30, blank=True)
	supplier_email = models.EmailField(max_length=30, blank=True)
	
	def __unicode__(self):
		return str(self.supplier_name)

class Product(models.Model):
	product_identification_number = models.IntegerField(primary_key=True)
	product_name = models.CharField(max_length=30, blank=False)
	product_category = models.ForeignKey(Category, blank=False)
	product_manufacturer = models.ForeignKey(Manufacturer, blank=False)
	product_supplier = models.ForeignKey(Supplier, blank=False)
	product_description = models.CharField(max_length=50, blank=True)
	product_price_per_unit = models.IntegerField()
	product_quantity_in_stock = models.IntegerField()

	def __unicode__(self):
		return str(self.product_name)

class Invoice(models.Model):
	invoice_identification_number = models.IntegerField(primary_key=True)
	patient = models.ForeignKey(Patient)
	staff = models.ForeignKey(Staff)
	total_amount = models.IntegerField()

	def __unicode__(self):
		return str(self.invoice_identification_number)
