from django.db import models
from django.utils import timezone
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed

# Create your models here.
from django.contrib.auth.models import *
from patient.models import *

def upload_location(instance, filename):
    return "%s/%s" %("staff", filename)


class Staff(models.Model):
    # This field is required.
    user = models.OneToOneField(User)
    # image = models.FileField(upload_to = upload_location, blank=True)
    staff_identification_number = models.IntegerField(primary_key=True)
    staff_first_name = models.CharField(max_length=30, blank=True)
    staff_last_name = models.CharField(max_length=30, blank=True)

    staff_middle_name = models.CharField(max_length=30, blank=False, default='')
    

    DOCTOR = 'Dr',
    PHARMACIST = 'Pharm',
    NURSE = 'Nur',
    LABTECH = 'Tech',
    ACCOUNTANT = 'Acct',

    option_title = (
            ('DOCTOR', 'Doct.'),
            ('PHARMACIST', 'Pharm.'),
            ('NURSE', 'Nur.'),
            ('LAB TECH', 'Tech.'),
            ('ACCOUNTANT', 'Acct.'),
        )
    staff_title = models.CharField(max_length=12, choices=option_title, default=' ')
    
    
    MALE = 'MALE',
    FEMALE = 'FEMALE'  

    option_sex  = (
            ('MALE', 'Male'),
            ('FEMALE', 'Female')
        )
    staff_sex = models.CharField(max_length=9, choices=option_sex)

    staff_tribe = models.CharField(max_length=30, blank=True)
    staff_religion = models.CharField(max_length=30, blank=True)
    staff_occupation = models.CharField(max_length=30, blank=True)
    
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
    staff_marital_status = models.CharField(max_length=10, choices=option_status, blank=False)
    
    staff_email = models.EmailField(max_length=30, blank=True)
    staff_address = models.CharField(max_length=50, blank=True)
    staff_known_allergy = models.CharField(max_length=50, blank=True)
    staff_next_of_kin_name = models.CharField(max_length=30, blank=True)
    staff_next_of_relationship = models.CharField(max_length=30, blank=True)
    staff_next_of_kin_number = models.CharField(max_length=30, blank=True)
    staff_next_of_kin_email = models.EmailField(max_length=30, blank=True)
    staff_phone = models.CharField(max_length=11, blank=True)
    staff_phone2 = models.CharField(max_length=11, blank=True)
    date_registered = models.DateTimeField(default=timezone.now)

    #staff vitals
    staff_blood_group_and_genotype = models.CharField(max_length=11, blank=True)
    staff_pulse_rate = models.CharField(max_length=30, blank=True)
    staff_blood_pressure = models.CharField(max_length=30, blank=True)
    staff_respiratory_rate = models.CharField(max_length=30, blank=True)
    staff_temperature = models.CharField(max_length=30, blank=True)
    staff_weight = models.CharField(max_length=30, blank=True)

    def __unicode__(self):
        return str(self.staff_identification_number)

    # def create_staff(sender, instance, created, **kwargs):
    #     if created:
    #         Staff.objects.create(user=instance)

    #     post_save.connect(create_staff, sender=User)

    # def __unicode__(self):
    # 	return str(self.user.email)


class LoggedUser(models.Model):
    user = models.OneToOneField(User, primary_key=True)

    def __unicode__(self):
        return str(self.user.last_name)

    def login_user(sender, request, user, **kwargs):
        LoggedUser(user=user).save()

    def logout_user(sender, request, user, **kwargs):
        try:
            u = LoggedUser.objects.get(user=user)
            u.delete()
        except LoggedUser.DoesNotExist:
            pass

    user_logged_in.connect(login_user)
    user_logged_out.connect(logout_user)