from django.db import models
from django.utils import timezone
# Create your models here.
from django.contrib.auth.models import User
#from patient.models import GroupAccount

def upload_location(instance, filename):
	return "%s/%s" %("patients", filename)


#family account
class GroupAccount(models.Model):

	group_identification_number = models.IntegerField(primary_key=True)
	group_name = models.CharField(max_length=30, blank=False)
	group_email = models.EmailField(max_length=30, blank=False)
	group_phone = models.CharField(max_length=15, blank=False)
	group_phone2 = models.CharField(max_length=15, blank=False)
	group_address = models.CharField(max_length=50, blank=True)  

	def __unicode__(self):
		return str(self.group_identification_number)

class Patient(models.Model):
	image = models.FileField(upload_to = upload_location, blank=True)
	
	patient_identification_number = models.IntegerField(primary_key=True)
	group_identification_number = models.ForeignKey(GroupAccount, blank=True, null=True)
	
	MR = 'Mr',
	MRS = 'Mrs',
	MS = 'Ms'

	option_title = (
			('MR', 'Mr'),
			('MRS', 'Mrs'),
			('MS', 'Ms'),
		)
    	patient_title = models.CharField(max_length=9, choices=option_title, default=' ')
	
	patient_first_name = models.CharField(max_length=30, blank=False)
	patient_middle_name = models.CharField(max_length=30, blank=False)
	patient_last_name = models.CharField(max_length=30, blank=False)
	
	MALE = 'MALE',
	FEMALE = 'FEMALE'

	option_sex = (
			('MALE', 'Male'),
			('FEMALE', 'Female'),
		)
    	patient_sex = models.CharField(max_length=9, choices=option_sex, blank=False)
	
	patient_tribe = models.CharField(max_length=30, blank=False)
	patient_religion = models.CharField(max_length=30, blank=False)
	patient_occupation = models.CharField(max_length=30, blank=False)
	
	SINGLE = 'SINGLE',
	MARRIED = 'MARRIED',
	WIDOWED = 'WIDOWED',
	SEPERATED = 'SEPERATED',

	option_status = (
			('SINGLE', 'Single'),
			('MARRIED', 'Married'),
			('WIDOWED', 'Widdowed'),
			('SEPERATED', 'Separated'),
		)
    	patient_marital_status = models.CharField(max_length=10, choices=option_status, blank=False)
	

	patient_address = models.CharField(max_length=50, blank=False)
	patient_next_of_kin_name = models.CharField(max_length=30, blank=False)
	patient_next_of_kin_number = models.CharField(max_length=30, blank=False)
	patient_next_of_kin_email = models.EmailField(max_length=30, blank=False)
	patient_phone = models.CharField(max_length=11, blank=False)
	patient_phone2 = models.CharField(max_length=11, blank=False)
	patient_email = models.EmailField(blank=True)
	created_by = models.CharField(max_length=20)
	date_registered = models.DateTimeField(default=timezone.now)

	#patient vitals
	patient_blood_group_and_genotype = models.CharField(max_length=11, blank=True)
	patient_pulse_rate = models.CharField(max_length=30, blank=True)
	patient_blood_pressure = models.CharField(max_length=30, blank=True)
	patient_respiratory_rate = models.CharField(max_length=30, blank=True)
	patient_temperature = models.CharField(max_length=30, blank=True)
	patient_weight = models.CharField(max_length=30, blank=True)

	def __unicode__(self):
		return str(self.patient_identification_number)

	def create_patient(sender, instance, created, **kwargs):
		if created:
			Patient.objects.create(user=instance)

		post_save.connect(create_patient, sender=User)


class Diagnosis(models.Model):
	diagnosis_identification_number = models.IntegerField(primary_key=True)
	doctor = models.ForeignKey(User)
	patient = models.ForeignKey(Patient)
	date_created = models.DateTimeField(default=timezone.now)
	diagnosis_class = models.CharField(max_length=50, blank=True)
	diagnosis_difinitive = models.TextField(max_length=255, blank=True)
	diagnosis_differential = models.TextField(max_length=255, blank=True)
	diagnosis_provincial = models.TextField(max_length=255, blank=True) 

	def __unicode__(self):
		return str(self.diagnosis_identification_number)


#Prescription
class Prescription(models.Model):
	prescription_identification_number = models.IntegerField(primary_key=True)
	doctor = models.ForeignKey(User)
	patient = models.ForeignKey(Patient)
	# diagnosis = models.ForeignKey(Diagnosis)
	date_created = models.DateTimeField(default=timezone.now)
	prescription_details = models.TextField(max_length=255, blank=False)
	prescription_price = models.IntegerField( blank=False)
	dispense_status = models.BooleanField(blank=True)

	def __unicode__(self):
		return str(self.prescription_identification_number)


#Patient Diagnosis
class Investigation(models.Model):
	investigation_identification_number = models.IntegerField(primary_key=True)
	doctor = models.ForeignKey(User)
	patient = models.ForeignKey(Patient)
	diagnosis = models.ForeignKey(Diagnosis)
	investigation_general_state = models.TextField(max_length=255, blank=False)
	investigation_view_requested = models.TextField(max_length=255, blank=False)
	investigation_anatomical_sites = models.TextField(max_length=255, blank=False)
	investigation_investigation_required = models.TextField(max_length=255, blank=False)
	#investigation_urgency
	date_created = models.DateTimeField(default=timezone.now)

	def __unicode__(self):
		return str(self.investigation_identification_number)


class Admission(models.Model):
	admission_identification_number = models.IntegerField(primary_key=True)
	admission_admitting_doctor = models.ForeignKey(User)
	patient = models.ForeignKey(Patient)
	date_created = models.DateTimeField(default=timezone.now)
	admission_diagnosis =models.TextField(max_length=255, blank=False)
	admission_date = models.DateTimeField(default=timezone.now)
	#admission_date_of_surgery = models.DateTimeField()

	ICU = 'ICU',
	EPU = 'EPU',
	GENERALWARD = 'GENERALWARD',
	PRIVATEWARD = 'PRIVATEWARD',

	option_ward_type = (
			('ICU', 'Single'),
			('EPU', 'Married'),
			('GENERAL WARD', 'General ward'),
			('PRIVATE WARD', 'Private ward'),
		)
	admission_ward_type = models.CharField(max_length=10, choices=option_ward_type, blank=True)

	def __unicode__(self):
		return str(self.admission_identification_number)


class Observation(models.Model):
	observation_identification_number = models.IntegerField(primary_key=True)
	doctor = models.ForeignKey(User)
	patient = models.ForeignKey(Patient)
	date_created = models.DateTimeField(default=timezone.now)
	observation_details =models.TextField(max_length=255, blank=False)

	def __unicode__(self):
		return str(self.observation_identification_number)
