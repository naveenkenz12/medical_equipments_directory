from django.shortcuts import render

from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse

from django.http import JsonResponse

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf

from django.contrib import messages
from django.template import RequestContext

from medical_equipments.forms import equipmentform
from django.contrib.auth.forms import UserCreationForm
from medical_equipments.forms import userregisterform
from medical_equipments.models import equipment
from django.contrib.auth.models import User
#from medical_equipments.models import userregister

from django.core.exceptions import PermissionDenied

from django.utils.translation import ugettext
# from countries_states.forms import CountryStateForm, states_for_country

import os
import sys
import subprocess
import csv

from django.core.mail import send_mail
from django.core.mail import BadHeaderError

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

from medical_equipments.forms import request_for_state_admin_form
from medical_equipments.forms import request_for_district_admin_form

from medical_equipments.models import request_for_state_admin
from medical_equipments.models import request_for_district_admin

from medical_equipments.forms import state_adminform
from medical_equipments.models import state_admin

from medical_equipments.forms import district_adminform
from medical_equipments.models import district_admin

from medical_equipments.forms import hospitalform
from medical_equipments.models import hospital


# from rest_framework.renderers import JSONRenderer
# from rest_framework.response import Response
# from rest_framework.views import APIView

# Create your views here.


from django.views.decorators.csrf import csrf_exempt



import os
import random
import string
from random import randint


def _generate_password_():

	length = 8 + randint(0,4)
	chars = string.ascii_letters + string.digits + '!@#$*'
	random.seed = (os.urandom(1024))

	return  ''.join(random.choice(chars) for i in range(length))



def edit_fav(request):
	print(request)
	if request.method  == "POST":
		if request.is_ajax():
			print("data")
			email = request.POST.get('email')
			mobile = request.POST.get('mobile')
			con = request.POST.get('con')
			data = {"email":email, "mobile":mobile , "con":con }
			print(email)
			print(mobile)
			print(con)
		print("post")
	else:
		search = "none"
	return


# def home(request):
# 	if not request.user.is_superuser:
# 		raise PermissionDenied
# 	if request.method == 'POST':
# 		#print("anmol")
# 		if request.is_ajax():
# 			email = request.POST.get('email')
# 			mobile = request.POST.get('mobile')
# 			con = request.POST.get('con')
# 			data = {"email":email, "mobile":mobile , "con":con }
# 			print(email)
# 			print(mobile)
# 			print(con)
# 			try:
# 				queryset = request_for_state_admin.objects.get(email = email)
# 				print("yes")
# 			except:
# 				queryset = None
# 				print("no")


# 			print(queryset.email)
# 			print(queryset.first_name)
# 			print(queryset.middle_name)
# 			print(queryset.last_name)
# 			print(queryset.mobile)
# 			print(queryset.state)

# 			passwd = _generate_password_()
# 			print(passwd)

# 			message = 'username: '+queryset.email+' password: '+passwd
# 			to_list = [ 'naveenkenz12@gmail.com',queryset.email]
# 			send_mail('login credentials',message,settings.EMAIL_HOST_USER,to_list, fail_silently=False)

# 			user = User.objects.create_user(username=queryset.email ,email=queryset.email ,password=passwd , first_name=queryset.first_name,last_name=queryset.last_name, is_staff = True)

# 			input_data = state_admin()
# 			input_data.email = queryset.email
# 			input_data.mobile = queryset.mobile
# 			input_data.first_name = queryset.first_name
# 			input_data.middle_name = queryset.middle_name
# 			input_data.last_name = queryset.last_name
# 			input_data.state = queryset.state
# 			input_data.save()

# 			queryset.delete()

# 			return JsonResponse(data)

# 	return HttpResponseRedirect('/admin/medical_equipments/request_for_state_admin/')

# # def home2(request):
# # 	return render(request,'invalid_request.html')


# def reject(request):
# 	if not request.user.is_superuser:
# 		raise PermissionDenied
# 	if request.method == 'POST':
# 		#print("anmol")
# 		if request.is_ajax():
# 			email = request.POST.get('email')
# 			mobile = request.POST.get('mobile')
# 			data = {"email":email, "mobile":mobile }
# 			print(email)
# 			print(mobile)

# 			try:
# 				queryset = request_for_state_admin.objects.get(email = email)
# 				print("yes")
# 			except:
# 				queryset = None
# 				print("no")


# 			print(queryset.email)
# 			print(queryset.first_name)
# 			print(queryset.middle_name)
# 			print(queryset.last_name)
# 			print(queryset.mobile)
# 			print(queryset.state)


# 			message = 'your request has been rejected'
# 			to_list = [ 'naveenkenz12@gmail.com',queryset.email]
# 			send_mail('login credentials',message,settings.EMAIL_HOST_USER,to_list, fail_silently=False)

