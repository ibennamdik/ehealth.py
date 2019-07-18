from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django import template
from django.template.loader import get_template
from django.template import Context, Template
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
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

from frontdesk.forms import *
from patient.forms import *


# home View
def home(request):
	return render(request, "laboratory/laboratory_home.html", {})