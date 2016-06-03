from django import forms
from medical_equipments.models import equipment
#from medical_equipments.models import UserProfile
from medical_equipments.models import request_for_state_admin
from medical_equipments.models import request_for_district_admin

from medical_equipments.models import state_admin
from medical_equipments.models import district_admin
from medical_equipments.models import hospital


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

from django.utils.translation import ugettext_lazy as _
# from countries_states.data import Country
# from django.db.models import Q

class equipmentform(forms.ModelForm):
	
	class Meta:
		model = equipment
		fields = ('hospital_id','equipment_id','hospital_name','state','district','signed')
		
		widgets = {'hospital_id':forms.TextInput(attrs={'placeholder':'Hospital ID','readonly':True,'class':'form-control'}),'equipment_id':forms.TextInput(attrs={'placeholder':'equipment id','class':'form-control'}),'hospital_name':forms.TextInput(attrs={'placeholder':'hospital name','class':'form-control','readonly':True}),'state':forms.TextInput(attrs={'placeholder':'state','class':'form-control','readonly':True}),'district':forms.TextInput(attrs={'placeholder':'district','class':'form-control','readonly':True}),'signed':forms.TextInput(attrs={'placeholder':'email id','readonly':True,'class':'form-control'}),}
		

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



class state_adminform(forms.ModelForm):
	

	file = forms.FileField(required = False)

	class Meta:
		model = state_admin
		fields = ('email','email2','first_name','middle_name','last_name','state','mobile','mobile2','address','file')
		widgets = { 'email':forms.TextInput(attrs={'placeholder':'email id','readonly':True, 'class':'form-control'}),'email2':forms.TextInput(attrs={'placeholder':'email id', 'class':'form-control'}),'mobile':forms.TextInput(attrs={'placeholder':'mobile number','class':'form-control'}),'mobile2':forms.TextInput(attrs={'placeholder':'mobile number','class':'form-control'}),'first_name':forms.TextInput(attrs={'placeholder':'first name','readonly':True,'class':'form-control'}),'middle_name':forms.TextInput(attrs={'placeholder':'middle name','readonly':True,'class':'form-control'}),'last_name':forms.TextInput(attrs={'placeholder':'last name','readonly':True,'class':'form-control'}),'address':forms.TextInput(attrs={'placeholder':'address','class':'form-control'}), 'state':forms.TextInput(attrs={'placeholder':'state','readonly':True,'class':'form-control'}),}


