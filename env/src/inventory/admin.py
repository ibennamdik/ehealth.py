from django.contrib import admin

from inventory.models import *


class ProductAdmin(admin.ModelAdmin):
	list_display = ["product_identification_number", "product_name","product_category","product_manufacturer","product_supplier","product_price_per_unit","product_quantity_in_stock"]

class CategoryAdmin(admin.ModelAdmin):
	list_display = ["category_identification_number", "category_name"]
	
class ManufacturerAdmin(admin.ModelAdmin):
	list_display = ["manufacturer_identification_number", "manufacturer_name","manufacturer_phone","manufacturer_email"]

class SupplierAdmin(admin.ModelAdmin):
	list_display = ["supplier_identification_number", "supplier_name","supplier_phone","supplier_email"]

class InvoiceAdmin(admin.ModelAdmin):
	list_display = ["invoice_identification_number", "patient","staff","total_amount"]


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Invoice, InvoiceAdmin)