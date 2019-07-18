from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django import template
from django.template.loader import get_template
from django.template import Context, Template
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import logout, authenticate, login
from django.template import RequestContext
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.db.models import Q

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

from .forms import *

def main_page(request):
    return render(request, 'home.html', {})
    
def profile_page(request):
    #user = User.objects.get(username=request.user)
    profile = get_object_or_404(Staff, user=request.user)

    context = {
    "profile" : profile,

    }
    return render(request, 'registration/profile.html', context)

def login_page(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        return render(request, 'base.html', {})
    else:
        # Return an 'invalid login' error message.
        return render(request, 'login.html', {})


def logout_page(request):
    logout(request)
    return render(request, 'login.html', {})

def register_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],password=form.cleaned_data['password1'],email=form.cleaned_data['email'])
            
            return render(request, 'main_page.html',{})
    form = RegistrationForm()
    context = {
    "form" : form,
    }
    return render (request, 'registration/register.html', context)


def staff_update(request, search_id):
    staff = get_object_or_404(Staff, staff_identification_number=search_id)
    form = StaffUpdateForm(request.POST or None, instance=staff)
    if form.is_valid():
        
        message = 'Staff successfully updated'
        form.save()
        return redirect('/')
    else:
        message = 'Staff update Failed!'

    context = {
        'form':form,
        'message': message
    }
    return render(request, 'patient/patient_update_form.html', context)

def profile_page(request):
    #user = User.objects.get(username=request.user)
    profile = get_object_or_404(Staff, user=request.user)

    context = {
    "profile" : profile,

    }
    return render(request, 'registration/profile.html', context)

def staff_profile(request):
    staff = get_object_or_404(Staff, user=request.user)

    context = {
    "staff" : staff,

    }
    return render(request, 'registration/staff_profile.html', context)

#def staff_profile(request, search_id):


    #staff = Staff.objects.all()
    #user = User.objects.all()
    #staff = get_object_or_404(Staff, user=search_id)
    #staff = Staff.objects.values("user")
    # search_id = (
    #     Q(user=search_id) 
    #     #Q(authors__last_name__icontains=query)
    # )
    # #staff = Staff.objects.get(search_id)
    #staff = User.objects.get(username=search_id)
    #print staff.username

    #context = {
    #"staff" : staff,

    #}
    #return render(request, 'registration/staff_profile.html', context)