class request_for_district_admin_form(forms.ModelForm):
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

	nicobar = 'Nicobar'
	northandmiddleandaman = 'North and Middle Andaman'
	southandaman = 'South Andaman'
	anantapur = 'Anantapur'
	chittor = 'Chittor'
	eastgodavari = 'East Godavari'
	guntur = 'Guntur'
	kadapa = 'Kadapa'
	krishna = 'Krishna'
	kurnool = 'Kurnool'
	prakasam = 'Prakasam'
	sripottisriramulunellore = 'Sri Potti Sriramulu Nellore'
	srikakulam = 'Srikakulam'
	visakhapatnam = 'Visakhapatnam'
	vizianagaram = 'Vizianagaram'
	westgodavari = 'West Godavari'
	anjaw = 'Anjaw'
	changlang = 'Changlang'
	dibangvalley = 'Dibang Valley'
	eastkameng = 'East Kameng'
	eastsiang = 'East Siang'
	kradaadi = 'Kra Daadi'
	kurungkumey = 'Kurung Kumey'
	lohit = 'Lohit'
	longding = 'Longding'
	lowerdibangvalley = 'Lower Dibang Valley'
	lowersubansiri = 'Lower Subansiri'
	namsai = 'Namsai'
	papumpare = 'Papum Pare'
	siang = 'Siang'
	tawang = 'Tawang'
	tirap = 'Tirap'
	uppersiang = 'Upper Siang'
	uppersubansiri = 'Upper Subansiri'
	westkameng = 'West Kameng'
	westsiang = 'West Siang'
	baksa = 'Baksa'
	barpeta = 'Barpeta'
	bishwanath = 'Bishwanath'
	bongaigaon = 'Bongaigaon'
	cachar = 'Cachar'
	charaideo = 'Charaideo'
	chirang = 'Chirang'
	darrang = 'Darrang'
	dhemaji = 'Dhemaji'
	dhubri = 'Dhubri'
	dibrugarh = 'Dibrugarh'
	dimahasao = 'Dima Hasao'
	eastkamrup = 'East Kamrup'
	goalpara = 'Goalpara'
	golaghat = 'Golaghat'
	hailakandi = 'Hailakandi'
	hojai = 'Hojai'
	jorhat = 'Jorhat'
	kamrup = 'Kamrup'
	kamrupmetropolitan = 'Kamrup Metropolitan'
	karbianglong = 'Karbi Anglong'
	karimganj = 'Karimganj'
	kokrajhar = 'Kokrajhar'
	lakhimpur = 'Lakhimpur'
	morigaon = 'Morigaon'
	nagaon = 'Nagaon'
	nalbari = 'Nalbari'
	sivasagar = 'Sivasagar'
	sonitpur = 'Sonitpur'
	southkamrup = 'South Kamrup'
	southsalmaramanakachar = 'South Salmara-Manakachar'
	tinsukia = 'Tinsukia'
	udalguri = 'Udalguri'
	westkarbianglong = 'West Karbi Anglong'
	araria = 'Araria'
	arwal = 'Arwal'
	aurangabad = 'Aurangabad'
	banka = 'Banka'
	begusarai = 'Begusarai'
	bhagalpur = 'Bhagalpur'
	bhojpur = 'Bhojpur'
	buxar = 'Buxar'
	darbhanga = 'Darbhanga'
	eastchamparan = 'East Champaran'
	gaya = 'Gaya'
	gopalganj = 'Gopalganj'
	jamui = 'Jamui'
	jehanabad = 'Jehanabad'
	kaimur = 'Kaimur'
	katihar = 'Katihar'
	khagaria = 'Khagaria'
	kishanganj = 'Kishanganj'
	lakhisarai = 'Lakhisarai'
	madhepura = 'Madhepura'
	madhubani = 'Madhubani'
	munger = 'Munger'
	muzaffarpur = 'Muzaffarpur'
	nalanda = 'Nalanda'
	nawada = 'Nawada'
	patna = 'Patna'
	purnia = 'Purnia'
	rohtas = 'Rohtas'
	saharsa = 'Saharsa'
	samastipur = 'Samastipur'
	saran = 'Saran'
	sheikhpura = 'Sheikhpura'
	sheohar = 'Sheohar'
	sitamarhi = 'Sitamarhi'
	siwan = 'Siwan'
	supaul = 'Supaul'
	vaishali = 'Vaishali'
	westchamparan = 'West Champaran'
	chandigarh = 'Chandigarh'
	balod = 'Balod'
	balodabazar = 'Baloda Bazar'
	balrampur = 'Balrampur'
	bastar = 'Bastar'
	bemetara = 'Bemetara'
	bijapur = 'Bijapur'
	bilaspur = 'Bilaspur'
	dantewada = 'Dantewada'
	dhamtari = 'Dhamtari'
	durg = 'Durg'
	gariaband = 'Gariaband'
	janjgirchampa = 'Janjgir-Champa'
	jashpur = 'Jashpur'
	kabirdhamformerlykawardha = 'Kabirdham (formerly Kawardha)'
	kanker = 'Kanker'
	kondagaon = 'Kondagaon'
	korba = 'Korba'
	koriya = 'Koriya'
	mahasamund = 'Mahasamund'
	mungeli = 'Mungeli'
	narayanpur = 'Narayanpur'
	raigarh = 'Raigarh'
	raipur = 'Raipur'
	rajnandgaon = 'Rajnandgaon'
	sukma = 'Sukma'
	surajpur = 'Surajpur'
	surguja = 'Surguja'
	dadraandnagarhaveli = 'Dadra and Nagar Haveli'
	daman = 'Daman'
	diu = 'Diu'
	centraldelhi = 'Central Delhi'
	eastdelhi = 'East Delhi'
	newdelhi = 'New Delhi'
	northdelhi = 'North Delhi'
	northeastdelhi = 'North East Delhi'
	northwestdelhi = 'North West Delhi'
	shahdara = 'Shahdara'
	southdelhi = 'South Delhi'
	southeastdelhi = 'South East Delhi'
	southwestdelhi = 'South West Delhi'
	westdelhi = 'West Delhi'
	northgoa = 'North Goa'
	southgoa = 'South Goa'
	ahmedabad = 'Ahmedabad'
	amrelidistrict = 'Amreli district'
	anand = 'Anand'
	aravalli = 'Aravalli'
	banaskantha = 'Banaskantha'
	bharuch = 'Bharuch'
	bhavnagar = 'Bhavnagar'
	botad = 'Botad'
	chhotaudaipur = 'Chhota Udaipur'
	dahod = 'Dahod'
	dang = 'Dang'
	devbhoomidwarka = 'Devbhoomi Dwarka'
	gandhinagar = 'Gandhinagar'
	girsomnath = 'Gir Somnath'
	jamnagar = 'Jamnagar'
	junagadh = 'Junagadh'
	kheda = 'Kheda'
	kutch = 'Kutch'
	mahisagar = 'Mahisagar'
	mehsana = 'Mehsana'
	morbi = 'Morbi'
	narmada = 'Narmada'
	navsari = 'Navsari'
	panchmahal = 'Panchmahal'
	patan = 'Patan'
	porbandar = 'Porbandar'
	rajkot = 'Rajkot'
	sabarkantha = 'Sabarkantha'
	surat = 'Surat'
	surendranagar = 'Surendranagar'
	tapi = 'Tapi'
	vadodara = 'Vadodara'
	valsad = 'Valsad'
	ambala = 'Ambala'
	bhiwani = 'Bhiwani'
	faridabad = 'Faridabad'
	fatehabad = 'Fatehabad'
	gurgaon = 'Gurgaon'
	hissar = 'Hissar'
	jhajjar = 'Jhajjar'
	jind = 'Jind'
	kaithal = 'Kaithal'
	karnal = 'Karnal'
	kurukshetra = 'Kurukshetra'
	mahendragarh = 'Mahendragarh'
	mewat = 'Mewat'
	palwal = 'Palwal'
	panchkula = 'Panchkula'
	panipat = 'Panipat'
	rewari = 'Rewari'
	rohtak = 'Rohtak'
	sirsa = 'Sirsa'
	sonipat = 'Sonipat'
	yamunanagar = 'Yamuna Nagar'
	bilaspur = 'Bilaspur'
	chamba = 'Chamba'
	hamirpur = 'Hamirpur'
	kangra = 'Kangra'
	kinnaur = 'Kinnaur'
	kullu = 'Kullu'
	lahaulandspiti = 'Lahaul and Spiti'
	mandi = 'Mandi'
	shimla = 'Shimla'
	sirmaur = 'Sirmaur'
	solan = 'Solan'
	una = 'Una'
	anantnag = 'Anantnag'
	badgam = 'Badgam'
	bandipora = 'Bandipora'
	baramulla = 'Baramulla'
	doda = 'Doda'
	ganderbal = 'Ganderbal'
	jammu = 'Jammu'
	kargil = 'Kargil'
	kathua = 'Kathua'
	kishtwar = 'Kishtwar'
	kulgam = 'Kulgam'
	kupwara = 'Kupwara'
	leh = 'Leh'
	poonch = 'Poonch'
	pulwama = 'Pulwama'
	rajouri = 'Rajouri'
	ramban = 'Ramban'
	reasi = 'Reasi'
	samba = 'Samba'
	shopian = 'Shopian'
	srinagar = 'Srinagar'
	udhampur = 'Udhampur'
	bokaro = 'Bokaro'
	chatra = 'Chatra'
	deoghar = 'Deoghar'
	dhanbad = 'Dhanbad'
	dumka = 'Dumka'
	eastsinghbhum = 'East Singhbhum'
	garhwa = 'Garhwa'
	giridih = 'Giridih'
	godda = 'Godda'
	gumla = 'Gumla'
	hazaribag = 'Hazaribag'
	jamtara = 'Jamtara'
	khunti = 'Khunti'
	koderma = 'Koderma'
	latehar = 'Latehar'
	lohardaga = 'Lohardaga'
	pakur = 'Pakur'
	palamu = 'Palamu'
	ramgarh = 'Ramgarh'
	ranchi = 'Ranchi'
	sahibganj = 'Sahibganj'
	seraikelakharsawan = 'Seraikela Kharsawan'
	simdega = 'Simdega'
	westsinghbhum = 'West Singhbhum'
	bagalkot = 'Bagalkot'
	bangalorerural = 'Bangalore Rural'
	bangaloreurban = 'Bangalore Urban'
	belgaum = 'Belgaum'
	bellary = 'Bellary'
	bidar = 'Bidar'
	chamarajnagar = 'Chamarajnagar'
	chikkaballapur = 'Chikkaballapur'
	chikkamagaluru = 'Chikkamagaluru'
	chitradurga = 'Chitradurga'
	dakshinakannada = 'Dakshina Kannada'
	davanagere = 'Davanagere'
	dharwad = 'Dharwad'
	gadag = 'Gadag'
	gulbarga = 'Gulbarga'
	hassan = 'Hassan'
	haveridistrict = 'Haveri district'
	kodagu = 'Kodagu'
	kolar = 'Kolar'
	koppal = 'Koppal'
	mandya = 'Mandya'
	mysore = 'Mysore'
	raichur = 'Raichur'
	ramanagara = 'Ramanagara'
	shimoga = 'Shimoga'
	tumkur = 'Tumkur'
	udupi = 'Udupi'
	uttarakannada = 'Uttara Kannada'
	vijayapura = 'Vijayapura'
	yadgir = 'Yadgir'
	alappuzha = 'Alappuzha'
	ernakulam = 'Ernakulam'
	idukki = 'Idukki'
	kannur = 'Kannur'
	kasaragod = 'Kasaragod'
	kollam = 'Kollam'
	kottayam = 'Kottayam'
	kozhikode = 'Kozhikode'
	malappuram = 'Malappuram'
	palakkad = 'Palakkad'
	pathanamthitta = 'Pathanamthitta'
	thiruvananthapuram = 'Thiruvananthapuram'
	thrissur = 'Thrissur'
	wayanad = 'Wayanad'
	lakshadweep = 'Lakshadweep'
	agar = 'Agar'
	alirajpur = 'Alirajpur'
	anuppur = 'Anuppur'
	ashoknagar = 'Ashok Nagar'
	balaghat = 'Balaghat'
	barwani = 'Barwani'
	betul = 'Betul'
	bhind = 'Bhind'
	bhopal = 'Bhopal'
	burhanpur = 'Burhanpur'
	chhatarpur = 'Chhatarpur'
	chhindwara = 'Chhindwara'
	damoh = 'Damoh'
	datia = 'Datia'
	dewas = 'Dewas'
	dhar = 'Dhar'
	dindori = 'Dindori'
	guna = 'Guna'
	gwalior = 'Gwalior'
	harda = 'Harda'
	hoshangabad = 'Hoshangabad'
	indore = 'Indore'
	jabalpur = 'Jabalpur'
	jhabua = 'Jhabua'
	katni = 'Katni'
	khandwaeastnimar = 'Khandwa (East Nimar)'
	khargonewestnimar = 'Khargone (West Nimar)'
	mandla = 'Mandla'
	mandsaur = 'Mandsaur'
	morena = 'Morena'
	narsinghpur = 'Narsinghpur'
	neemuch = 'Neemuch'
	panna = 'Panna'
	raisen = 'Raisen'
	rajgarh = 'Rajgarh'
	ratlam = 'Ratlam'
	rewa = 'Rewa'
	sagar = 'Sagar'
	satna = 'Satna'
	sehore = 'Sehore'
	seoni = 'Seoni'
	shahdol = 'Shahdol'
	shajapur = 'Shajapur'
	sheopur = 'Sheopur'
	shivpuri = 'Shivpuri'
	sidhi = 'Sidhi'
	singrauli = 'Singrauli'
	tikamgarh = 'Tikamgarh'
	ujjain = 'Ujjain'
	umaria = 'Umaria'
	vidisha = 'Vidisha'
	ahmednagar = 'Ahmednagar'
	akola = 'Akola'
	amravati = 'Amravati'
	aurangabad = 'Aurangabad'
	beed = 'Beed'
	bhandara = 'Bhandara'
	buldhana = 'Buldhana'
	chandrapur = 'Chandrapur'
	dhule = 'Dhule'
	gadchiroli = 'Gadchiroli'
	gondia = 'Gondia'
	hingoli = 'Hingoli'
	jalgaon = 'Jalgaon'
	jalna = 'Jalna'
	kolhapur = 'Kolhapur'
	latur = 'Latur'
	mumbaicity = 'Mumbai City'
	mumbaisuburban = 'Mumbai suburban'
	nagpur = 'Nagpur'
	nande = 'Nande'
	nandurbar = 'Nandurbar'
	nashik = 'Nashik'
	osmanabad = 'Osmanabad'
	palghar = 'Palghar'
	parbhani = 'Prabhani'
	pune = 'Pune'
	raigad = 'Raigad'
	ratnagiri = 'Ratnagiri'
	sangli = 'Sangli'
	satara = 'Satara'
	sindhudurg = 'Sindhudurg'
	solapur = 'Solapur'
	thane = 'Thane'
	wardha = 'Wardha'
	washim = 'Washim'
	yavatmal = 'Yavatmal'
	bishnupur = 'Bishnupur'
	chandel = 'Chandel'
	churachandpur = 'Churachandpur'
	imphaleast = 'Imphal East'
	imphalwest = 'Imphal West'
	senapati = 'Senapati'
	tamenglong = 'Tamenglong'
	thoubal = 'Thoubal'
	ukhrul = 'Ukhrul'
	eastgarohills = 'East Garo Hills'
	eastjaintiahills = 'East Jaintia Hills'
	eastkhasihills = 'East Khasi Hills'
	northgarohills = 'North Garo Hills'
	ribhoi = 'Ri Bhoi'
	southgarohills = 'South Garo Hills'
	southwestgarohills = 'South West Garo Hills'
	southwestkhasihills = 'South West Khasi Hills'
	westgarohills = 'West Garo Hills'
	westjaintiahills = 'West Jaintia Hills'
	westkhasihills = 'West Khasi Hills'
	aizwal = 'Aizwal'
	champhai = 'Champhai'
	kolasib = 'Kolasib'
	lawngtlai = 'Lawngtlai'
	lunglei = 'Lunglei'
	mamit = 'Mamit'
	saiha = 'Saiha'
	serchhip = 'Serchhip'
	dimapur = 'Dimapur'
	kiphire = 'Kiphire'
	kohima = 'Kohima'
	longleng = 'Longleng'
	mokokchung = 'Mokokchung'
	mon = 'Mon'
	peren = 'Peren'
	phek = 'Phek'
	tuensang = 'Tuensang'
	wokha = 'Wokha'
	zunheboto = 'Zunheboto'
	angul = 'Angul'
	balangir = 'Balangir'
	balasore = 'Balasore'
	bargarhbaragarh = 'Bargarh (Baragarh)'
	bhadrak = 'Bhadrak'
	boudhbauda = 'Boudh (Bauda)'
	cuttack = 'Cuttack'
	debagarhdeogarh = 'Debagarh (Deogarh)'
	dhenkanal = 'Dhenkanal'
	gajapati = 'Gajapati'
	ganjam = 'Ganjam'
	jagatsinghpur = 'Jagatsinghpur'
	jajpur = 'Jajpur'
	jharsuguda = 'Jharsuguda'
	kalahandi = 'Kalahandi'
	kandhamal = 'Kandhamal'
	kendrapara = 'Kendrapara'
	kendujharkeonjhar = 'Kendujhar (Keonjhar)'
	khordha = 'Khordha'
	koraput = 'Koraput'
	malkangiri = 'Malkangiri'
	mayurbhanj = 'Mayurbhanj'
	nabarangpur = 'Nabarangpur'
	nayagarh = 'Nayagarh'
	nuapada = 'Nuapada'
	puri = 'Puri'
	rayagada = 'Rayagada'
	sambalpur = 'Sambalpur'
	subarnapursonepur = 'Subarnapur (Sonepur)'
	sundargarh = 'Sundargarh'
	karaikal = 'Karaikal'
	mahe = 'Mahe'
	pondicherry = 'Pondicherry'
	yanam = 'Yanam'
	amritsar = 'Amritsar'
	barnala = 'Barnala'
	bathinda = 'Bathinda'
	faridkot = 'Faridkot'
	fatehgarhsahib = 'Fatehgarh Sahib'
	fazilka = 'Fazilka'
	firozpur = 'Firozpur'
	gurdaspur = 'Gurdaspur'
	hoshiarpur = 'Hoshiarpur'
	jalandhar = 'Jalandhar'
	kapurthala = 'Kapurthala'
	ludhiana = 'Ludhiana'
	mansa = 'Mansa'
	moga = 'Moga'
	pathankot = 'Pathankot'
	patiala = 'Patiala'
	rupnagar = 'Rupnagar'
	sahibzadaajitsinghnagar = 'Sahibzada Ajit Singh Nagar'
	sangrur = 'Sangrur'
	shahidbhagatsinghnagar = 'Shahid Bhagat Singh Nagar'
	srimuktsarsahib = 'Sri Muktsar Sahib'
	tarntaran = 'Tarn Taran'
	ajmer = 'Ajmer'
	alwar = 'Alwar'
	banswara = 'Banswara'
	baran = 'Baran'
	barmer = 'Barmer'
	bharatpur = 'Bharatpur'
	bhilwara = 'Bhilwara'
	bikaner = 'Bikaner'
	bundi = 'Bundi'
	chittorgarh = 'Chittorgarh'
	churu = 'Churu'
	dausa = 'Dausa'
	dholpur = 'Dholpur'
	dungapur = 'Dungapur'
	ganganagar = 'Ganganagar'
	hanumangarh = 'Hanumangarh'
	jaipur = 'Jaipur'
	jaisalmer = 'Jaisalmer'
	jalore = 'Jalore'
	jhalawar = 'Jhalawar'
	jhunjhunu = 'Jhunjhunu'
	jodhpur = 'Jodhpur'
	karauli = 'Karauli'
	kota = 'Kota'
	nagaur = 'Nagaur'
	pali = 'Pali'
	pratapgarh = 'Pratapgarh'
	rajsamand = 'Rajsamand'
	sawaimadhopur = 'Sawai Madhopur'
	sikar = 'Sikar'
	sirohi = 'Sirohi'
	tonk = 'Tonk'
	udaipur = 'Udaipur'
	eastsikkim = 'East Sikkim'
	northsikkim = 'North Sikkim'
	southsikkim = 'South Sikkim'
	westsikkim = 'West Sikkim'
	ariyalur = 'Ariyalur'
	chennai = 'Chennai'
	coimbatore = 'Coimbatore'
	cuddalore = 'Cuddalore'
	dharmapuri = 'Dharmapuri'
	dindigul = 'Dindigul'
	erode = 'Erode'
	kanchipuram = 'Kanchipuram'
	kanyakumari = 'Kanyakumari'
	karur = 'Karur'
	krishnagiri = 'Krishnagiri'
	madurai = 'Madurai'
	nagapattinam = 'Nagapattinam'
	namakkal = 'Namakkal'
	nilgiris = 'Nilgiris'
	perambalur = 'Perambalur'
	pudukkottai = 'Pudukkottai'
	ramanathapuram = 'Ramanathapuram'
	salem = 'Salem'
	sivaganga = 'Sivaganga'
	thanjavur = 'Thanjavur'
	theni = 'Theni'
	thoothukudi = 'Thoothukudi'
	tiruchirappalli = 'Tiruchirappalli'
	tirunelveli = 'Tirunelveli'
	tirupur = 'Tirupur'
	tiruvallur = 'Tiruvallur'
	tiruvannamalai = 'Tiruvannamalai'
	tiruvarur = 'Tiruvarur'
	vellore = 'Vellore'
	viluppuram = 'Viluppuram'
	virudhunagar = 'Virudhunagar'
	adilabad = 'Adilabad'
	hyderabad = 'Hyderabad'
	karimnagar = 'Karimnagar'
	khammam = 'Khammam'
	mahbubnagar = 'Mahbubnagar'
	medak = 'Medak'
	nalgonda = 'Nalgonda'
	nizamabad = 'Nizamabad'
	rangareddy = 'Ranga Reddy'
	warangal = 'Warangal'
	dhalai = 'Dhalai'
	gomati = 'Gomati'
	khowai = 'Khowai'
	northtripura = 'North Tripura'
	sepahijala = 'Sepahijala'
	southtripura = 'South Tripura'
	unokoti = 'Unokoti'
	westtripura = 'West Tripura'
	agra = 'Agra'
	aligarh = 'Aligarh'
	allahabad = 'Allahabad'
	ambedkarnagar = 'Ambedkar Nagar'
	amethichhatrapatishahujimaharajnagar = 'Amethi (Chhatrapati Shahuji Maharaj Nagar)'
	auraiya = 'Auraiya'
	azamgarh = 'Azamgarh'
	bagpat = 'Bagpat'
	bahraich = 'Bahraich'
	ballia = 'Ballia'
	balrampur = 'Balrampur'
	banda = 'Banda'
	barabanki = 'Barabanki'
	bareilly = 'Bareilly'
	basti = 'Basti'
	bijnor = 'Bijnor'
	budaun = 'Budaun'
	bulandshahr = 'Bulandshahr'
	chandauli = 'Chandauli'
	chitrakoot = 'Chitrakoot'
	deoria = 'Deoria'
	etah = 'Etah'
	etawah = 'Etawah'
	faizabad = 'Faizabad'
	farrukhabad = 'Farrukhabad'
	fatehpur = 'Fatehpur'
	firozabad = 'Firozabad'
	gautambuddhnagar = 'Gautam Buddh Nagar'
	ghaziabad = 'Ghaziabad'
	ghazipur = 'Ghazipur'
	gonda = 'Gonda'
	gorakhpur = 'Gorakhpur'
	hamirpur = 'Hamirpur'
	hapurpanchsheelnagar = 'Hapur (Panchsheel Nagar)'
	hardoi = 'Hardoi'
	hathrasmahamayanagar = 'Hathras (Mahamaya Nagar)'
	jalaun = 'Jalaun'
	jaunpurdistrict = 'Jaunpur district'
	jhansi = 'Jhansi'
	jyotibaphulenagar = 'Jyotiba Phule Nagar'
	kannauj = 'Kannauj'
	kanpurdehatramabainagar = 'Kanpur Dehat (Ramabai Nagar)'
	kanpurnagar = 'Kanpur Nagar'
	kanshiramnagar = 'Kanshi Ram Nagar'
	kaushambi = 'Kaushambi'
	kushinagar = 'Kushinagar'
	lakhimpurkheri = 'Lakhimpur Kheri'
	lalitpur = 'Lalitpur'
	lucknow = 'Lucknow'
	maharajganj = 'Maharajganj'
	mahoba = 'Mahoba'
	mainpuri = 'Mainpuri'
	mathura = 'Mathura'
	mau = 'Mau'
	meerut = 'Meerut'
	mirzapur = 'Mirzapur'
	moradabad = 'Moradabad'
	muzaffarnagar = 'Muzaffarnagar'
	pilibhit = 'Pilibhit'
	pratapgarh = 'Pratapgarh'
	raebareli = 'Raebareli'
	rampur = 'Rampur'
	saharanpur = 'Saharanpur'
	sambhalbheemnagar = 'Sambhal(Bheem Nagar)'
	santkabirnagar = 'Sant Kabir Nagar'
	santravidasnagar = 'Sant Ravidas Nagar'
	shahjahanpur = 'Shahjahanpur'
	shamli = 'Shamli'
	shravasti = 'Shravasti'
	siddharthnagar = 'Siddharthnagar'
	sitapur = 'Sitapur'
	sonbhadra = 'Sonbhadra'
	sultanpur = 'Sultanpur'
	unnao = 'Unnao'
	varanasialmora = 'Varanasi Almora'
	bageshwar = 'Bageshwar'
	chamoli = 'Chamoli'
	champawat = 'Champawat'
	dehradun = 'Dehradun'
	haridwar = 'Haridwar'
	nainital = 'Nainital'
	paurigarhwal = 'Pauri Garhwal'
	pithoragarh = 'Pithoragarh'
	rudraprayag = 'Rudraprayag'
	tehrigarhwal = 'Tehri Garhwal'
	udhamsinghnagar = 'Udham Singh Nagar'
	uttarkashi = 'Uttarkashi'
	alipurduar = 'Alipurduar'
	bankura = 'Bankura'
	bardhaman = 'Bardhaman'
	birbhum = 'Birbhum'
	coochbehar = 'Cooch Behar'
	dakshindinajpur = 'Dakshin Dinajpur'
	darjeeling = 'Darjeeling'
	hooghly = 'Hooghly'
	howrah = 'Howrah'
	jalpaiguri = 'Jalpaiguri'
	kolkata = 'Kolkata'
	maldah = 'Maldah'
	murshidabad = 'Murshidabad'
	nadia = 'Nadia'
	north24parganas = 'North 24 Parganas'
	paschimmedinipur = 'Paschim Medinipur'
	purbamedinipur = 'Purba Medinipur'
	purulia = 'Purulia'
	south24parganas = 'South 24 Parganas'
	uttardinajpur = 'Uttar Dinajpur'
	
	DISTRICT_LIST = ((nicobar ,nicobar ),(northandmiddleandaman ,northandmiddleandaman ),(southandaman ,southandaman ),(anantapur ,anantapur ),(chittor ,chittor ),(eastgodavari ,eastgodavari ),(guntur ,guntur ),(kadapa ,kadapa ),(krishna ,krishna ),(kurnool ,kurnool ),(prakasam ,prakasam ),(sripottisriramulunellore ,sripottisriramulunellore ),(srikakulam ,srikakulam ),(visakhapatnam ,visakhapatnam ),(vizianagaram ,vizianagaram ),(westgodavari ,westgodavari ),(anjaw ,anjaw ),(changlang ,changlang ),(dibangvalley ,dibangvalley ),(eastkameng ,eastkameng ),(eastsiang ,eastsiang ),(kradaadi ,kradaadi ),(kurungkumey ,kurungkumey ),(lohit ,lohit ),(longding ,longding ),(lowerdibangvalley ,lowerdibangvalley ),(lowersubansiri ,lowersubansiri ),(namsai ,namsai ),(papumpare ,papumpare ),(siang ,siang ),(tawang ,tawang ),(tirap ,tirap ),(uppersiang ,uppersiang ),(uppersubansiri ,uppersubansiri ),(westkameng ,westkameng ),(westsiang ,westsiang ),(baksa ,baksa ),(barpeta ,barpeta ),(bishwanath ,bishwanath ),(bongaigaon ,bongaigaon ),(cachar ,cachar ),(charaideo ,charaideo ),(chirang ,chirang ),(darrang ,darrang ),(dhemaji ,dhemaji ),(dhubri ,dhubri ),(dibrugarh ,dibrugarh ),(dimahasao ,dimahasao ),(eastkamrup ,eastkamrup ),(goalpara ,goalpara ),(golaghat ,golaghat ),(hailakandi ,hailakandi ),(hojai ,hojai ),(jorhat ,jorhat ),(kamrup ,kamrup ),(kamrupmetropolitan ,kamrupmetropolitan ),(karbianglong ,karbianglong ),(karimganj ,karimganj ),(kokrajhar ,kokrajhar ),(lakhimpur ,lakhimpur ),(morigaon ,morigaon ),(nagaon ,nagaon ),(nalbari ,nalbari ),(sivasagar ,sivasagar ),(sonitpur ,sonitpur ),(southkamrup ,southkamrup ),(southsalmaramanakachar ,southsalmaramanakachar ),(tinsukia ,tinsukia ),(udalguri ,udalguri ),(westkarbianglong ,westkarbianglong ),(araria ,araria ),(arwal ,arwal ),(aurangabad ,aurangabad ),(banka ,banka ),(begusarai ,begusarai ),(bhagalpur ,bhagalpur ),(bhojpur ,bhojpur ),(buxar ,buxar ),(darbhanga ,darbhanga ),(eastchamparan ,eastchamparan ),(gaya ,gaya ),(gopalganj ,gopalganj ),(jamui ,jamui ),(jehanabad ,jehanabad ),(kaimur ,kaimur ),(katihar ,katihar ),(khagaria ,khagaria ),(kishanganj ,kishanganj ),(lakhisarai ,lakhisarai ),(madhepura ,madhepura ),(madhubani ,madhubani ),(munger ,munger ),(muzaffarpur ,muzaffarpur ),(nalanda ,nalanda ),(nawada ,nawada ),(patna ,patna ),(purnia ,purnia ),(rohtas ,rohtas ),(saharsa ,saharsa ),(samastipur ,samastipur ),(saran ,saran ),(sheikhpura ,sheikhpura ),(sheohar ,sheohar ),(sitamarhi ,sitamarhi ),(siwan ,siwan ),(supaul ,supaul ),(vaishali ,vaishali ),(westchamparan ,westchamparan ),(chandigarh ,chandigarh ),(balod ,balod ),(balodabazar ,balodabazar ),(balrampur ,balrampur ),(bastar ,bastar ),(bemetara ,bemetara ),(bijapur ,bijapur ),(bilaspur ,bilaspur ),(dantewada ,dantewada ),(dhamtari ,dhamtari ),(durg ,durg ),(gariaband ,gariaband ),(janjgirchampa ,janjgirchampa ),(jashpur ,jashpur ),(kabirdhamformerlykawardha ,kabirdhamformerlykawardha ),(kanker ,kanker ),(kondagaon ,kondagaon ),(korba ,korba ),(koriya ,koriya ),(mahasamund ,mahasamund ),(mungeli ,mungeli ),(narayanpur ,narayanpur ),(raigarh ,raigarh ),(raipur ,raipur ),(rajnandgaon ,rajnandgaon ),(sukma ,sukma ),(surajpur ,surajpur ),(surguja ,surguja ),(dadraandnagarhaveli ,dadraandnagarhaveli ),(daman ,daman ),(diu ,diu ),(centraldelhi ,centraldelhi ),(eastdelhi ,eastdelhi ),(newdelhi ,newdelhi ),(northdelhi ,northdelhi ),(northeastdelhi ,northeastdelhi ),(northwestdelhi ,northwestdelhi ),(shahdara ,shahdara ),(southdelhi ,southdelhi ),(southeastdelhi ,southeastdelhi ),(southwestdelhi ,southwestdelhi ),(westdelhi ,westdelhi ),(northgoa ,northgoa ),(southgoa ,southgoa ),(ahmedabad ,ahmedabad ),(amrelidistrict ,amrelidistrict ),(anand ,anand ),(aravalli ,aravalli ),(banaskantha ,banaskantha ),(bharuch ,bharuch ),(bhavnagar ,bhavnagar ),(botad ,botad ),(chhotaudaipur ,chhotaudaipur ),(dahod ,dahod ),(dang ,dang ),(devbhoomidwarka ,devbhoomidwarka ),(gandhinagar ,gandhinagar ),(girsomnath ,girsomnath ),(jamnagar ,jamnagar ),(junagadh ,junagadh ),(kheda ,kheda ),(kutch ,kutch ),(mahisagar ,mahisagar ),(mehsana ,mehsana ),(morbi ,morbi ),(narmada ,narmada ),(navsari ,navsari ),(panchmahal ,panchmahal ),(patan ,patan ),(porbandar ,porbandar ),(rajkot ,rajkot ),(sabarkantha ,sabarkantha ),(surat ,surat ),(surendranagar ,surendranagar ),(tapi ,tapi ),(vadodara ,vadodara ),(valsad ,valsad ),(ambala ,ambala ),(bhiwani ,bhiwani ),(faridabad ,faridabad ),(fatehabad ,fatehabad ),(gurgaon ,gurgaon ),(hissar ,hissar ),(jhajjar ,jhajjar ),(jind ,jind ),(kaithal ,kaithal ),(karnal ,karnal ),(kurukshetra ,kurukshetra ),(mahendragarh ,mahendragarh ),(mewat ,mewat ),(palwal ,palwal ),(panchkula ,panchkula ),(panipat ,panipat ),(rewari ,rewari ),(rohtak ,rohtak ),(sirsa ,sirsa ),(sonipat ,sonipat ),(yamunanagar ,yamunanagar ),(bilaspur ,bilaspur ),(chamba ,chamba ),(hamirpur ,hamirpur ),(kangra ,kangra ),(kinnaur ,kinnaur ),(kullu ,kullu ),(lahaulandspiti ,lahaulandspiti ),(mandi ,mandi ),(shimla ,shimla ),(sirmaur ,sirmaur ),(solan ,solan ),(una ,una ),(anantnag ,anantnag ),(badgam ,badgam ),(bandipora ,bandipora ),(baramulla ,baramulla ),(doda ,doda ),(ganderbal ,ganderbal ),(jammu ,jammu ),(kargil ,kargil ),(kathua ,kathua ),(kishtwar ,kishtwar ),(kulgam ,kulgam ),(kupwara ,kupwara ),(leh ,leh ),(poonch ,poonch ),(pulwama ,pulwama ),(rajouri ,rajouri ),(ramban ,ramban ),(reasi ,reasi ),(samba ,samba ),(shopian ,shopian ),(srinagar ,srinagar ),(udhampur ,udhampur ),(bokaro ,bokaro ),(chatra ,chatra ),(deoghar ,deoghar ),(dhanbad ,dhanbad ),(dumka ,dumka ),(eastsinghbhum ,eastsinghbhum ),(garhwa ,garhwa ),(giridih ,giridih ),(godda ,godda ),(gumla ,gumla ),(hazaribag ,hazaribag ),(jamtara ,jamtara ),(khunti ,khunti ),(koderma ,koderma ),(latehar ,latehar ),(lohardaga ,lohardaga ),(pakur ,pakur ),(palamu ,palamu ),(ramgarh ,ramgarh ),(ranchi ,ranchi ),(sahibganj ,sahibganj ),(seraikelakharsawan ,seraikelakharsawan ),(simdega ,simdega ),(westsinghbhum ,westsinghbhum ),(bagalkot ,bagalkot ),(bangalorerural ,bangalorerural ),(bangaloreurban ,bangaloreurban ),(belgaum ,belgaum ),(bellary ,bellary ),(bidar ,bidar ),(chamarajnagar ,chamarajnagar ),(chikkaballapur ,chikkaballapur ),(chikkamagaluru ,chikkamagaluru ),(chitradurga ,chitradurga ),(dakshinakannada ,dakshinakannada ),(davanagere ,davanagere ),(dharwad ,dharwad ),(gadag ,gadag ),(gulbarga ,gulbarga ),(hassan ,hassan ),(haveridistrict ,haveridistrict ),(kodagu ,kodagu ),(kolar ,kolar ),(koppal ,koppal ),(mandya ,mandya ),(mysore ,mysore ),(raichur ,raichur ),(ramanagara ,ramanagara ),(shimoga ,shimoga ),(tumkur ,tumkur ),(udupi ,udupi ),(uttarakannada ,uttarakannada ),(vijayapura ,vijayapura ),(yadgir ,yadgir ),(alappuzha ,alappuzha ),(ernakulam ,ernakulam ),(idukki ,idukki ),(kannur ,kannur ),(kasaragod ,kasaragod ),(kollam ,kollam ),(kottayam ,kottayam ),(kozhikode ,kozhikode ),(malappuram ,malappuram ),(palakkad ,palakkad ),(pathanamthitta ,pathanamthitta ),(thiruvananthapuram ,thiruvananthapuram ),(thrissur ,thrissur ),(wayanad ,wayanad ),(lakshadweep ,lakshadweep ),(agar ,agar ),(alirajpur ,alirajpur ),(anuppur ,anuppur ),(ashoknagar ,ashoknagar ),(balaghat ,balaghat ),(barwani ,barwani ),(betul ,betul ),(bhind ,bhind ),(bhopal ,bhopal ),(burhanpur ,burhanpur ),(chhatarpur ,chhatarpur ),(chhindwara ,chhindwara ),(damoh ,damoh ),(datia ,datia ),(dewas ,dewas ),(dhar ,dhar ),(dindori ,dindori ),(guna ,guna ),(gwalior ,gwalior ),(harda ,harda ),(hoshangabad ,hoshangabad ),(indore ,indore ),(jabalpur ,jabalpur ),(jhabua ,jhabua ),(katni ,katni ),(khandwaeastnimar ,khandwaeastnimar ),(khargonewestnimar ,khargonewestnimar ),(mandla ,mandla ),(mandsaur ,mandsaur ),(morena ,morena ),(narsinghpur ,narsinghpur ),(neemuch ,neemuch ),(panna ,panna ),(raisen ,raisen ),(rajgarh ,rajgarh ),(ratlam ,ratlam ),(rewa ,rewa ),(sagar ,sagar ),(satna ,satna ),(sehore ,sehore ),(seoni ,seoni ),(shahdol ,shahdol ),(shajapur ,shajapur ),(sheopur ,sheopur ),(shivpuri ,shivpuri ),(sidhi ,sidhi ),(singrauli ,singrauli ),(tikamgarh ,tikamgarh ),(ujjain ,ujjain ),(umaria ,umaria ),(vidisha ,vidisha ),(ahmednagar ,ahmednagar ),(akola ,akola ),(amravati ,amravati ),(aurangabad ,aurangabad ),(beed ,beed ),(bhandara ,bhandara ),(buldhana ,buldhana ),(chandrapur ,chandrapur ),(dhule ,dhule ),(gadchiroli ,gadchiroli ),(gondia ,gondia ),(hingoli ,hingoli ),(jalgaon ,jalgaon ),(jalna ,jalna ),(kolhapur ,kolhapur ),(latur ,latur ),(mumbaicity ,mumbaicity ),(mumbaisuburban ,mumbaisuburban ),(nagpur ,nagpur ),(nande ,nande ),(nandurbar ,nandurbar ),(nashik ,nashik ),(osmanabad ,osmanabad ),(palghar ,palghar ),(parbhani,parbhani ),(pune,pune),(raigad ,raigad ),(ratnagiri ,ratnagiri ),(sangli ,sangli ),(satara ,satara ),(sindhudurg ,sindhudurg ),(solapur ,solapur ),(thane ,thane ),(wardha ,wardha ),(washim ,washim ),(yavatmal ,yavatmal ),(bishnupur ,bishnupur ),(chandel ,chandel ),(churachandpur ,churachandpur ),(imphaleast ,imphaleast ),(imphalwest ,imphalwest ),(senapati ,senapati ),(tamenglong ,tamenglong ),(thoubal ,thoubal ),(ukhrul ,ukhrul ),(eastgarohills ,eastgarohills ),(eastjaintiahills ,eastjaintiahills ),(eastkhasihills ,eastkhasihills ),(northgarohills ,northgarohills ),(ribhoi ,ribhoi ),(southgarohills ,southgarohills ),(southwestgarohills ,southwestgarohills ),(southwestkhasihills ,southwestkhasihills ),(westgarohills ,westgarohills ),(westjaintiahills ,westjaintiahills ),(westkhasihills ,westkhasihills ),(aizwal ,aizwal ),(champhai ,champhai ),(kolasib ,kolasib ),(lawngtlai ,lawngtlai ),(lunglei ,lunglei ),(mamit ,mamit ),(saiha ,saiha ),(serchhip ,serchhip ),(dimapur ,dimapur ),(kiphire ,kiphire ),(kohima ,kohima ),(longleng ,longleng ),(mokokchung ,mokokchung ),(mon ,mon ),(peren ,peren ),(phek ,phek ),(tuensang ,tuensang ),(wokha ,wokha ),(zunheboto ,zunheboto ),(angul ,angul ),(balangir ,balangir ),(balasore ,balasore ),(bargarhbaragarh ,bargarhbaragarh ),(bhadrak ,bhadrak ),(boudhbauda ,boudhbauda ),(cuttack ,cuttack ),(debagarhdeogarh ,debagarhdeogarh ),(dhenkanal ,dhenkanal ),(gajapati ,gajapati ),(ganjam ,ganjam ),(jagatsinghpur ,jagatsinghpur ),(jajpur ,jajpur ),(jharsuguda ,jharsuguda ),(kalahandi ,kalahandi ),(kandhamal ,kandhamal ),(kendrapara ,kendrapara ),(kendujharkeonjhar ,kendujharkeonjhar ),(khordha ,khordha ),(koraput ,koraput ),(malkangiri ,malkangiri ),(mayurbhanj ,mayurbhanj ),(nabarangpur ,nabarangpur ),(nayagarh ,nayagarh ),(nuapada ,nuapada ),(puri ,puri ),(rayagada ,rayagada ),(sambalpur ,sambalpur ),(subarnapursonepur ,subarnapursonepur ),(sundargarh ,sundargarh ),(karaikal ,karaikal ),(mahe ,mahe ),(pondicherry ,pondicherry ),(yanam ,yanam ),(amritsar ,amritsar ),(barnala ,barnala ),(bathinda ,bathinda ),(faridkot ,faridkot ),(fatehgarhsahib ,fatehgarhsahib ),(fazilka ,fazilka ),(firozpur ,firozpur ),(gurdaspur ,gurdaspur ),(hoshiarpur ,hoshiarpur ),(jalandhar ,jalandhar ),(kapurthala ,kapurthala ),(ludhiana ,ludhiana ),(mansa ,mansa ),(moga ,moga ),(pathankot ,pathankot ),(patiala ,patiala ),(rupnagar ,rupnagar ),(sahibzadaajitsinghnagar ,sahibzadaajitsinghnagar ),(sangrur ,sangrur ),(shahidbhagatsinghnagar ,shahidbhagatsinghnagar ),(srimuktsarsahib ,srimuktsarsahib ),(tarntaran ,tarntaran ),(ajmer ,ajmer ),(alwar ,alwar ),(banswara ,banswara ),(baran ,baran ),(barmer ,barmer ),(bharatpur ,bharatpur ),(bhilwara ,bhilwara ),(bikaner ,bikaner ),(bundi ,bundi ),(chittorgarh ,chittorgarh ),(churu ,churu ),(dausa ,dausa ),(dholpur ,dholpur ),(dungapur ,dungapur ),(ganganagar ,ganganagar ),(hanumangarh ,hanumangarh ),(jaipur ,jaipur ),(jaisalmer ,jaisalmer ),(jalore ,jalore ),(jhalawar ,jhalawar ),(jhunjhunu ,jhunjhunu ),(jodhpur ,jodhpur ),(karauli ,karauli ),(kota ,kota ),(nagaur ,nagaur ),(pali ,pali ),(pratapgarh ,pratapgarh ),(rajsamand ,rajsamand ),(sawaimadhopur ,sawaimadhopur ),(sikar ,sikar ),(sirohi ,sirohi ),(tonk ,tonk ),(udaipur ,udaipur ),(eastsikkim ,eastsikkim ),(northsikkim ,northsikkim ),(southsikkim ,southsikkim ),(westsikkim ,westsikkim ),(ariyalur ,ariyalur ),(chennai ,chennai ),(coimbatore ,coimbatore ),(cuddalore ,cuddalore ),(dharmapuri ,dharmapuri ),(dindigul ,dindigul ),(erode ,erode ),(kanchipuram ,kanchipuram ),(kanyakumari ,kanyakumari ),(karur ,karur ),(krishnagiri ,krishnagiri ),(madurai ,madurai ),(nagapattinam ,nagapattinam ),(namakkal ,namakkal ),(nilgiris ,nilgiris ),(perambalur ,perambalur ),(pudukkottai ,pudukkottai ),(ramanathapuram ,ramanathapuram ),(salem ,salem ),(sivaganga ,sivaganga ),(thanjavur ,thanjavur ),(theni ,theni ),(thoothukudi ,thoothukudi ),(tiruchirappalli ,tiruchirappalli ),(tirunelveli ,tirunelveli ),(tirupur ,tirupur ),(tiruvallur ,tiruvallur ),(tiruvannamalai ,tiruvannamalai ),(tiruvarur ,tiruvarur ),(vellore ,vellore ),(viluppuram ,viluppuram ),(virudhunagar ,virudhunagar ),(adilabad ,adilabad ),(hyderabad ,hyderabad ),(karimnagar ,karimnagar ),(khammam ,khammam ),(mahbubnagar ,mahbubnagar ),(medak ,medak ),(nalgonda ,nalgonda ),(nizamabad ,nizamabad ),(rangareddy ,rangareddy ),(warangal ,warangal ),(dhalai ,dhalai ),(gomati ,gomati ),(khowai ,khowai ),(northtripura ,northtripura ),(sepahijala ,sepahijala ),(southtripura ,southtripura ),(unokoti ,unokoti ),(westtripura ,westtripura ),(agra ,agra ),(aligarh ,aligarh ),(allahabad ,allahabad ),(ambedkarnagar ,ambedkarnagar ),(amethichhatrapatishahujimaharajnagar ,amethichhatrapatishahujimaharajnagar ),(auraiya ,auraiya ),(azamgarh ,azamgarh ),(bagpat ,bagpat ),(bahraich ,bahraich ),(ballia ,ballia ),(balrampur ,balrampur ),(banda ,banda ),(barabanki ,barabanki ),(bareilly ,bareilly ),(basti ,basti ),(bijnor ,bijnor ),(budaun ,budaun ),(bulandshahr ,bulandshahr ),(chandauli ,chandauli ),(chitrakoot ,chitrakoot ),(deoria ,deoria ),(etah ,etah ),(etawah ,etawah ),(faizabad ,faizabad ),(farrukhabad ,farrukhabad ),(fatehpur ,fatehpur ),(firozabad ,firozabad ),(gautambuddhnagar ,gautambuddhnagar ),(ghaziabad ,ghaziabad ),(ghazipur ,ghazipur ),(gonda ,gonda ),(gorakhpur ,gorakhpur ),(hamirpur ,hamirpur ),(hapurpanchsheelnagar ,hapurpanchsheelnagar ),(hardoi ,hardoi ),(hathrasmahamayanagar ,hathrasmahamayanagar ),(jalaun ,jalaun ),(jaunpurdistrict ,jaunpurdistrict ),(jhansi ,jhansi ),(jyotibaphulenagar ,jyotibaphulenagar ),(kannauj ,kannauj ),(kanpurdehatramabainagar ,kanpurdehatramabainagar ),(kanpurnagar ,kanpurnagar ),(kanshiramnagar ,kanshiramnagar ),(kaushambi ,kaushambi ),(kushinagar ,kushinagar ),(lakhimpurkheri ,lakhimpurkheri ),(lalitpur ,lalitpur ),(lucknow ,lucknow ),(maharajganj ,maharajganj ),(mahoba ,mahoba ),(mainpuri ,mainpuri ),(mathura ,mathura ),(mau ,mau ),(meerut ,meerut ),(mirzapur ,mirzapur ),(moradabad ,moradabad ),(muzaffarnagar ,muzaffarnagar ),(pilibhit ,pilibhit ),(pratapgarh ,pratapgarh ),(raebareli ,raebareli ),(rampur ,rampur ),(saharanpur ,saharanpur ),(sambhalbheemnagar ,sambhalbheemnagar ),(santkabirnagar ,santkabirnagar ),(santravidasnagar ,santravidasnagar ),(shahjahanpur ,shahjahanpur ),(shamli ,shamli ),(shravasti ,shravasti ),(siddharthnagar ,siddharthnagar ),(sitapur ,sitapur ),(sonbhadra ,sonbhadra ),(sultanpur ,sultanpur ),(unnao ,unnao ),(varanasialmora ,varanasialmora ),(bageshwar ,bageshwar ),(chamoli ,chamoli ),(champawat ,champawat ),(dehradun ,dehradun ),(haridwar ,haridwar ),(nainital ,nainital ),(paurigarhwal ,paurigarhwal ),(pithoragarh ,pithoragarh ),(rudraprayag ,rudraprayag ),(tehrigarhwal ,tehrigarhwal ),(udhamsinghnagar ,udhamsinghnagar ),(uttarkashi ,uttarkashi ),(alipurduar ,alipurduar ),(bankura ,bankura ),(bardhaman ,bardhaman ),(birbhum ,birbhum ),(coochbehar ,coochbehar ),(dakshindinajpur ,dakshindinajpur ),(darjeeling ,darjeeling ),(hooghly ,hooghly ),(howrah ,howrah ),(jalpaiguri ,jalpaiguri ),(kolkata ,kolkata ),(maldah ,maldah ),(murshidabad ,murshidabad ),(nadia ,nadia ),(north24parganas ,north24parganas ),(paschimmedinipur ,paschimmedinipur ),(purbamedinipur ,purbamedinipur ),(purulia ,purulia ),(south24parganas ,south24parganas ),(uttardinajpur ,uttardinajpur),)


	STATE_LIST = ((andaman,andaman),(andhra,andhra),(arunachal,arunachal),(assam,assam),(bihar,bihar),(chandigarh,chandigarh),(chattisgarh,chattisgarh),(dadra,dadra),(daman,daman),(delhi,delhi),(goa,goa),(gujrat,gujrat),(haryana,haryana),(himachal,himachal),(jammu,jammu),(jharkhand,jharkhand),(karnataka,karnataka),(kerala,kerala),(lakshadweep,lakshadweep),(madhya,madhya),(maharashtra,maharashtra),(manipur,manipur),(meghalaya,meghalaya),(mizoram,mizoram),(nagaland,nagaland),(odisha,odisha),(puducherry,puducherry),(punjab,punjab),(rajasthan,rajasthan),(sikkim,sikkim),(tamil,tamil),(telangana,telangana),(tripura,tripura),(uttar,uttar),(uttarakhand,uttarakhand),(west,west),)

	state = forms.ChoiceField(choices = STATE_LIST, required = True, widget=forms.Select(attrs={'class':'form-control'}))

	district = forms.ChoiceField(choices = DISTRICT_LIST, required = True, widget=forms.Select(attrs={'class':'form-control'}))


	file = forms.FileField(required = False)

	class Meta:
		model = request_for_district_admin
		fields = ('email','first_name','middle_name','last_name','state','district','mobile','file')
		widgets = {'email':forms.TextInput(attrs={'placeholder':'email id','class':'form-control'}),'mobile':forms.TextInput(attrs={'placeholder':'mobile number','class':'form-control'}),'first_name':forms.TextInput(attrs={'placeholder':'first name','class':'form-control'}),'middle_name':forms.TextInput(attrs={'placeholder':'middle name','class':'form-control'}),'last_name':forms.TextInput(attrs={'placeholder':'last name','class':'form-control'}),}


