from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django import template
from django.template.loader import get_template
from django.template import Context, Template
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.template import RequestContext
from django.contrib.auth.models import User, models
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.db.models import Q

from django.views.generic.edit import CreateView, UpdateView, DeleteView

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
from patient.forms import *



def patient_update(request, search_id):
    patient = get_object_or_404(Patient, patient_identification_number=search_id)
    form = PatientUpdateForm(request.POST or None, instance=patient)
    if form.is_valid():
        
        message = 'Patient successfully updated'
        form.save()
        return redirect('/')
    else:
        message = 'Patient update Failed!'

    context = {
        'form':form,
        'message': message
    }
    return render(request, 'patient/patient_update_form.html', context)


# home View
def home(request):
    
    context = {
        
    }
    return render(request, "patient/patient_home.html", context)

@csrf_exempt
def register_patient(request):
    if request.method == "POST":
        
        form = RegisterPatientForm(request.POST)

        if form.is_valid():             
             #get patient id from db and send back with message
             form = form.save(commit=False)
             form.created_by = request.user
             form.save()

             patient_object = Patient.objects.latest('patient_identification_number')
             message = 'Patient successfully registered'
             
        else:
            message = 'Registeration failed',
            patient_object = None

        context = {
        	'message' : message,
            'patient_object' : patient_object
        }

        return render(request, 'patient/patient_register.html', context)
    else:

    	context = {
        	'form': RegisterPatientForm()
        }
        return render(request, 'patient/patient_register.html', context)


@csrf_exempt
def register_group(request):
    if request.method == "POST":
        
        form = RegisterGroupForm(request.POST)

        if form.is_valid():             
             #get patient id from db and send back with message
             form = form.save(commit=False)
             form.created_by = request.user
             form.save()

             group_object = GroupAccount.objects.latest('group_identification_number')
             message = 'Group successfully registered'
             
        else:
            message = 'Registeration failed',
            group_object = None

        context = {
            'message' : message,
            'group_object' : group_object
        }

        return render(request, 'patient/group_register.html', context)
    else:

        context = {
            'form': RegisterGroupForm()
        }
        return render(request, 'patient/group_register.html', context)


def searchPatient(request):
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(patient_identification_number=query)
            #Q(patient_first_name=query) 
            #Q(authors__last_name__icontains=query)
        )
        results = Patient.objects.filter(qset).distinct()

    else:
        results = []

    context = {
        "results": results,
        "query": query
    }
    return render(request,'patient/patient_home.html', context)


def patient_profile(request, search_id):
    if search_id:
        patient = Patient.objects.get(patient_identification_number=search_id)
        appointment = Appointment.objects.filter(patient=search_id)
        #appointment = get_object_or_404(Appointment, patient=search_id)
    else:
        appointment = []
        patient = []

    context = {
    "patient" : patient,
    "appointment":appointment,

    }
    return render(request, 'patient/patient_profile.html', context)



@csrf_exempt
def diagnose_patient(request, search_id):

    data ={'patient_identification_number':'{{search_id}}' }

    if request.method == "POST":

        form = DiagnosisForm(request.POST, initial=data)

        if form.is_valid():
            form.save()

            message = 'Saved!'
        else:
            message = 'Could not save data, Please try again!'

        context = {
            'message' : message
        }
        return render(request, 'patient/patient_diagnose.html', context)
    else:

        context = {
            'form' : DiagnosisForm(initial=data)
        }
        return render(request, 'patient/patient_diagnose.html', context)


def medical_records(request, search_id):
    if search_id:
        patient = Patient.objects.get(patient_identification_number=search_id)
        appointment = Appointment.objects.filter(patient=search_id)
        medical_records = Diagnosis.objects.filter(patient=search_id)
        admission = Admission.objects.filter(patient=search_id)
        #appointment = get_object_or_404(Appointment, patient=search_id)
        #print admission
    else:
        patient = []
        appointment = []
        medical_records = []
        admission = []

    context = {
    "patient" : patient,
    "appointment" : appointment,
    "medical_records" : medical_records,
    "admission" : admission
    
    }
    return render(request, 'patient/patient_records.html', context)

@csrf_exempt
def admit_patient(request, search_id):

    if request.method == "POST":

        form = AdmissionForm(request.POST)

        if form.is_valid():
            form.save()

            message = 'Patient Successfully Admitted!'
        else:
            message = 'Admission failed, Please try again!'

        context = {
            'message' : message
        }
        return render(request, 'patient/patient_admission.html', context)
    else:

        context = {
            'form' : AdmissionForm()
        }
        return render(request, 'patient/patient_admission.html', context)



def patients_admitted(request):

    context = {

    
    }
    return render(request, 'patient/admission_list.html', context)
