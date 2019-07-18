from django.db import models
from django.utils import timezone
# Create your models here.
from django.contrib.auth.models import User
#from patient.models import GroupAccount

def upload_location(instance, filename):
	return "%s/%s" %("patients", filename)


#Ward
class Ward(models.Model):

	ward_identification_number = models.IntegerField(primary_key=True)
	ward_name = models.CharField(max_length=30, blank=False)
	ward_type = models.CharField(max_length=30, blank=False)
	ward_location = models.CharField(max_length=30, blank=False)
	total_beds = models.IntegerField(blank=False)
	available_beds = models.IntegerField(blank=False)
	total_rooms = models.IntegerField(blank=False)
	
	def __unicode__(self):
		return str(self.ward_name)

class Bed(models.Model):

	bed_identification_number = models.IntegerField(primary_key=True)
	bed_type = models.CharField(max_length=30, blank=False)
	ward = models.ForeignKey(Ward)
	status = models.CharField(max_length=30, blank=False)
	
	def __unicode__(self):
		return str(self.bed_identification_number)