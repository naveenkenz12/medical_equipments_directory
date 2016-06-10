from django.shortcuts import render

from django.db.models import Min,Max,Avg,Count

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
from medical_equipments.forms import equipment_update_form
from medical_equipments.forms import equipment_viewonly_form

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
from medical_equipments.forms import request_for_country_admin_form

from medical_equipments.models import request_for_state_admin
from medical_equipments.models import request_for_district_admin
from medical_equipments.models import request_for_country_admin

from medical_equipments.forms import hospitalviewform

from medical_equipments.forms import state_adminform
from medical_equipments.models import state_admin

from medical_equipments.forms import district_adminform
from medical_equipments.models import district_admin

from medical_equipments.forms import country_adminform
from medical_equipments.models import country_admin

from medical_equipments.forms import hospitalform
from medical_equipments.forms import hospital_viewonly_form
from medical_equipments.forms import hospital_update_form

from medical_equipments.models import hospital

from medical_equipments.forms import change_passwordform
from medical_equipments.forms import forgot_passwordform

from medical_equipments.forms import equipment_searchform

#from medical_equipments.models import change_password


# from rest_framework.renderers import JSONRenderer
# from rest_framework.response import Response
# from rest_framework.views import APIView

# Create your views here.


from django.views.decorators.csrf import csrf_exempt

from difflib import SequenceMatcher

#from chartit import DataPool, Chart

import os
import random
import string
import datetime
import time
from random import randint



def similar(a,b):
	return SequenceMatcher(None,a,b).ratio()


def index(request):
	args = {}
	args.update(csrf(request))

	return render_to_response('index.html', args, context_instance = RequestContext(request))

def valid_hospital_registration(request):
	hid = request.GET['hid']
	if request.user.is_superuser:
		raise PermissionDenied
	elif request.user.is_staff:
		raise PermissionDenied
	else:
		try:
			queryset = hospital.objects.get(hospital_id = hid)
		except:
			queryset = None
			raise PermissionDenied

		try:
			q = district_admin.objects.get(email = request.user.username)
		except:
			q = None

		try:
			q2 = country_admin.objects.get(email = request.user.username)
		except:
			q2 = None

		if q is None and q2 is None:
			raise PermissionDenied

		context = {
				'queryset' :queryset
				}

		return render(request, 'valid_hospital_registration.html', context)

def valid_equipment_registration(request):
	hid = request.GET['hid']
	eid = request.GET['eid']
	if request.user.is_superuser:
		raise PermissionDenied
	elif request.user.is_staff:
		raise PermissionDenied
	else:
		try:
			queryset = equipment.objects.get(hospital_id = hid, equipment_id=eid)
		except:
			queryset = None
			raise PermissionDenied

		try:
			q = district_admin.objects.get(email = request.user.username)
		except:
			q = None

		try:
			q2 = country_admin.objects.get(email = request.user.username)
		except:
			q2 = None

		if q is None and q2 is None:
			raise PermissionDenied

		context = {
				'queryset' :queryset
				}

		return render(request, 'valid_equipment_registration.html', context)

