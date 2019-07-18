from django.db import models
from django.utils import timezone
from django.conf import settings
# Create your models here.
from django.contrib.auth.models import User
from patient.models import *
from usermanagement.models import *
# Create your models here.
 

class Appointment(models.Model):
    appointment_identification_number = models.IntegerField(primary_key=True)
    doctor = models.ForeignKey(User)
    patient = models.OneToOneField(Patient)
    created_by = models.CharField(max_length=30, blank=False)
    
    PENDING = 'PND',
    COMPLETE = 'CPL',
    CANCELLED = 'CNC'    

    option_appointment_status  = (
		('PENDING', 'Pending'),
		('COMPLETE', 'Completed'),
		('CANCELLED', 'Cancelled')
	)

    appointment_status = models.CharField(
        max_length=9,
        choices=option_appointment_status,
        default='Pending'
    )

    date_created = models.DateTimeField(default=timezone.now)
    #date_scheduled = models.DateField()

    def __unicode__(self):
        return str(self.appointment_identification_number)

