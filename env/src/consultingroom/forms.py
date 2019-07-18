from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.forms import ModelForm
from patient.models import Patient, GroupAccount
from consultingroom.models import Appointment


from django.db.models import Q


class CreateAppointmentForm(forms.ModelForm):
     class Meta:
         model = Appointment
         fields = ['doctor', 'patient','appointment_status']
        # exclude = ('appointment_identification_number',)