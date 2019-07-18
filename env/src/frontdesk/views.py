from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings

from django import template
from django.template.loader import get_template
from django.template import Context, Template
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.models import User, Group

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

# Create your views here.

# home View
def home(request):
	if not request.user.is_authenticated():
		return redirect('login')

	user = User.objects.get(username=request.user)
	profile = Staff.objects.get(user=request.user)
	logged_users = LoggedUser.objects.all().order_by('user')
	admission = Admission.objects.get()
        
	
	context = {
	"user" : user,
    "profile" : profile,
    "logged_users":logged_users,
    "admission" : admission
	}
	return render(request, "frontdesk/frontdesk_home.html", context)