class district_adminform(forms.ModelForm):
	

	file = forms.FileField(required = False)

	class Meta:
		model = district_admin
		fields = ('email','email2','first_name','middle_name','last_name','state','district','mobile','mobile2','address','file')
		widgets = { 'email':forms.TextInput(attrs={'placeholder':'email id','readonly':True, 'class':'form-control'}),'email2':forms.TextInput(attrs={'placeholder':'email id', 'class':'form-control'}),'mobile':forms.TextInput(attrs={'placeholder':'mobile number','class':'form-control'}),'mobile2':forms.TextInput(attrs={'placeholder':'mobile number','class':'form-control'}),'first_name':forms.TextInput(attrs={'placeholder':'first name','readonly':True,'class':'form-control'}),'middle_name':forms.TextInput(attrs={'placeholder':'middle name','readonly':True,'class':'form-control'}),'last_name':forms.TextInput(attrs={'placeholder':'last name','readonly':True,'class':'form-control'}),'address':forms.TextInput(attrs={'placeholder':'address','class':'form-control'}), 'state':forms.TextInput(attrs={'placeholder':'state','readonly':True,'class':'form-control'}),'district':forms.TextInput(attrs={'placeholder':'district','readonly':True,'class':'form-control'}),}



class hospitalform(forms.ModelForm):

	govt = 'Government'
	private = 'Private'

	TYPE_LIST = ((govt,govt),(private,private),)

	
	hospital_type = forms.ChoiceField(choices=TYPE_LIST , required = True, widget=forms.Select(attrs={'class':'form-control'}))
	
	class Meta:
		model = hospital
		fields = ('hospital_id','hospital_name','hospital_type','email','mobile','address','state','district','pincode')
		widgets = {'hospital_id':forms.TextInput(attrs={'placeholder':'hospital id','class':'form-control'}),'hospital_name':forms.TextInput(attrs={'placeholder':'hospital name','class':'form-control'}),'email':forms.TextInput(attrs={'placeholder':'email id','class':'form-control'}),'mobile':forms.TextInput(attrs={'placeholder':'mobile number','class':'form-control'}),'address':forms.TextInput(attrs={'placeholder':'address','class':'form-control'}),'state':forms.TextInput(attrs={'placeholder':'state','readonly':True,'class':'form-control'}),'district':forms.TextInput(attrs={'placeholder':'district','readonly':True,'class':'form-control'}),'pincode':forms.TextInput(attrs={'placeholder':'pin code','class':'form-control'}),}

