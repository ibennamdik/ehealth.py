from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.forms import ModelForm

from patient.models import *
from inventory.models import *


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name','product_category','product_manufacturer', 
        'product_supplier','product_description','product_price_per_unit',
        'product_quantity_in_stock']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name']


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['supplier_name','supplier_phone','supplier_address', 
        'supplier_email']


class ManufacturerForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = ['manufacturer_name','manufacturer_phone','manufacturer_address', 
        'manufacturer_email']
