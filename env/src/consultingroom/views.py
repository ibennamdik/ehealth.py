
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
from django.views.generic import ListView, DetailView

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

from frontdesk.forms import *
from .forms import CreateAppointmentForm
from django.views.decorators.csrf import csrf_exempt, csrf_protect


# Create your views here.


class AppointmentList(ListView):
    model = Appointment


def home(request):  
    return render(request, "consultingroom/consultingroom_home.html", {})

@csrf_exempt
def create_appointment(request, search_id):
    if request.method == "POST":
        
        form = CreateAppointmentForm(request.POST)
         
        if form.is_valid():             
             #get patient id from db and send back with message
             form = form.save(commit=False)
             form.save()

             appointment_object = Appointment.objects.latest('appointment_identification_number')
             message = 'Appointment successfully registered'
             
        else:
            message = "Appointment cannot created at the moment"
            appointment_object = None

        context = {
        	'message' : message,
            'appointment_object' : appointment_object,
            'form': CreateAppointmentForm(initial={"patient": search_id, "createst_by":request.user})
        }

        return render(request, 'consultingroom/consultingroom_appointment.html', context)
    else:

    	context = {
        	'form': CreateAppointmentForm(initial={"patient": search_id, "createst_by":request.user})
        }
        return render(request, 'consultingroom/consultingroom_appointment.html', context)
