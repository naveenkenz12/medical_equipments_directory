from django import forms
from medical_equipments.models import userpost
#from medical_equipments.models import UserProfile
from medical_equipments.models import request_for_state_admin
#from medical_equipments.models import state_admin
#from medical_equipments.models import userregister
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#from medical_equipments.models import allocated_branch

#from medical_equipments.models import branch_stats

import re
import random
import string

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

class userpostform(forms.ModelForm):

	class Meta:
		model = userpost
		fields = ('user_name','name',)
		widgets = { 'user_name':forms.TextInput(attrs={'class':'form-control','readonly': 'True' ,'style':'display:none'}),'name':forms.TextInput(attrs={'placeholder':'Name','class':'form-control'}) }
		

# class userregisterform(UserCreationForm):
# 	email = forms.EmailField(required=True)

# 	class Meta:
# 		model = userregister
# 		fields = ("username", "name", "email", "password1", "password2")

# 	def save(self, commit=True):
# 		user = super(userregisterform, self).save(commit = False)
# 		user.email = self.cleaned_data["email"]

# 		if commit:
# 			user.save()
# 		return user

class uniqueuseremailfield(forms.EmailField):
	"""
	An EmailFiels which only is valid if no User has that email.
	"""

	def validate(self, value):
		super(forms.EmailField, self).validate(value)
		try:
			User.objects.get(email = value)
			raise forms.ValidationError("Email Already Exists")
		except User.MultipleObjectsReturned:
			raise forms.ValidationError("Email Already Exists")
		except User.DoesNotExist:
			pass

class userregisterform(UserCreationForm):
	username = forms.CharField(required = True, max_length = 50)
	email = forms.EmailField(required = True, label = 'Email address')
	mobile = forms.CharField(required = True, label = 'Mobile number')
	first_name = forms.CharField(required = True, max_length = 50)
	middle_name = forms.CharField(required = False, max_length = 50, label = 'Middle name')
	last_name = forms.CharField(required = False, max_length = 50)

	def __init__(self, *args, **kwargs):
		super(UserCreationForm, self).__init__(*args, **kwargs)
		self.fields.keyOrder = ['username' , 'email', 'first_name', 'middle_name' , 'last_name', 'mobile' , 'password1', 'password2']

	def __generate_username(self, email):
		# highest_user_id = User.objects.all().order_by('-id')[0].id
		# leading_part_of_email = email.split('@',1)[0]
		# leading_part_of_email = re.sub(r'[^a-zA-Z0-9+]', '',leading_part_of_email)
		# truncated_part_of_email = leading_part_of_email[:3] \
		# 	 + leading_part_of_email[-3:]
		# derived_username = truncated_part_of_email + str(highest_user_id+1)
		# return derived_username
		return email

	def clean(self, *args, **kwargs):
		cleaned_data = super(UserCreationForm, self).clean(*args, **kwargs)
		if 'email' in cleaned_data:
			cleaned_data['username'] = self.__generate_username(cleaned_data['email'])

		return cleaned_data

	def save(self, commit = True):
		user = super(UserCreationForm, self).save(commit)
		if user:
			user.email = self.cleaned_data['email']
			user.mobile = self.cleaned_data['mobile']
			user.first_name = self.cleaned_data['first_name']
			user.middle_name = self.cleaned_data['middle_name']
			user.label = self.cleaned_data['last_name']
			user.set_password(self.cleaned_data['password1'])

			if commit:
				#user.is_staff = True
				print("apple")
				user.save()
		return user