# def countries():
#     """Get country selections."""
#     return Country.objects.filter(active=True)

# def states_for_country(country=None, translator=_):
#     """
#     Get state selections based on the country parameter.
#     """
#     choices = [('', translator('Not Applicable'))]

#     if country:
#         states = country.state_set.filter(active=True)
#         if states.count() > 0:
#             choices = [('', translator('---Please Select---'))]
#             choices.extend([(state.abbr or state.name, state.name) for state in states])

#     return choices



# class CountryStateForm(forms.ModelForm):
# 	country = forms.ModelChoiceField(queryset=countries(), required=True, label=_('Country'), empty_label=_('---Please Select---'))
# 	state = forms.CharField(max_length=30, required=False, label=_('State/Province'), widget=forms.Select(choices=states_for_country()))

# 	def __init__(self, *args, **kwargs):
# 		super(CountryStateForm, self).__init__(*args, **kwargs)
# 		if self.is_bound:
# 			# if the user has already chosen the country and submitted,
# 			# populate the states/provinces accordingly.

# 			country_obj = self.fields['country'].clean(self.data.get('country'))
# 			state_choices = states_for_country(country_obj)
# 			self.fields['state'] = forms.ChoiceField(label=_('State/Province'), choices=state_choices,required=len(state_choices) > 1)
    
# 	def clean_country(self):
# 		if not self.cleaned_data.get('country'):
# 			raise forms.ValidationError(_('This field is required.'))
# 		return self.cleaned_data['country']

# 	def _check_state(self, data, country):
# 		if country and country.state_set.filter(active=True):
# 			if not data:
# 				raise forms.ValidationError(_('State is required for your country.'))
# 			if (country.state_set.filter(active=True).filter(Q(name__iexact=data) | Q(abbr__iexact=data)).count() != 1):
# 				raise forms.ValidationError(_('Invalid State or Province.'))
    
# 	def clean_state(self):
# 		data = self.cleaned_data.get('state')

# 		country = self.fields['country'].clean(self.data.get('country'))
# 		if country == None:
# 			raise forms.ValidationError(_('This field is required.'))
# 		self._check_state(data, country)

# 		return data