from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin 

from patient import views

urlpatterns = [

    url(r'^$', 'patient.views.home', name='patient_home'),
    url(r'^register_patient/$', 'patient.views.register_patient', name='patient_register'),
    url(r'^register_group/$', 'patient.views.register_group', name='group_register'),
    url(r'^search/$', 'patient.views.searchPatient', name='search'),
    #url(r'^(?P<search_id>[0-9]+)/$', 'patient.views.patient_profile', name='patient_profile'),
    url(r'^createappointment/(?P<search_id>[0-9]+)/$', 'consultingroom.views.create_appointment', name='create_appointment'),
    url(r'^edit/(?P<search_id>\d+)$', 'patient.views.patient_update', name='patient_update'),
    
    url(r'^diagnose_patient/(?P<search_id>[0-9]+)/$', 'patient.views.diagnose_patient', name='patient_diagnose'),
    
    url(r'^admit_patient/(?P<search_id>[0-9]+)/$', 'patient.views.admit_patient', name='patient_admission'),
    
    url(r'^admit_patient/$', 'patient.views.admit_patient', name='patient_admission'),
    
    url(r'^medical_records/(?P<search_id>[0-9]+)/$', 'patient.views.medical_records', name='patient_records'),
        


    #url(r'^search/(?q<query>\d+)/$', 'patient.views.search', name='search'),
	#url(r'^patient_profile/$', 'patient.views.patient_profile', name='patient_profile'),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