class request_for_state_admin_form(forms.ModelForm):
	andaman = 'Andaman and Nicobar Islands'
	andhra = 'Andhra Pradesh'
	arunachal = 'Arunachal Pradesh'
	assam = 'Assam'
	bihar  = 'Bihar'
	chandigarh = 'Chandigarh'
	chattisgarh = 'Chattisgarh'
	dadra = 'Dadra and Nagar Haveli'
	daman = 'Daman and Diu'
	delhi = 'Delhi'
	goa = 'Goa'
	gujrat = 'Gujrat'
	haryana = 'Haryana'
	himachal = 'Himachal Pradesh'
	jammu = 'Jammu and Kashmir'
	jharkhand = 'Jharkhand'
	karnataka = 'Karnataka'
	kerala = 'Kerala'
	lakshadweep = 'Lakshadweep'
	madhya = 'Madhya Pradesh'
	maharashtra = 'Maharashtra'
	manipur = 'Manipur'
	meghalaya = 'Meghalaya'
	mizoram = 'Mizoram'
	nagaland = 'Nagaland'
	odisha = 'Odisha'
	puducherry = 'Puducherry'
	punjab = 'Punjab'
	rajasthan = 'Rajasthan'
	sikkim = 'Sikkim'
	tamil = 'Tamil Nadu'
	telangana = 'Telangana'
	tripura = 'Tripura'
	uttar = 'Uttar Pradesh'
	uttarakhand = 'Uttarakhand'
	west = 'West Bengal'

	STATE_LIST = ((andaman,andaman),(andhra,andhra),(arunachal,arunachal),(assam,assam),(bihar,bihar),(chandigarh,chandigarh),(chattisgarh,chattisgarh),(dadra,dadra),(daman,daman),(delhi,delhi),(goa,goa),(gujrat,gujrat),(haryana,haryana),(himachal,himachal),(jammu,jammu),(jharkhand,jharkhand),(karnataka,karnataka),(kerala,kerala),(lakshadweep,lakshadweep),(madhya,madhya),(maharashtra,maharashtra),(manipur,manipur),(meghalaya,meghalaya),(mizoram,mizoram),(nagaland,nagaland),(odisha,odisha),(puducherry,puducherry),(punjab,punjab),(rajasthan,rajasthan),(sikkim,sikkim),(tamil,tamil),(telangana,telangana),(tripura,tripura),(uttar,uttar),(uttarakhand,uttarakhand),(west,west),)

	state = forms.ChoiceField(choices = STATE_LIST, required = True, widget=forms.Select(attrs={'class':'form-control'}))



	file = forms.FileField(required = False)

	class Meta:
		model = request_for_state_admin
		fields = ('email','first_name','middle_name','last_name','state','mobile','file')
		widgets = {'email':forms.TextInput(attrs={'placeholder':'email id','class':'form-control'}),'mobile':forms.TextInput(attrs={'placeholder':'mobile number','class':'form-control'}),'first_name':forms.TextInput(attrs={'placeholder':'first name','class':'form-control'}),'middle_name':forms.TextInput(attrs={'placeholder':'middle name','class':'form-control'}),'last_name':forms.TextInput(attrs={'placeholder':'last name','class':'form-control'}),}



# class state_adminform(forms.ModelForm):
# 	andaman = 'Andaman and Nicobar Islands'
# 	andhra = 'Andhra Pradesh'
# 	arunachal = 'Arunachal Pradesh'
# 	assam = 'Assam'
# 	bihar  = 'Bihar'
# 	chandigarh = 'Chandigarh'
# 	chattisgarh = 'Chattisgarh'
# 	dadra = 'Dadra and Nagar Haveli'
# 	daman = 'Daman and Diu'
# 	delhi = 'Delhi'
# 	goa = 'Goa'
# 	gujrat = 'Gujrat'
# 	haryana = 'Haryana'
# 	himachal = 'Himachal Pradesh'
# 	jammu = 'Jammu and Kashmir'
# 	jharkhand = 'Jharkhand'
# 	karnataka = 'Karnataka'
# 	kerala = 'Kerala'
# 	lakshadweep = 'Lakshadweep'
# 	madhya = 'Madhya Pradesh'
# 	maharashtra = 'Maharashtra'
# 	manipur = 'Manipur'
# 	meghalaya = 'Meghalaya'
# 	mizoram = 'Mizoram'
# 	nagaland = 'Nagaland'
# 	odisha = 'Odisha'
# 	puducherry = 'Puducherry'
# 	punjab = 'Punjab'
# 	rajasthan = 'Rajasthan'
# 	sikkim = 'Sikkim'
# 	tamil = 'Tamil Nadu'
# 	telangana = 'Telangana'
# 	tripura = 'Tripura'
# 	uttar = 'Uttar Pradesh'
# 	uttarakhand = 'Uttarakhand'
# 	west = 'West Bengal'

# 	STATE_LIST = ((andaman,andaman),(andhra,andhra),(arunachal,arunachal),(assam,assam),(bihar,bihar),(chandigarh,chandigarh),(chattisgarh,chattisgarh),(dadra,dadra),(daman,daman),(delhi,delhi),(goa,goa),(gujrat,gujrat),(haryana,haryana),(himachal,himachal),(jammu,jammu),(jharkhand,jharkhand),(karnataka,karnataka),(kerala,kerala),(lakshadweep,lakshadweep),(madhya,madhya),(maharashtra,maharashtra),(manipur,manipur),(meghalaya,meghalaya),(mizoram,mizoram),(nagaland,nagaland),(odisha,odisha),(puducherry,puducherry),(punjab,punjab),(rajasthan,rajasthan),(sikkim,sikkim),(tamil,tamil),(telangana,telangana),(tripura,tripura),(uttar,uttar),(uttarakhand,uttarakhand),(west,west),)

# 	state = forms.ChoiceField(choices = STATE_LIST, required = True, widget=forms.Select(attrs={'class':'form-control'}))



# 	file = forms.FileField(required = False)

# 	class Meta:
# 		model = state_admin
# 		fields = ('email','first_name','middle_name','last_name','state','mobile','file')
# 		widgets = {'email':forms.TextInput(attrs={'placeholder':'email id','class':'form-control'}),'mobile':forms.TextInput(attrs={'placeholder':'mobile number','class':'form-control'}),'first_name':forms.TextInput(attrs={'placeholder':'first name','class':'form-control'}),'middle_name':forms.TextInput(attrs={'placeholder':'middle name','class':'form-control'}),'last_name':forms.TextInput(attrs={'placeholder':'last name','class':'form-control'}),}

