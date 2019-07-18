from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django import template
from django.template.loader import get_template
from django.template import Context, Template
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.template import RequestContext
from django.contrib.auth.models import User
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from account.models import *
from bloodbank.models import *
from consultingroom.models import *
from frontdesk.models import *
from hospital.models import *
from inventory.models import *
from laboratory.models import *
from patient.models import *
from pharmacy.models import *
from theatre.models import *
from usermanagement.models import *

from inventory.forms import *




# home View
def home(request):
	return render(request, "inventory/inventory_home.html", {})

@csrf_exempt
def add_product(request):
    if request.method == "POST":
        
        form = ProductForm(request.POST)

        if form.is_valid():             
             #get patient id from db and send back with message
             form = form.save(commit=False)
             form.created_by = request.user
             form.save()

             product_object = Product.objects.latest('product_identification_number')
             message = 'Product successfully added'
             
        else:
            message = 'Product addition failed',
            product_object = None

        context = {
        	'message' : message,
            'product_object' : product_object
        }

        return render(request, 'inventory/inventory_addproduct.html', context)
    else:

    	context = {
        	'form': ProductForm()
        }
        return render(request, 'inventory/inventory_addproduct.html', context)


def search_product(request):
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(product_name=query)
            #Q(patient_first_name=query) 
            #Q(authors__last_name__icontains=query)
        )
        results = Product.objects.filter(product_name=query)
        result = results.select_related('product_category').get(product_name=query)
    else:
        results = []
        result = []

    context = {
        "results": results,
        "result": result,
        "query": query
    }
    return render(request,'inventory/inventory_home.html', context)


@csrf_exempt
def add_manufacturer(request):
    if request.method == "POST":
        
        form = ManufacturerForm(request.POST)

        if form.is_valid():             
             #get patient id from db and send back with message
             form = form.save(commit=False)
             form.created_by = request.user
             form.save()

             manufacturer_object = Manufacturer.objects.latest('manufacturer_identification_number')
             message = 'Manufacturer successfully added'
             
        else:
            message = 'Manufacturer addition failed',
            manufacturer_object = None

        context = {
        	'message' : message,
            'manufacturer_object' : manufacturer_object
        }

        return render(request, 'inventory/inventory_addmanufacturer.html', context)
    else:

    	context = {
        	'form': ManufacturerForm()
        }
        return render(request, 'inventory/inventory_addmanufacturer.html', context)

@csrf_exempt
def add_supplier(request):
    if request.method == "POST":
        
        form = SupplierForm(request.POST)

        if form.is_valid():             
             #get patient id from db and send back with message
             form = form.save(commit=False)
             form.created_by = request.user
             form.save()

             manufacturer_object = Supplier.objects.latest('supplier_identification_number')
             message = 'Supplier successfully added'
             
        else:
            message = 'Supplier addition failed',
            supplier_object = None

        context = {
        	'message' : message,
            'supplier_object' : supplier_object
        }

        return render(request, 'inventory/inventory_addsupplier.html', context)
    else:

    	context = {
        	'form': SupplierForm()
        }
        return render(request, 'inventory/inventory_addsupplier.html', context)


@csrf_exempt
def add_category(request):
    if request.method == "POST":
        
        form = ProductCategoryForm(request.POST)

        if form.is_valid():             
             #get patient id from db and send back with message
             form = form.save(commit=False)
             form.created_by = request.user
             form.save()

             category_object = Category.objects.latest('category_identification_number')
             message = 'Category successfully added'
             
        else:
            message = 'Category addition failed',
            category_object = None

        context = {
        	'message' : message,
            'category_object' : category_object
        }

        return render(request, 'inventory/inventory_addcategory.html', context)
    else:

    	context = {
        	'form': ProductCategoryForm()
        }
        return render(request, 'inventory/inventory_addcategory.html', context)

