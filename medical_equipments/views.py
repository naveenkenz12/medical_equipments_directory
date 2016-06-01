from django.shortcuts import render

from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf

from django.contrib import messages
from django.template import RequestContext

from medical_equipments.forms import userpostform
from django.contrib.auth.forms import UserCreationForm
from medical_equipments.forms import userregisterform
from medical_equipments.models import userpost
#from medical_equipments.models import userregister

from django.core.exceptions import PermissionDenied

import os
import sys
import subprocess
import csv

from django.core.mail import send_mail
from django.core.mail import BadHeaderError

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

from medical_equipments.forms import request_for_state_admin_form
from medical_equipments.models import request_for_state_admin

# from rest_framework.renderers import JSONRenderer
# from rest_framework.response import Response
# from rest_framework.views import APIView

# Create your views here.


from django.views.decorators.csrf import csrf_exempt



import os
import random
import string
from random import randint


@csrf_exempt
def edit_fav(request):
	print(request)
	if request.method  == "POST":
		print("post")
	else:
		search = "none"
	return


def _generate_password_(request):

	length = 8 + randint(0,4)
	chars = string.ascii_letters + string.digits + '!@#$*'
	random.seed = (os.urandom(1024))

	return  ''.join(random.choice(chars) for i in range(length))


def state_admin_register_form(request):
	if request.method == 'POST':
		admin_register_form = request_for_state_admin_form(request.POST, request.FILES)
		print("naveen")
		
		if admin_register_form.is_valid():
			admin_register_form.save()
			#to_list = [ 'naveenkenz12@gmail.com']
			#send_mail('subject','message',settings.EMAIL_HOST_USER,to_list, fail_silently=False)
			return HttpResponseRedirect("/request_sent")

		else:
			print(admin_register_form.errors)
			messages.error(request, 'A request with this Email ID already exists')
			return HttpResponseRedirect("/state_admin_register_form")

	args = {}
	args.update(csrf(request))

	args['admin_register_form'] = request_for_state_admin_form()

	return render_to_response('state_admin_registration.html',args, context_instance = RequestContext(request))

def approve(request):
	if not request.user.is_superuser:
		raise PermissionDenied




# def make_state_admin(request):
# 	if request.method == 'POST':
# 		make_state_admin_form = state_adminform(request.POST, request.FILES)

# 		if make_state_admin_form.is_valid():
# 			make_state_admin_form.save()
# 			#to_list = [ 'naveenkenz12@gmail.com']
# 			#send_mail('subject','message',settings.EMAIL_HOST_USER,to_list, fail_silently=False)
# 			return HttpResponseRedirect("/state_requests")
			

def request_sent(request):
	args = {}
	return render_to_response('request_sent.html', args)

def invalid_request(request):
	args = {}
	return render_to_response('invalid_request.html', args)

def state_requests(request):
	if not request.user.is_superuser:
		print("nav")
		raise PermissionDenied
	else:
		try:
			queryset = request_for_state_admin.objects.all()
		except:
			queryset = None
			print("none")
		context = {
			'queryset' :queryset
			}
		return render(request, 'state_request.html', context)

def medical_equipments_form(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/login')
	try:
		queryset =userpost.objects.get(user_name = request.user.username)
	except:
		queryset = None

	if request.method == 'POST':
		form = userpostform(request.POST, instance = queryset)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/user')
		else:
			print(form.errors)
	else:
		try:
			form = userpostform(initial = {'user_name':queryset.user_name })
		except:
			form = userpostform(initial = {'user_name':request.user.username })
	context = {
	'medical_equipments_form' :form,
	'queryset' :queryset
	}
	
	return render(request, 'medical_equipments_form.html', context)
	#return render(request, 'user.html', context)

def login(request):
	if not request.user.is_authenticated():
		log = {}
		log.update(csrf(request))
		return render_to_response('medical_equipments_form.html', log, context_instance = RequestContext(request))
	else:
		return HttpResponseRedirect('/medical_equipments_form')

def logout(request):
	auth.logout(request)
	render_to_response('medical_equipments_form.html', {})
	return HttpResponseRedirect('/login')

def authorized_view(request):
	username = request.POST.get('username','')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password =password )

	if user is not None:
		auth.login(request,user)
		return HttpResponseRedirect('/medical_equipments_form')
	else:
		messages.error(request, 'username or password is not valid')
		return HttpResponseRedirect('/login')

def register(request):
	if request.method == 'POST':
		form = userregisterform(request.POST)
		if form.is_valid():
			new_user = form.save()
			return HttpResponseRedirect("/medical_equipments_form")
		else:
			messages.error(request, form.errors)
			print(form.errors)
			return HttpResponseRedirect('/register/')

	print("apple")
	args = {}
	args.update(csrf(request))

	args['form'] = userregisterform()

	
	return render_to_response('registration.html',args, context_instance = RequestContext(request))


def user(request):
	try:
		queryset =userpost.objects.get(user_name = request.user.username)
	except:
		queryset = None
	context = {
    	'queryset' :queryset
    }
	return render(request, 'user.html', context)