# 			queryset.delete()

# 			return JsonResponse(data)

# 	return HttpResponseRedirect('/admin/medical_equipments/request_for_state_admin/')

def state_admin_register_form(request):
	if request.method == 'POST':
		admin_register_form = request_for_state_admin_form(request.POST, request.FILES)
		print("naveen")
		
		if admin_register_form.is_valid():
			admin_register_form.save()
			
			return HttpResponseRedirect("/request_sent")

		else:
			print(admin_register_form.errors)
			messages.error(request, 'A request with this Email ID already exists')
			return HttpResponseRedirect("/state_admin_register_form")

	args = {}
	args.update(csrf(request))

	args['admin_register_form'] = request_for_state_admin_form()

	return render_to_response('state_admin_registration.html',args, context_instance = RequestContext(request))


def district_admin_register_form(request):
	if request.method == 'POST':
		dis_admin_register_form = request_for_district_admin_form(request.POST, request.FILES)
		print("naveen")
		
		if dis_admin_register_form.is_valid():
			dis_admin_register_form.save()
			
			return HttpResponseRedirect("/request_sent")

		else:
			print(dis_admin_register_form.errors)
			messages.error(request, 'A request with this Email ID already exists')
			return HttpResponseRedirect("/district_admin_register_form")

	args = {}
	args.update(csrf(request))

	args['dis_admin_register_form'] = request_for_district_admin_form()

	return render_to_response('district_admin_registration.html',args, context_instance = RequestContext(request))



def make_state_admin(request):
	if request.method == 'POST':
		make_state_admin_form = state_adminform(request.POST, request.FILES)

		if make_state_admin_form.is_valid():
			make_state_admin_form.save()
			#to_list = [ 'naveenkenz12@gmail.com']
			#send_mail('subject','message',settings.EMAIL_HOST_USER,to_list, fail_silently=False)
			return HttpResponseRedirect("/state_requests")
			

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

def district_requests(request):
	if request.user.is_superuser:
		return HttpResponseRedirect('/admin')
	if not request.user.is_staff:
		raise HttpResponseRedirect('/login')
	try:
		queryset = state_admin.objects.get(email = request.user.username)
	except:
		queryset = None
		raise PermissionDenied

	state = queryset.state
	print(state)
	try:
		queryset = request_for_district_admin.objects.filter(state = state)
		print("yes")
	except:
		queryset = None



	context = {
		'queryset' :queryset
		}

	return render(request, 'district_requests.html', context)

def district_approve(request):
	if request.user.is_superuser:
		raise PermissionDenied
	if not request.user.is_staff:
		raise PermissionDenied
	if request.user.is_staff:
		email = request.GET['email']
		print(email)
	try:
		q = state_admin.objects.get(email =request.user.username)
	except:
		q = None
		raise PermissionDenied

	try:
		print("yes")
		queryset = request_for_district_admin.objects.get(email = email)
	except:
		queryset = None

	print(q.state)
	print(queryset.state)
	if q.state != queryset.state:
		raise PermissionDenied

	passwd = _generate_password_()
	print(passwd)

	message = 'username: '+queryset.email+' password: '+passwd
	to_list = [ 'naveenkenz12@gmail.com',queryset.email]
	send_mail('login credentials',message,settings.EMAIL_HOST_USER,to_list, fail_silently=False)

	user = User.objects.create_user(username=queryset.email ,email=queryset.email ,password=passwd , first_name=queryset.first_name,last_name=queryset.last_name, is_staff = False)

	input_data = district_admin()
	input_data.email = queryset.email
	input_data.mobile = queryset.mobile
	input_data.first_name = queryset.first_name
	input_data.middle_name = queryset.middle_name
	input_data.last_name = queryset.last_name
	input_data.state = queryset.state
	input_data.district = queryset.district
	input_data.save()

	queryset.delete()

	return HttpResponseRedirect('/district_requests/')

def state_approve(request):
	if not request.user.is_superuser:
		raise PermissionDenied
	
	if request.user.is_superuser:
		email = request.GET['email']
		print(email)
	
	try:
		print("yes")
		queryset = request_for_state_admin.objects.get(email = email)
	except:
		queryset = None


	print(queryset.state)

	passwd = _generate_password_()
	print(passwd)

	message = 'username: '+queryset.email+' password: '+passwd
	to_list = [ 'naveenkenz12@gmail.com',queryset.email]
	send_mail('login credentials',message,settings.EMAIL_HOST_USER,to_list, fail_silently=False)

	user = User.objects.create_user(username=queryset.email ,email=queryset.email ,password=passwd , first_name=queryset.first_name,last_name=queryset.last_name, is_staff = True)

	input_data = state_admin()
	input_data.email = queryset.email
	input_data.mobile = queryset.mobile
	input_data.first_name = queryset.first_name
	input_data.middle_name = queryset.middle_name
	input_data.last_name = queryset.last_name
	input_data.state = queryset.state
	input_data.save()

	queryset.delete()

	return HttpResponseRedirect('/state_requests/')