def change_password(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/login')
	if request.method == 'POST':
		change_password_form = change_passwordform(request.POST)
		print("naveen")
		
		c = request.POST['old_password']
		p1 = request.POST['new_password1']
		p2 = request.POST['new_password2']
		u = (request.user.username).split('@')[0]
		print(p1)
		print(p2)

		user = auth.authenticate(username=request.user.username, password =c )
		if user is None:
			messages.error(request, 'Current Password is Not Correct' )
			return HttpResponseRedirect("/change_password")

		elif p1 != p2:
			messages.error(request, 'Both Password Does Not Match' )
			return HttpResponseRedirect("/change_password")	

		elif similar(c,p1)>0.8:
			messages.error(request, 'New Password Too Similar To Old Password' )
			return HttpResponseRedirect("/change_password")

		elif len(p1)<8:
			messages.error(request, 'New Password is Too Short' )
			return HttpResponseRedirect("/change_password")

		elif similar(p1,request.user.username)>=0.8 or similar(p1,u)>=0.75:
			messages.error(request, 'Password Too Similar to Username' )
			return HttpResponseRedirect("/change_password")

		elif change_password_form.is_valid():
			user = User.objects.get(username = request.user.username)
			print(user.username)
			user.set_password(p1)
			user.save()
			print("naveen")
			return HttpResponseRedirect("/logout")

		else:
			print(change_password_form.errors)
			messages.error(request, change_password_form.errors )
			return HttpResponseRedirect("/change_paasword")

	args = {}
	args.update(csrf(request))

	args['change_password_form'] = change_passwordform()

	return render_to_response('change_password.html',args, context_instance = RequestContext(request))


def equipment_query(request):
	if request.method == 'POST':
		equipment_search_form = equipment_searchform(request.POST)
		
		if equipment_search_form.is_valid():
			print("naveen")

			try:
				hid = request.POST['hospital_id']
			except:
				hid = ""

			try:
				eid = request.POST['equipment_id']
			except:
				eid = ""

			try:
				hname = request.POST['hospital_name']
			except:
				hname = ""

			try:
				ename = request.POST['equipment_name']
			except:
				ename = ""

			try:
				emodel = request.POST['equipment_model']
			except:
				emodel = ""

			try:
				man = request.POST['manufacturar']
			except:
				man = ""

			country = request.POST['country']
			state = request.POST['state']
			district = request.POST['district']

			cat = request.POST['equipment_category']
			war = request.POST['equipment_in_warranty']
			amc = request.POST['equipment_under_AMC_CMC']
			sta = request.POST['working_condition']

			if hid != "" and eid != "":
				queryset = equipment.objects.filter(hospital_id = hid, equipment_id = eid)
				print("a")

			elif hid != "":
				queryset = equipment.objects.filter(hospital_id = hid)
				print("b")

				if hname != "":
					queryset = queryset.filter(hospital_name = hname)

				if ename != "":
					queryset = queryset.filter(equipment_name = ename)

				if emodel != "":
					queryset = queryset.filter(equipment_model = model)

				if country != "All":
					queryset = queryset.filter(country = country)

				if state != "All":
					queryset = queryset.filter(state = state)

				if district != "All":
					queryset = queryset.filter(district = district)

			elif eid != "":
				print("c")
				queryset = equipment.objects.filter(equipment_id = eid)
				if hname != "":
					queryset = queryset.filter(hospital_name = hname)

				if ename != "":
					queryset = queryset.filter(equipment_name = ename)

				if country != "All":
					queryset = queryset.filter(country = country)

				if state != "All":
					queryset = queryset.filter(state = state)

				if district != "All":
					queryset = queryset.filter(district = district)

			else:
				print("d")
				queryset = equipment.objects.all()
				print(queryset)
				if hname != "":
					queryset = queryset.filter(hospital_name = hname)
					

				if ename != "":
					queryset = queryset.filter(equipment_name = ename)
					

				if country != "All":
					queryset = queryset.filter(country = country)
					

				if state != "All":
					queryset = queryset.filter(state = state)
					

				if district != "All":
					queryset = queryset.filter(district = district)
					

			if man != "":
				queryset = queryset.filter(manufacturar = man)

			if cat != "All Category":
				queryset = queryset.filter(equipment_category = cat)

			if war != "All":
				queryset = queryset.filter(equipment_in_warranty = war)		

			if amc != "All":
				queryset = queryset.filter(equipment_under_AMC_CMC= amc)	

			if sta != "All":
				queryset = queryset.filter(working_condition = sta)

			context = {
			'queryset' :queryset
			}
			
			print(queryset)

			return render(request, 'equipment_search_result.html', context)
		else:
			messages.error(request, equipment_search_form.errors )
			return HttpResponseRedirect("/equipment_query")


	args = {}
	args.update(csrf(request))

	args['equipment_search_form'] = equipment_searchform()

	return render_to_response('equipment_search.html',args, context_instance = RequestContext(request))

def forgot_password(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/login')
	if request.method == 'POST':
		forgot_password_form = forgot_passwordform(request.POST)
		print("naveen")
		
		email = request.POST['email']
		mobile = request.POST['mobile']
		print(email)

		try:
			user = User.objects.get(username = email)
		except:
			user = None

		
		if user is None:
			messages.error(request, 'Email ID/Username is Incorrect' )
			return HttpResponseRedirect("/forgot_password")

		elif change_password_form.is_valid():
			passwd = _generate_password_()
			print(passwd)
			
			message = 'New Password is :' + passwd
			to_list = [ 'naveenkenz12@gmail.com',email]
			send_mail('login credentials',message,settings.EMAIL_HOST_USER,to_list, fail_silently=False)
			
			user = User.objects.get(username = email)
			print(user.username)
			user.set_password(passwd)
			user.save()
			
			print("naveen")
			return HttpResponseRedirect("/login")

		else:
			print(forgot_password_form.errors)
			messages.error(request, forgot_password_form.errors )
			return HttpResponseRedirect("/forgot_paasword")

	args = {}
	args.update(csrf(request))

	args['forgot_password_form'] = forgot_passwordform()

	return render_to_response('forgot_password.html',args, context_instance = RequestContext(request))


def _generate_password_():

	length = 8 + randint(0,4)
	chars = string.ascii_letters + string.digits + '!@#$*'
	random.seed = (os.urandom(1024))

	return  ''.join(random.choice(chars) for i in range(length))

def _generate_hospital_id_(state):
	if state == "Andaman and Nicobar Islands":
		st_code = "AN"
	elif state == "Andhra Pradesh":
		st_code = "AP"
	elif state == "Arunachal Pradesh":
		st_code = "AR"
	elif state == "Assam":
		st_code = "AS"
	elif state == "Bihar":
		st_code = "BR"
	elif state == "Chandigarh":
		st_code = "CN"
	elif state == "Chattisgarh":
		st_code = "CT"
	elif state == "Dadra and Nagar Haveli":
		st_code = "DN"
	elif state == "Daman and Diu":
		st_code = "DD"
	elif state == "Delhi":
		st_code = "DL"
	elif state == "Goa":
		st_code = "GA"
	elif state == "Gujrat":
		st_code = "GJ"
	elif state == "Haryana":
		st_code = "HR"
	elif state == "Himachal Pradesh":
		st_code = "HP"
	elif state == "Jammu and Kashmir":
		st_code = "JK"
	elif state == "Jharkhand":
		st_code = "JH"
	elif state == "Karnataka":
		st_code = "KA"
	elif state == "Kerala":
		st_code = "KL"
	elif state == "Lakshadweep":
		st_code = "LD"
	elif state == "Madhya Pradesh":
		st_code = "MP"
	elif state == "Maharashtra":
		st_code = "MH"
	elif state == "Manipur":
		st_code = "MN"
	elif state == "Meghalaya":
		st_code = "ML"
	elif state == "Mizoram":
		st_code = "MZ"
	elif state == "Nagaland":
		st_code = "NL"
	elif state == "Odisha":
		st_code = "OR"
	elif state == "Puducherry":
		st_code = "PY"
	elif state == "Punjab":
		st_code = "PB"
	elif state == "Rajasthan":
		st_code = "RJ"
	elif state == "Sikkim":
		st_code = "SK"
	elif state == "Tamil Nadu":
		st_code = "TN"
	elif state == "Telangana":
		st_code = "TG"
	elif state == "Tripura":
		st_code = "TR"
	elif state == "Uttar Pradesh":
		st_code = "UP"
	elif state == "Uttarakhand":
		st_code = "UT"
	elif state == "West Bengal":
		st_code = "WB"
	else:
		st_code = "OI"

	length = 7
	chars = string.digits 
	random.seed = (os.urandom(1024))

	code = ''.join(random.choice(chars) for i in range(length))

	return st_code + code + "S"

def _generate_equipment_id_ ():
	length = 4
	chars = string.digits

	random.seed = (os.urandom(1024))

	code = ''.join(random.choice(chars) for i in range(length))

	return "E" + code

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

def viewid(request):
	if request.method == 'POST':
		view_id_form = hospitalviewform(request.POST)

		hospital_id = request.POST['hospital_id']
		print(hospital_id)

		if view_id_form.is_valid():
			return HttpResponseRedirect("/hospital_equipments/?hid="+hospital_id)	

	args = {}
	args.update(csrf(request))

	args['view_id_form'] = hospitalviewform()

	return render_to_response('hospital.html',args, context_instance = RequestContext(request))

# def view_hospital(request):
# 	hospital_id = request.GET['hospital_id']
	
# 	try:
# 		queryset = equipment.objects.filter(hospital_id = hospital_id)
# 	except:
# 		queryset = None
# 	context = {
# 		'queryset' :queryset
# 		}
# 	return render(request, 'hospital_equipment.html', context)


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

def country_admin_register_form(request):
	if request.method == 'POST':
		coun_admin_register_form = request_for_country_admin_form(request.POST, request.FILES)
		print("naveen")
		email = request.POST['email']
		try:
			q = User.objects.get(username = email)
		except:
			q = None

		try:
			queryset = request_for_district_admin.objects.get(email = email)
		except:
			queryset = None

		try:
			queryset2 = request_for_state_admin.objects.get(email = email)
		except:
			queryset2 = None

		if q is not None:
			messages.error(request, 'A user with this Email ID already exists')
			return HttpResponseRedirect("/admin_register_form/country")

		elif queryset is not None:
			messages.error(request, 'A request with this Email ID for district admin already exists')
			return HttpResponseRedirect("/admin_register_form/country")

		elif queryset2 is not None:
			messages.error(request, 'A request with this Email ID for district admin already exists')
			return HttpResponseRedirect("/admin_register_form/country")
		
		elif coun_admin_register_form.is_valid():
			coun_admin_register_form.save()
			
			return HttpResponseRedirect("/request_sent")

		else:
			print(coun_admin_register_form.errors)
			messages.error(request, 'A request with this Email ID already exists')
			return HttpResponseRedirect("/admin_register_form/country")

	args = {}
	args.update(csrf(request))

	args['coun_admin_register_form'] = request_for_country_admin_form()

	return render_to_response('country_admin_registration.html',args, context_instance = RequestContext(request))



def state_admin_register_form(request):
	if request.method == 'POST':
		admin_register_form = request_for_state_admin_form(request.POST, request.FILES)
		print("naveen")
		email = request.POST['email']
		try:
			q = User.objects.get(username = email)
		except:
			q = None

		try:
			queryset = request_for_district_admin.objects.get(email = email)
		except:
			queryset = None

		try:
			queryset2 = request_for_district_admin.objects.get(email = email)
		except:
			queryset2 = None

		if q is not None:
			messages.error(request, 'A user with this Email ID already exists')
			return HttpResponseRedirect("/admin_register_form/state")

		elif queryset is not None:
			messages.error(request, 'A request with this Email ID for district admin already exists')
			return HttpResponseRedirect("/admin_register_form/state")

		elif queryset2 is not None:
			messages.error(request, 'A request with this Email ID for district admin already exists')
			return HttpResponseRedirect("/admin_register_form/state")
		
		elif admin_register_form.is_valid():
			admin_register_form.save()
			
			return HttpResponseRedirect("/request_sent")

		else:
			print(admin_register_form.errors)
			messages.error(request, 'A request with this Email ID already exists')
			return HttpResponseRedirect("/admin_register_form/state")

	args = {}
	args.update(csrf(request))

	args['admin_register_form'] = request_for_state_admin_form()

	return render_to_response('state_admin_registration.html',args, context_instance = RequestContext(request))


def district_admin_register_form(request):
	if request.method == 'POST':
		dis_admin_register_form = request_for_district_admin_form(request.POST, request.FILES)
		print("naveen")
		
		email = request.POST['email']
		try:
			q = User.objects.get(username = email)
		except:
			q = None

		try:
			queryset = request_for_state_admin.objects.get(email = email)
		except:
			queryset = None

		try:
			queryset2 = request_for_state_admin.objects.get(email = email)
		except:
			queryset2 = None

		if q is not None:
			messages.error(request, 'A user with this Email ID already exists')
			return HttpResponseRedirect("/admin_register_form/district")

		elif queryset is not None:
			messages.error(request, 'A request with this Email ID for state admin already exists')
			return HttpResponseRedirect("/admin_register_form/district")

		elif queryset2 is not None:
			messages.error(request, 'A request with this Email ID for state admin already exists')
			return HttpResponseRedirect("/admin_register_form/district")

		elif dis_admin_register_form.is_valid():
			print(request.POST['email'])
			dis_admin_register_form.save()
			
			return HttpResponseRedirect("/request_sent")

		else:
			print(dis_admin_register_form.errors)
			messages.error(request, 'A request with this Email ID already exists')
			return HttpResponseRedirect("/admin_register_form/district")

	args = {}
	args.update(csrf(request))

	args['dis_admin_register_form'] = request_for_district_admin_form()

	return render_to_response('district_admin_registration.html',args, context_instance = RequestContext(request))



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

def country_requests(request):
	if not request.user.is_superuser:
		print("nav")
		raise PermissionDenied
	else:
		try:
			queryset = request_for_country_admin.objects.all()
		except:
			queryset = None
			print("none")
		context = {
			'queryset' :queryset
			}
		return render(request, 'country_request.html', context)

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
		raise PermissionDenied
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
	input_data.country = queryset.country
	input_data.district = queryset.district
	input_data.agex = queryset.agex
	input_data.gender = queryset.gender
	input_data.education = queryset.education
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
	input_data.country = queryset.country
	input_data.agex = queryset.agex
	input_data.gender = queryset.gender
	input_data.education = queryset.education
	input_data.save()

	queryset.delete()

	return HttpResponseRedirect('/state_requests/')

def country_approve(request):
	if not request.user.is_superuser:
		raise PermissionDenied
	
	if request.user.is_superuser:
		email = request.GET['email']
		print(email)
	
	try:
		print("yes")
		queryset = request_for_country_admin.objects.get(email = email)
	except:
		queryset = None


	print(queryset.state)

	passwd = _generate_password_()
	print(passwd)

	message = 'username: '+queryset.email+' password: '+passwd
	to_list = [ 'naveenkenz12@gmail.com',queryset.email]
	send_mail('login credentials',message,settings.EMAIL_HOST_USER,to_list, fail_silently=False)

	user = User.objects.create_user(username=queryset.email ,email=queryset.email ,password=passwd , first_name=queryset.first_name,last_name=queryset.last_name, is_staff = False)

	input_data = country_admin()
	input_data.email = queryset.email
	input_data.mobile = queryset.mobile
	input_data.first_name = queryset.first_name
	input_data.middle_name = queryset.middle_name
	input_data.last_name = queryset.last_name
	input_data.country = queryset.country
	input_data.agex = queryset.agex
	input_data.gender = queryset.gender
	input_data.education = queryset.education
	input_data.save()

	queryset.delete()

	return HttpResponseRedirect('/country_requests/')

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
		queryset = request_for_state_admin.objects.get(email = email)
	except:
		queryset = None

	
	message = 'The request of '+queryset.email+' is rejected'
	to_list = [ 'naveenkenz12@gmail.com',queryset.email]
	send_mail('login credentials',message,settings.EMAIL_HOST_USER,to_list, fail_silently=False)

	queryset.delete()

	return HttpResponseRedirect('/state_requests/')

def country_reject(request):
	if not request.user.is_superuser:
		raise PermissionDenied
	if request.user.is_superuser:
		email = request.GET['email']
		print(email)
	try:
		print("yes")
		queryset = request_for_country_admin.objects.get(email = email)
	except:
		queryset = None

	print(queryset.state)
	
	message = 'The request of '+queryset.email+' is rejected'
	to_list = [ 'naveenkenz12@gmail.com',queryset.email]
	send_mail('login credentials',message,settings.EMAIL_HOST_USER,to_list, fail_silently=False)

	queryset.delete()

	return HttpResponseRedirect('/country_requests/')

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

def country_remove(request):
	if not request.user.is_superuser:
		raise PermissionDenied
	if request.user.is_superuser:
		email = request.GET['email']
		print(email)

	try:
		print("yes")
		queryset = country_admin.objects.get(email = email)
	except:
		queryset = None

	
	
	
	try:
		q = User.objects.get(username = email)
	except:
		q = None

	message = 'The state admin '+queryset.email+' is removed'
	to_list = [ 'naveenkenz12@gmail.com',queryset.email]
	send_mail('login credentials',message,settings.EMAIL_HOST_USER,to_list, fail_silently=False)

	queryset.delete()
	q.delete()

	return HttpResponseRedirect('/country_admin/')


def hospital_equipments(request):
	hid = request.GET['hid']

	try:
		queryset = equipment.objects.filter(hospital_id = hid)
	except:
		queryset = None
	

	context = {
		'queryset' :queryset,
		'hid' :hid
		}
	return render(request, 'equipments_hospital.html', context)


def see_equipments(request):
	hid = request.GET['hid']

	try:
		queryset = equipment.objects.filter(hospital_id = hid)
	except:
		queryset = None
	try:
		q = district_admin.objects.get(email = request.user.username)
	except:
		q = None

	try:
		q2 = country_admin.objects.get(email = request.user.username)
	except:
		q2 = None

	if q is None and q2 is None:
		raise PermissionDenied

	context = {
		'queryset' :queryset,
		'hid' :hid
		}
	return render(request, 'equipments_hospital.html', context)




def district_equipments(request):
	if not request.user.is_authenticated():
		raise PermissionDenied
	try:
		q = district_admin.objects.get(email = request.user.username)
	except:
		q = None
		
	try:
		q2 = country_admin.objects.get(email = request.user.username)
	except:
		q2 = None

	if q is None and q2 is None:
		raise PermissionDenied

	district = request.GET['district']

	if q is not None:
		if q.district != district:
			raise PermissionDenied

		try:
			queryset = equipment.objects.filter(district = district)
		except:
			queryset = None

		context = {
			'queryset' :queryset,
			'district' :district
			}

		return render(request, 'equipments_district.html' ,context)

	if q2 is not None:
		if q2.country != district:
			raise PermissionDenied

		try:
			queryset = equipment.objects.filter(country = district)
		except:
			queryset = None

		context = {
			'queryset' :queryset,
			'district' :district
			}

		return render(request, 'equipments_district.html' ,context)

def state_equipments(request):
	if not request.user.is_staff:
		raise PermissionDenied

	try:
		q = state_admin.objects.get(email = request.user.username)
	except:
		q = None
		raise PermissionDenied

	state = request.GET['state']

	if q.state != state:
		raise PermissionDenied

	try:
		queryset = equipment.objects.filter(state = state)
	except:
		queryset = None

	context = {
		'queryset' :queryset,
		'state' :state
		}

	return render(request, 'equipments_state.html' ,context)

def all_equipments(request):
	if not request.user.is_superuser:
		raise PermissionDenied


	try:
		queryset = equipment.objects.all()
	except:
		queryset = None

	context = {
		'queryset' :queryset
		}

	return render(request, 'equipments_all.html' ,context)

def show_country_admin(request):
	if not request.user.is_superuser:
		raise PermissionDenied
	try:
		print("yes")
		queryset = country_admin.objects.all()
		print("yes")
	except:
		print("NO")
		queryset = None
	context = {
		'queryset' :queryset
	}
	return render(request, 'country_admin.html', context)

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


def equipment_view(request):
	hid = request.GET['hid']
	print(hid)
	eid = request.GET['eid']
	print(eid)

	try:
		queryset = equipment.objects.get(hospital_id = hid, equipment_id = eid)
	except:
		queryset = None

	if request.method == 'POST':
		if request.user.is_superuser:
			raise PermissionDenied
		elif request.user.is_staff:
			raise PermissionDenied
		elif not request.user.is_authenticated:
			raise PermissionDenied
		else:
			try:
				q1 = district_admin.objects.get(email = request.user.username)
			except:
				q1 = None

			try:
				q2 = country_admin.objects.get(email = request.user.username)
			except:
				q2 = None

			if q1 is None and q2 is None:
				raise PermissionDenied

			if q1 is not None:
				if queryset.district != q1.district:
					raise PermissionDenied

			if q2 is not None:
				if queryset.country != q2.country:
					raise PermissionDenied

		equipment_form = equipment_update_form(request.POST, instance=queryset)

		if equipment_form.is_valid():
			equipment_form.save()

			if q1 is not None:
				dis = q1.district
			else:
				dis = q2.country

			return HttpResponseRedirect("/registration/equipment/success/?hid="+hid+"&eid="+eid)

		else:
			print(equipment_form.errors)
			messages.error(request, equipment_form.errors)
			return HttpResponseRedirect("/equipment_view/?hid="+hid+"&eid="+eid)

	args = {}

	args.update(csrf(request))

	if (not request.user.is_authenticated() ) or request.user.is_superuser or request.user.is_staff:
		args['equipment_form'] = equipment_viewonly_form(initial={'hospital_id':queryset.hospital_id, 'equipment_id':queryset.equipment_id, 'equipment_category':queryset.equipment_category, 'equipment_name':queryset.equipment_name, 'equipment_in_warranty':queryset.equipment_in_warranty, 'warranty_expiry':queryset.warranty_expiry, 'equipment_model':queryset.equipment_model, 'manufacturar':queryset.manufacturar, 'installation_date':queryset.installation_date, 'equipment_under_AMC_CMC':queryset.equipment_under_AMC_CMC, 'amc_upto':queryset.amc_upto, 'working_condition':queryset.working_condition, 'not_working_since':queryset.not_working_since, 'remarks':queryset.remarks, 'hospital_name':queryset.hospital_name, 'state':queryset.state, 'district':queryset.district , 'country':queryset.country , 'signed':queryset.signed })
		return render_to_response('equipment_viewonly.html', args, context_instance = RequestContext(request))

	try:
		q1 = district_admin.objects.get(email = request.user.username)
	except:
		q1 = None

	try:
		q2 = country_admin.objects.get(email = request.user.username)
	except:
		q2 = None

	if q1 is None and q2 is None:
		args['equipment_form'] = equipment_viewonly_form(initial={'hospital_id':queryset.hospital_id, 'equipment_id':queryset.equipment_id, 'equipment_category':queryset.equipment_category, 'equipment_name':queryset.equipment_name, 'equipment_in_warranty':queryset.equipment_in_warranty, 'warranty_expiry':queryset.warranty_expiry, 'equipment_model':queryset.equipment_model, 'manufacturar':queryset.manufacturar, 'installation_date':queryset.installation_date, 'equipment_under_AMC_CMC':queryset.equipment_under_AMC_CMC, 'amc_upto':queryset.amc_upto, 'working_condition':queryset.working_condition, 'not_working_since':queryset.not_working_since, 'remarks':queryset.remarks, 'hospital_name':queryset.hospital_name, 'state':queryset.state, 'district':queryset.district , 'country':queryset.country , 'signed':queryset.signed })
		return render_to_response('equipment_viewonly.html', args, context_instance = RequestContext(request))

	if q1 is not None:
		if queryset.district != q1.district:
			args['equipment_form'] = equipment_viewonly_form(initial={'hospital_id':queryset.hospital_id, 'equipment_id':queryset.equipment_id, 'equipment_category':queryset.equipment_category, 'equipment_name':queryset.equipment_name, 'equipment_in_warranty':queryset.equipment_in_warranty, 'warranty_expiry':queryset.warranty_expiry, 'equipment_model':queryset.equipment_model, 'manufacturar':queryset.manufacturar, 'installation_date':queryset.installation_date, 'equipment_under_AMC_CMC':queryset.equipment_under_AMC_CMC, 'amc_upto':queryset.amc_upto, 'working_condition':queryset.working_condition, 'not_working_since':queryset.not_working_since, 'remarks':queryset.remarks, 'hospital_name':queryset.hospital_name, 'state':queryset.state, 'district':queryset.district , 'country':queryset.country , 'signed':queryset.signed })
			return render_to_response('equipment_viewonly.html', args, context_instance = RequestContext(request))	

	if q2 is not None:
		if queryset.country != q2.country:
			args['equipment_form'] = equipment_viewonly_form(initial={'hospital_id':queryset.hospital_id, 'equipment_id':queryset.equipment_id, 'equipment_category':queryset.equipment_category, 'equipment_name':queryset.equipment_name, 'equipment_in_warranty':queryset.equipment_in_warranty, 'warranty_expiry':queryset.warranty_expiry, 'equipment_model':queryset.equipment_model, 'manufacturar':queryset.manufacturar, 'installation_date':queryset.installation_date, 'equipment_under_AMC_CMC':queryset.equipment_under_AMC_CMC, 'amc_upto':queryset.amc_upto, 'working_condition':queryset.working_condition, 'not_working_since':queryset.not_working_since, 'remarks':queryset.remarks, 'hospital_name':queryset.hospital_name, 'state':queryset.state, 'district':queryset.district , 'country':queryset.country , 'signed':queryset.signed })
			return render_to_response('equipment_viewonly.html', args, context_instance = RequestContext(request))	


	args['equipment_form'] = equipment_update_form(initial={'hospital_id':queryset.hospital_id, 'equipment_id':queryset.equipment_id, 'equipment_category':queryset.equipment_category, 'equipment_name':queryset.equipment_name, 'equipment_in_warranty':queryset.equipment_in_warranty, 'warranty_expiry':queryset.warranty_expiry, 'equipment_model':queryset.equipment_model, 'manufacturar':queryset.manufacturar, 'installation_date':queryset.installation_date, 'equipment_under_AMC_CMC':queryset.equipment_under_AMC_CMC, 'amc_upto':queryset.amc_upto, 'working_condition':queryset.working_condition, 'not_working_since':queryset.not_working_since, 'remarks':queryset.remarks, 'hospital_name':queryset.hospital_name, 'state':queryset.state, 'district':queryset.district , 'country':queryset.country , 'signed':queryset.signed })

	return render_to_response('equipment_update.html', args, context_instance = RequestContext(request))

def hospital_view(request):
	hid = request.GET['hid']
	print(hid)

	try:
		queryset = hospital.objects.get(hospital_id = hid)
	except:
		queryset = None

	if request.method == 'POST':
		if request.user.is_superuser:
			raise PermissionDenied
		elif request.user.is_staff:
			raise PermissionDenied
		elif not request.user.is_authenticated:
			raise PermissionDenied
		else:
			try:
				q1 = district_admin.objects.get(email = request.user.username)
			except:
				q1 = None

			try:
				q2 = country_admin.objects.get(email = request.user.username)
			except:
				q2 = None

			if q1 is None and q2 is None:
				raise PermissionDenied

			if q1 is not None:
				if queryset.district != q1.district:
					raise PermissionDenied

			if q2 is not None:
				if queryset.country != q2.country:
					raise PermissionDenied

		hospital_form = hospital_update_form(request.POST, instance=queryset)

		if hospital_form.is_valid():

			hospital_form.save()
			
			return HttpResponseRedirect('/registration/hospital/success/?hid='+hid)
			
		else:
			messages.error(request, hospital_form.errors)
			print(hospital_form.errors)
			return HttpResponseRedirect('/hospital_view/?hid='+hid)

	

	args = {}
	args.update(csrf(request))

	if (not request.user.is_authenticated() ) or request.user.is_superuser or request.user.is_staff:
		args['hospital_form'] = hospital_viewonly_form(initial={'hospital_id':queryset.hospital_id, 'hospital_name':queryset.hospital_name, 'hospital_type':queryset.hospital_type, 'hospital_cat':queryset.hospital_cat, 'email':queryset.email, 'mobile':queryset.mobile, 'address':queryset.address, 'country':queryset.country, 'state':queryset.state, 'district':queryset.district, 'pincode':queryset.pincode })
		return render_to_response('hospital_viewonly.html', args, context_instance = RequestContext(request))
	try:
		q1 = district_admin.objects.get(email = request.user.username)
	except:
		q1 = None

	try:
		q2 = country_admin.objects.get(email = request.user.username)
	except:
		q2 = None

	if q1 is not None:
		if q1.district!=queryset.district:
			args['hospital_form'] = hospital_viewonly_form(initial={'hospital_id':queryset.hospital_id, 'hospital_name':queryset.hospital_name, 'hospital_type':queryset.hospital_type, 'hospital_cat':queryset.hospital_cat, 'email':queryset.email, 'mobile':queryset.mobile, 'address':queryset.address, 'country':queryset.country, 'state':queryset.state, 'district':queryset.district, 'pincode':queryset.pincode })
			return render_to_response('hospital_viewonly.html', args, context_instance = RequestContext(request))

	if q2 is not None:
		if q2.country!=queryset.country:
			args['hospital_form'] = hospital_viewonly_form(initial={'hospital_id':queryset.hospital_id, 'hospital_name':queryset.hospital_name, 'hospital_type':queryset.hospital_type, 'hospital_cat':queryset.hospital_cat, 'email':queryset.email, 'mobile':queryset.mobile, 'address':queryset.address, 'country':queryset.country, 'state':queryset.state, 'district':queryset.district, 'pincode':queryset.pincode })
			return render_to_response('hospital_viewonly.html', args, context_instance = RequestContext(request))

	args['hospital_form'] = hospital_update_form(initial={'hospital_id':queryset.hospital_id, 'hospital_name':queryset.hospital_name, 'hospital_type':queryset.hospital_type, 'hospital_cat':queryset.hospital_cat, 'email':queryset.email, 'mobile':queryset.mobile, 'address':queryset.address, 'country':queryset.country, 'state':queryset.state, 'district':queryset.district, 'pincode':queryset.pincode })

	return render_to_response('hospital_update.html', args, context_instance = RequestContext(request))



def medical_equipments_form(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/login')
	if request.user.is_superuser:
		raise PermissionDenied
	if request.user.is_staff:
		return HttpResponseRedirect('/district_requests')

	hid = request.GET['hid']
	print(hid)

	try:
		q = hospital.objects.get(hospital_id = hid)
	except:
		q = None
		raise PermissionDenied

	if request.method == 'POST':
		equipment_form = equipmentform(request.POST)
		if equipment_form.is_valid():

			eid_avail = request.POST['equipment_id_available']

			if eid_avail == "No":
				sys_eid = _generate_equipment_id_()
				try:
					q1 = equipment.objects.get(hospital_id = hid, equipment_id = sys_eid)
				except:
					q1 = None

				while(q1 is not None):
					sys_eid = _generate_equipment_id_()
					try:
						q1 = equipment.objects.get(hospital_id = hid, equipment_id = sys_eid)
					except:
						q1 = None

				print(sys_eid)

			if eid_avail == "Yes":
				message = 'An equipment with equipment id : '+request.POST['equipment_id']+' was registerd by '+'hospital with hospital ID : '+hid+'  '+'Equipment ID : '+request.POST['equipment_id']+' and '+'Equipment Name : '+request.POST['equipment_name']
			else:
				message = 'An equipment with equipment id : '+request.POST['equipment_id']+' was registerd by '+'hospital with hospital ID : '+hid+'\nSince you did not provide with any equipment ID, a system generated equipment ID is being provided for any future reference. '+'Equipment ID : '+sys_eid+' and '+'Equipment Name : '+request.POST['equipment_name']
			
			to_list = [ 'naveenkenz12@gmail.com', q.email, request.user.username]
			send_mail('login credentials',message,settings.EMAIL_HOST_USER,to_list, fail_silently=False)

			updated_equipment = equipment()

			updated_equipment.hospital_id = request.POST['hospital_id']
			updated_equipment.equipment_id_available = request.POST['equipment_id_available']

			if eid_avail == "Yes":
				updated_equipment.equipment_id = request.POST['equipment_id']
				eid = request.POST['equipment_id']
			else:
				updated_equipment.equipment_id = sys_eid
				eid = sys_eid

			updated_equipment.hospital_name = request.POST['hospital_name']
			updated_equipment.equipment_category = request.POST['equipment_category']
			updated_equipment.equipment_name = request.POST['equipment_name']
			updated_equipment.equipment_in_warranty = request.POST['equipment_in_warranty']
			updated_equipment.warranty_expiry = request.POST['warranty_expiry']
			updated_equipment.equipment_model = request.POST['equipment_model']
			updated_equipment.manufacturar = request.POST['manufacturar']
			updated_equipment.installation_date = request.POST['installation_date']
			updated_equipment.equipment_under_AMC_CMC = request.POST['equipment_under_AMC_CMC']
			updated_equipment.amc_upto = request.POST['amc_upto']
			updated_equipment.working_condition = request.POST['working_condition']
			updated_equipment.not_working_since = request.POST['not_working_since']
			updated_equipment.remarks = request.POST['remarks']
			updated_equipment.district = request.POST['district']
			updated_equipment.state = request.POST['state']
			updated_equipment.country = request.POST['country']
			updated_equipment.signed = request.POST['signed']

			updated_equipment.save()


			return HttpResponseRedirect('/registration/equipment/success/?hid='+hid+'&eid='+eid)
		else:
			messages.error(request, equipment_form.errors)
			print(equipment_form.errors)
			return HttpResponseRedirect('/medical_equipments_form')

	args = {}
	args.update(csrf(request))

	args['equipment_form'] = equipmentform(initial = {'hospital_id':q.hospital_id, 'hospital_name':q.hospital_name, 'state':q.state , 'district':q.district , 'signed':request.user.username ,'country':q.country })

	return render_to_response('medical_equipments_form.html' , args, context_instance = RequestContext(request))

	#return render(request, 'user.html', context)

def login(request):
	if not request.user.is_authenticated():
		log = {}
		log.update(csrf(request))
		return render_to_response('medical_equipments_form.html', log, context_instance = RequestContext(request))
	else:
		return HttpResponseRedirect('/')

def logout(request):
	auth.logout(request)
	render_to_response('medical_equipments_form.html', {})
	return HttpResponseRedirect('/')

def authorized_view(request):
	username = request.POST.get('username','')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password =password )

	if user is not None:
		auth.login(request,user)
		return HttpResponseRedirect('/user')
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
				form = state_adminform(initial = {'email':queryset.email ,'state':queryset.state, 'country':queryset.country, 'email2':queryset.email2, 'first_name':queryset.first_name, 'middle_name':queryset.middle_name, 'last_name':queryset.last_name, 'mobile':queryset.mobile, 'mobile2':queryset.mobile2, 'agex':queryset.agex, 'gender':queryset.gender , 'education':queryset.education , 'address':queryset.address, 'file':queryset.file })

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

		try:
			queryset2 = country_admin.objects.get(email = request.user.username)
		except:
			queryset2 = None
			
		if queryset is None and queryset2 is None:
			raise PermissionDenied
	
		if queryset is not None:
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
					form = district_adminform(initial = {'email':queryset.email ,'country':queryset.country, 'state':queryset.state, 'district':queryset.district,  'email2':queryset.email2, 'first_name':queryset.first_name, 'middle_name':queryset.middle_name, 'last_name':queryset.last_name, 'mobile':queryset.mobile, 'mobile2':queryset.mobile2, 'agex':queryset.agex, 'gender':queryset.gender , 'education':queryset.education , 'address':queryset.address, 'file':queryset.file })

				except:
					form = district_adminform(initial = {'email':request.user.username })
			context = {
			'district_adminform' :form,
			'queryset' :queryset
			}
	
			return render(request, 'user.html', context)

		elif queryset2 is not None:
			if request.method == 'POST':
				form = country_adminform(request.POST, instance = queryset2)
				print(queryset2)
				if form.is_valid():
					form.save()
					return HttpResponseRedirect('/user')
				else:
					print(form.errors)
			else:
				try:
					form = country_adminform(initial = {'email':queryset2.email ,'country':queryset2.country,  'email2':queryset2.email2, 'first_name':queryset2.first_name, 'middle_name':queryset2.middle_name, 'last_name':queryset2.last_name, 'mobile':queryset2.mobile, 'mobile2':queryset2.mobile2, 'agex':queryset2.agex, 'gender':queryset2.gender , 'education':queryset2.education , 'address':queryset2.address, 'file':queryset2.file })

				except:
					form = country_adminform(initial = {'email':request.user.username })
			context = {
			'country_adminform' :form,
			'queryset' :queryset2
			}
			print("anmol")
			return render(request, 'country_user.html', context)
	
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

	try:
		q2 = country_admin.objects.get(email = request.user.username)
	except:
		q2 = None

	if q is None and q2 is None:
		raise PermissionDenied

	try:
		q_state = q.state
	except:
		q_state = q2.country 								#in case of outside india, take country

	if request.method == 'POST':
		hospital_form = hospitalform(request.POST)
		if hospital_form.is_valid():

			hid_avail = request.POST['hospital_id_available']

			if hid_avail == "No":
				sys_hid = _generate_hospital_id_(q_state)
				try:
					q1 = hospital.objects.get(hospital_id = sys_hid)
				except:
					q1 = None

				while(q1 is not None):
					sys_hid = _generate_hospital_id_(q_state)
					try:
						q1 = hospital.objects.get(hospital_id = sys_hid)
					except:
						q1 = None

				print(sys_hid)

			if hid_avail == "Yes":
				message = 'Hospital with Hospital Name : '+request.POST['hospital_name']+' and hospital ID : '+request.POST['hospital_id']+' has been registerd by '+request.user.username+'.'
			else:
				message = 'Hospital with Hospital Name : '+request.POST['hospital_name']+' has been registerd by '+request.user.username+'. '+'Since no hospital id was provided, A System Generated Hospital ID is being provided, for any future reference.  '+'HOSPITAL ID : '+sys_hid
			
			to_list = [ 'naveenkenz12@gmail.com', request.POST['email'], request.user.username]
			send_mail('login credentials',message,settings.EMAIL_HOST_USER,to_list, fail_silently=False)

			updated_hospital = hospital()

			updated_hospital.hospital_id_available = request.POST['hospital_id_available']
			if hid_avail == "Yes":
				updated_hospital.hospital_id = request.POST['hospital_id']
				hid = request.POST['hospital_id']
			else:
				updated_hospital.hospital_id = sys_hid
				hid = sys_hid

			updated_hospital.hospital_name = request.POST['hospital_name']
			updated_hospital.hospital_type = request.POST['hospital_type']
			updated_hospital.hospital_cat = request.POST['hospital_cat']
			print(request.POST['hospital_cat'])
			print(updated_hospital.hospital_cat)
			updated_hospital.email = request.POST['email']
			updated_hospital.mobile = request.POST['mobile']
			updated_hospital.address = request.POST['address']
			updated_hospital.state = request.POST['state']
			updated_hospital.country = request.POST['country']
			updated_hospital.district = request.POST['district']
			updated_hospital.pincode = request.POST['pincode']

			updated_hospital.save()
			return HttpResponseRedirect('/registration/hospital/success/?hid='+hid)
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

	try:
		args['hospital_form'] = hospitalform(initial = {'state':q.state , 'district':q.district ,'country':q.country })
	except:
		args['hospital_form'] = hospitalform(initial = {'country':q2.country })

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

	try:
		q2 = country_admin.objects.get(email = request.user.username)
	except:
		q2 = None

	if q is None and q2 is None:
		raise PermissionDenied

	if q is not None:
		try:
			queryset = hospital.objects.filter(district = q.district)
		except:
			queryset = None

	if q2 is not None:
		try:
			queryset = hospital.objects.filter(country = q2.country)
		except:
			queryset = None



	context = {
	'queryset' :queryset
	}
	return render(request, 'current_hospital.html', context)

def state_hospital(request):
	state = request.GET['state']
	try:
		queryset = hospital.objects.filter(state = state)
	except:
		queryset = None



	context = {
	'queryset' :queryset,
	'state' :state
	}
	return render(request, 'view_hospital.html', context)

def all_hospital(request):
	
	try:
		queryset = hospital.objects.all()
	except:
		queryset = None



	context = {
	'queryset' :queryset
	}
	return render(request, 'view_hospital.html', context)


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

    
