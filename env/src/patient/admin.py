from django.contrib import admin
from patient.models import *
# Register your models here.


from .forms import *
from .models import *

class PatientAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "patient_first_name","patient_last_name","patient_middle_name","patient_email"]
	form = PatientUpdateForm


admin.site.register(Patient, PatientAdmin)
admin.site.register(GroupAccount)

admin.site.register(Diagnosis)
admin.site.register(Prescription)
admin.site.register(Investigation)




