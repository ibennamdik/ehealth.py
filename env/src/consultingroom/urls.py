from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin 
from consultingroom.views import AppointmentList

urlpatterns = [

    url(r'^$', 'consultingroom.views.home', name='consultingroom_home'),
    url(r'^register_patient/$', 'patient.views.register_patient', name='patient_register'),
    url(r'^register_group/$', 'patient.views.register_group', name='group_register'),
    url(r'^search/$', 'patient.views.searchPatient', name='search'),
    url(r'^(?P<search_id>[0-9]+)/$', 'patient.views.patient_profile', name='patient_profile'),
    url(r'^(?P<search_id>[0-9]+)/$', 'usermanagement.views.staff_update', name='staff_update'),
    url(r'^createappointment/(?P<search_id>[0-9]+)/$', 'consultingroom.views.create_appointment', name='create_appointment'),
    
    url(r'^appointment/$', AppointmentList.as_view(), name='appointments'),

    #url(r'^appointment/create/$', 'consultingroom.views.create_appointment', name='create_appointment'),
    #url(r'^appointment/list/$', views.BookingListView.as_view(), name='booking_list'),
    ]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


