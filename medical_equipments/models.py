from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class userpost(models.Model):

	user_name = models.CharField(max_length = 100 , verbose_name = '')
	name = models.CharField( max_length = 100 ,verbose_name='Name')
	
	def __str__(self):
		return self.user_name


# class userregister(models.Model):

# 	username = models.CharField(max_length = 100 , verbose_name = 'User ID')
# 	name = models.CharField(max_length = 100 , verbose_name = 'Name')
# 	email = models.CharField(max_length = 100 , verbose_name = 'Email')

# 	password1 = models.CharField(max_length = 50, verbose_name='Password1')
# 	password2 = models.CharField(max_length = 50, verbose_name='Password2')

# 	def __str__(self):
# 		return self.user_name
def generate_filename(self, filename):
	url = "files/users/%s/%s/%s" % (self.state,self.mobile ,filename)
	print("file")
	return url

class request_for_state_admin(models.Model):
	
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

	email = models.EmailField(max_length = 100, verbose_name = 'Email ID', unique=True)
	first_name = models.CharField(max_length = 50, verbose_name = 'First Name')
	middle_name = models.CharField(max_length = 50, verbose_name = 'Middle Name', null=True, blank=True)
	last_name = models.CharField(max_length = 50, verbose_name = 'Last Name', null=True, blank=True)
	state = models.CharField(max_length = 30,verbose_name = 'State', choices = STATE_LIST )

	mobile = models.CharField(max_length = 10, verbose_name = 'Mobile No' )

	file = models.FileField(verbose_name = 'Related documents' , upload_to = generate_filename , null=True, blank=True)

	# class Meta:
	# 	unique_together = ('email' , 'state')

	def __str__(self):
		return self.email


# class state_admin(models.Model):
	
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

# 	email = models.EmailField(max_length = 100, verbose_name = 'Email ID', unique=True)
# 	first_name = models.CharField(max_length = 50, verbose_name = 'First Name')
# 	middle_name = models.CharField(max_length = 50, verbose_name = 'Middle Name', null=True, blank=True)
# 	last_name = models.CharField(max_length = 50, verbose_name = 'Last Name', null=True, blank=True)
# 	state = models.CharField(max_length = 30,verbose_name = 'State', choices = STATE_LIST )

# 	mobile = models.CharField(max_length = 10, verbose_name = 'Mobile No' )

# 	file = models.FileField(verbose_name = 'Related documents' , upload_to = generate_filename , null=True, blank=True)

# 	# class Meta:
# 	# 	unique_together = ('email' , 'state')

# 	def __str__(self):
# 		return self.email


# class state_admin(models.Model):
# 	

# class UserProfile(models.Model):
# 	user = models.OneToOneField(User)

# 	email = models.EmailField(max_length = 20,verbose_name="Email ID")
# 	mobile = models.CharField(max_length = 10, verbose_name="Mobile number")
# 	middle_name = models.CharField(max_length = 50, verbose_name = "Middle name", null=True, blank=True)

# User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

# def create_user_profile(sender, instance, created, **kwargs):
# 	if created:
# 		UserProfile.objects.create(user=instance)

# post_save.connect(create_user_profile, sender=User)