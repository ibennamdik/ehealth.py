from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin 

urlpatterns = [

    url(r'^$', 'frontdesk.views.home', name='front_desk_home'),
    url(r'^search/$', 'patient.views.searchPatient', name='search'),
    url(r'^createappointment/(?P<search_id>[0-9]+)/$', 'consultingroom.views.create_appointment', name='create_appointment'),
    url(r'^(?P<search_id>[0-9]+)/$', 'patient.views.patient_profile', name='patient_profile'),
    
    url(r'^admissions/$', 'patient.views.patients_admitted', name='admissions'),
    
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
