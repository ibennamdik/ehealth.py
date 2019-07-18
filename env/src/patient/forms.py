from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.forms import ModelForm
from patient.models import *


from django.db.models import Q



class RegisterPatientForm(forms.ModelForm):
    class Meta:
        model = Patient

        fields = ['patient_first_name',
        'patient_middle_name','patient_last_name', 
        'patient_sex','patient_tribe',
        'patient_religion','patient_occupation','patient_email',
        'patient_marital_status','patient_address','patient_email',
        'patient_next_of_kin_name','patient_next_of_kin_number',
        'patient_phone','patient_phone2','group_identification_number']


  	def clean_email(self):
    		patient_email = self.cleaned_data['email']
    		if Patient.objects.filter(patient_email=patient_email).exists():
        		raise ValidationError("Email already exists")
    		return patient_email

class PatientUpdateForm(ModelForm):
    class Meta:
        model = Patient

        fields = ['patient_first_name',
        'patient_middle_name','patient_last_name', 
        'patient_sex','patient_tribe',
        'patient_religion','patient_occupation','patient_email',
        'patient_marital_status','patient_address','patient_email',
        'patient_phone','patient_phone2','patient_next_of_kin_name',
        'patient_next_of_kin_number']


class RegisterGroupForm(forms.ModelForm):
    class Meta:
        model = GroupAccount

        fields = ['group_name',
        'group_email','group_phone', 
        'group_phone2','group_address']

    def clean_email(self):
            group_email = self.cleaned_data['group_email']
            if Patient.objects.filter(group_email=group_email).exists():
                raise ValidationError("Email already exists")
            return group_email

class DiagnosisForm(forms.ModelForm):
    class Meta:
        model = Diagnosis

        fields = ['date_created','doctor','patient','diagnosis_class','diagnosis_difinitive',
        'diagnosis_differential','diagnosis_provincial']


class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription

        fields = ['date_created','doctor','patient','prescription_details','prescription_price','dispense_status']


class InvestigationForm(forms.ModelForm):
    class Meta:
        model = Investigation

        fields = ['date_created','doctor','patient','investigation_general_state',
        'investigation_view_requested','investigation_anatomical_sites','investigation_investigation_required']


class AdmissionForm(forms.ModelForm):
    class Meta:
        model = Admission

        fields = ['date_created','admission_admitting_doctor','patient','admission_diagnosis','admission_date','admission_ward_type']


class ObservationForm(forms.ModelForm):
    class Meta:
        model = Observation

        fields = ['date_created','doctor','patient','observation_details']

