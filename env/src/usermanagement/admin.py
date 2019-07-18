from django.contrib import admin

# Register your models here.
from .forms import *
from .models import *

class StaffAdmin(admin.ModelAdmin):
	list_display = ["staff_identification_number","staff_first_name","staff_sex","staff_last_name","user","staff_email","staff_occupation"]
	form = StaffUpdateForm

admin.site.register(Staff, StaffAdmin)