def district_reject(request):
	if request.user.is_superuser:
		raise PermissionDenied
	if not request.user.is_staff:
		raise PermissionDenied
	if request.user.is_staff:
		email = request.GET['email']
		print(email)
	try:
		q = state_admin.objects.get(email =request.user.username)
	except:
		q = None
		raise PermissionDenied

	try:
		print("yes")
		queryset = request_for_district_admin.objects.get(email = email)
	except:
		queryset = None

	print(q.state)
	print(queryset.state)
	if q.state != queryset.state:
		raise PermissionDenied

	message = 'The request of '+queryset.email+' is rejected'
	to_list = [ 'naveenkenz12@gmail.com',queryset.email]
	send_mail('login credentials',message,settings.EMAIL_HOST_USER,to_list, fail_silently=False)

	queryset.delete()

	return HttpResponseRedirect('/district_requests/')


def state_reject(request):
	if not request.user.is_superuser:
		raise PermissionDenied
	if request.user.is_superuser:
		email = request.GET['email']
		print(email)
	try:
		print("yes")
		queryset = request_for_district_admin.objects.get(email = email)
	except:
		queryset = None

	print(queryset.state)
	
	message = 'The request of '+queryset.email+' is rejected'
	to_list = [ 'naveenkenz12@gmail.com',queryset.email]
	send_mail('login credentials',message,settings.EMAIL_HOST_USER,to_list, fail_silently=False)

	queryset.delete()

	return HttpResponseRedirect('/state_requests/')

def district_remove(request):
	if request.user.is_superuser:
		raise PermissionDenied
	if not request.user.is_staff:
		raise PermissionDenied
	if request.user.is_staff:
		email = request.GET['email']
		print(email)
	try:
		q = state_admin.objects.get(email =request.user.username)
	except:
		q = None
		raise PermissionDenied

	try:
		print("yes")
		queryset = district_admin.objects.get(email = email)
	except:
		queryset = None

	print(q.state)
	print(queryset.state)
	if q.state != queryset.state:
		raise PermissionDenied

	try:
		q = User.objects.get(username = email)
	except:
		q = None

	message = 'The district admin '+queryset.email+' is removed'
	to_list = [ 'naveenkenz12@gmail.com',queryset.email]
	send_mail('login credentials',message,settings.EMAIL_HOST_USER,to_list, fail_silently=False)

	queryset.delete()
	q.delete()

	return HttpResponseRedirect('/district_admin/')

def state_remove(request):
	if not request.user.is_superuser:
		raise PermissionDenied
	if request.user.is_superuser:
		email = request.GET['email']
		print(email)

	try:
		print("yes")
		queryset = state_admin.objects.get(email = email)
	except:
		queryset = None

	
	print(queryset.state)
	
	try:
		q = User.objects.get(username = email)
	except:
		q = None

	message = 'The state admin '+queryset.email+' is removed'
	to_list = [ 'naveenkenz12@gmail.com',queryset.email]
	send_mail('login credentials',message,settings.EMAIL_HOST_USER,to_list, fail_silently=False)

	queryset.delete()
	q.delete()

	return HttpResponseRedirect('/state_admin/')

def show_state_admin(request):
	if not request.user.is_superuser:
		raise PermissionDenied
	try:
		print("yes")
		queryset = state_admin.objects.all()
		print("yes")
	except:
		print("NO")
		queryset = None
	context = {
		'queryset' :queryset
	}
	return render(request, 'state_admin.html', context)



def show_district_admin(request):
	if request.user.is_superuser:
		raise PermissionDenied
	if not request.user.is_staff:
		raise PermissionDenied

	try:
		q = state_admin.objects.get(email = request.user.username)
	except:
		q = None
		raise PermissionDenied

	try:
		queryset = district_admin.objects.filter(state = q.state)
	except:
		queryset = None

	context = {
	'queryset' :queryset
	}
	return render(request, 'district_admin.html', context)


