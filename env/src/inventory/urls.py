from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin 
    
urlpatterns = [

    url(r'^$', 'inventory.views.home', name='inventory_home'),
	url(r'^addproduct/$', 'inventory.views.add_product', name='add_product'),
	url(r'^addmanufacturer/$', 'inventory.views.add_manufacturer', name='add_manufacturer'),
	url(r'^addcategory/$', 'inventory.views.add_category', name='add_category'),
	url(r'^addsupplier/$', 'inventory.views.add_supplier', name='add_supplier'),

	url(r'^search/$', 'inventory.views.search_product', name='search'),
    

]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