def medical_equipments_form(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/login')
	if request.user.is_superuser:
		return HttpResponseRedirect('/admin')
	if request.user.is_staff:
		return HttpResponseRedirect('/district_requests')

	hid = request.GET['hid']
	print(hid)

	try:
		q = hospital.objects.get(hospital_id = hid)
	except:
		q = None

	if request.method == 'POST':
		equipment_form = equipmentform(request.POST)
		if equipment_form.is_valid():
			equipment_form.save()
			return HttpResponseRedirect('/current_hospital')
		else:
			messages.error(request, equipment_form.errors)
			print(equipment_form.errors)
			return HttpResponseRedirect('/medical_equipments_form')

	args = {}
	args.update(csrf(request))

	args['equipment_form'] = equipmentform(initial = {'hospital_id':q.hospital_id, 'hospital_name':q.hospital_name, 'state':q.state , 'district':q.district , 'signed':request.user.username })

	return render_to_response('medical_equipments_form.html' , args, context_instance = RequestContext(request))

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
	if request.user.is_staff:
		try:
			queryset =state_admin.objects.get(email = request.user.username)
		except:
			queryset = None
	
		if request.method == 'POST':
			form = state_adminform(request.POST, instance = queryset)
			print(queryset)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/user')
			else:
				print(form.errors)
		else:
			try:
				form = state_adminform(initial = {'email':queryset.email ,'state':queryset.state,  'email2':queryset.email2, 'first_name':queryset.first_name, 'middle_name':queryset.middle_name, 'last_name':queryset.last_name, 'mobile':queryset.mobile, 'mobile2':queryset.mobile2, 'address':queryset.address, 'file':queryset.file })

			except:
				form = state_adminform(initial = {'email':request.user.username })
		context = {
		'state_adminform' :form,
		'queryset' :queryset
		}
	
		return render(request, 'user.html', context)

	if not request.user.is_staff:
		try:
			queryset =district_admin.objects.get(email = request.user.username)
		except:
			queryset = None
	
		if request.method == 'POST':
			form = district_adminform(request.POST, instance = queryset)
			print(queryset)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/user')
			else:
				print(form.errors)
		else:
			try:
				form = district_adminform(initial = {'email':queryset.email ,'state':queryset.state, 'district':queryset.district,  'email2':queryset.email2, 'first_name':queryset.first_name, 'middle_name':queryset.middle_name, 'last_name':queryset.last_name, 'mobile':queryset.mobile, 'mobile2':queryset.mobile2, 'address':queryset.address, 'file':queryset.file })

			except:
				form = district_adminform(initial = {'email':request.user.username })
		context = {
		'district_adminform' :form,
		'queryset' :queryset
		}
	
		return render(request, 'user.html', context)
	
def register_hospital(request):
	if not request.user.is_authenticated():
		raise PermissionDenied
	if request.user.is_superuser:
		raise PermissionDenied
	if request.user.is_staff:
		raise PermissionDenied

	try:
		q = district_admin.objects.get(email = request.user.username)
	except:
		q = None
		raise PermissionDenied

	if request.method == 'POST':
		hospital_form = hospitalform(request.POST)
		if hospital_form.is_valid():
			hospital_form.save()
			return HttpResponseRedirect('/login')
		else:
			messages.error(request, hospital_form.errors)
			print(hospital_form.errors)
			return HttpResponseRedirect('/register_hospital')

	# else:
	# 	try:
	# 		hospital_form = hospitalform(initial = {'state':q.state , 'district':q.district })
	# 	except:
	# 		hospital_form = hospitalform()

	args = {}
	args.update(csrf(request))

	args['hospital_form'] = hospitalform(initial = {'state':q.state , 'district':q.district })

	return render_to_response('hospital_registration.html' , args, context_instance = RequestContext(request))

def current_hospital(request):
	if not request.user.is_authenticated():
		raise PermissionDenied

	if request.user.is_superuser:
		raise PermissionDenied

	if request.user.is_staff:
		raise PermissionDenied

	try:
		q = district_admin.objects.get(email = request.user.username)
	except:
		q = None
		raise PermissionDenied

	try:
		queryset = hospital.objects.filter(district = q.district)
	except:
		queryset = None

	context = {
	'queryset' :queryset
	}
	return render(request, 'current_hospital.html', context)

# def countries_states_view(request):
#     """
#     A simple view that processes the CountriesStatesForm.
#     """
#     if request.method == 'POST':
#         form = CountryStateForm(request.POST)
#         if form.is_valid():
#             message = 'You selected %s' % form.cleaned_data['country']
#             if form.cleaned_data['state']:
#                 message += 'and %s' % form.cleaned_data['state']
#             return HttpResponse(message)
#     else:
#         form = CountryStateForm()

#     return render(request, 'base.html', {
#             'form': form
#         })

# def ajax_populate_states(request):
#     """
#     Populates the states dropdown with the appropriate states.
#     """
#     formdata = request.REQUEST.copy()

#     if 'country' in formdata:
#         country_field = 'country'
#     else:
#         return HttpResponseServerError()

#     form = CountryStateForm(data=formdata)
#     country_data = formdata.get(country_field)

#     try:
#         country_obj = form.fields[country_field].clean(country_data)
#     except:
#         raise HttpResponseServerError()

#     states = states_for_country(country_obj, ugettext)

#     return render(request, 'state_choices.html', {
#         'states': states    
#     })

    
