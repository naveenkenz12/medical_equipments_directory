from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from django.utils.translation import ugettext_lazy as _

# Create your models here.

class equipment(models.Model):

	yes = 'Yes'
	no = 'No'

	working = 'Working'
	not_working = 'Not Working'

	WORKING_LIST = ((working,working),(not_working,not_working),)

	YES_NO_LIST = ((no,no),(yes,yes),)

	sur = 'Surgical/Operation Theater(OT)'
	lab = 'Laboratory'
	rad = 'radiology'
	den = 'Dental'
	ent = 'ENT'
	ste = 'Sterlization Equipment'
	phy = 'Physiotherapy and Rehabilation'
	eme = 'Emergency'
	end = 'Endoscopy/Laparoscopy'
	car = 'Cardiology'
	blo = 'Blood Bank'
	mat = 'Maternal and Child Care'
	oph = 'Ophthalmology'
	out = 'Out Patient Department(OPD)'
	icu = 'Interiar Care Unit(ICU)'
	oth = 'Others'

	CATEGORY_LIST = ((sur,sur),(lab,lab),(rad,rad),(den,den),(ent,ent),(ste,ste),
					(phy,phy),(eme,eme),(end,end),(car,car),(blo,blo),(mat,mat),
					(oph,oph),(out,out),(icu,icu),(oth,oth),)

	hospital_id = models.CharField(max_length = 100 , verbose_name = 'Hospital ID')
	equipment_id_available = models.CharField(max_length = 3, verbose_name = 'Equipment ID Available', choices=YES_NO_LIST)

	equipment_id = models.CharField(max_length = 100, verbose_name = 'Equipment ID',null=True, blank = True)

	equipment_category = models.CharField(max_length = 40, verbose_name = 'Equipment Category',choices=CATEGORY_LIST)

	equipment_name = models.CharField(max_length = 100, verbose_name = 'Equipment Name')

	equipment_in_warranty = models.CharField(max_length = 3,verbose_name='Warranty Status', choices=YES_NO_LIST)

	warranty_expiry = models.CharField(max_length = 15, verbose_name='Warranty Expiry Date', null=True, blank=True)

	equipment_model = models.CharField(max_length = 100, verbose_name='Equipment Model',null=True, blank=True)

	manufacturar = models.CharField(max_length = 100, verbose_name='Manufacturar', null=True, blank=True)

	installation_date = models.CharField(max_length = 15,verbose_name = 'Date of Installation',null=True, blank=True)

	equipment_under_AMC_CMC = models.CharField(max_length = 3,verbose_name='Under AMC/CMC', choices=YES_NO_LIST)

	amc_upto = models.CharField(max_length = 15,verbose_name='AMC Upto',null=True, blank=True)

	working_condition = models.CharField(max_length = 12,verbose_name='Working Condition',choices=WORKING_LIST)

	not_working_since = models.CharField(max_length = 15,verbose_name='Not Working Since',null=True,blank=True)

	remarks = models.CharField(max_length = 500,verbose_name='Remarks',null=True,blank=True)

	hospital_name = models.CharField( max_length = 250 ,verbose_name='Hospital Name')

	state = models.CharField(max_length = 30, verbose_name = 'State',null=True, blank=True)
	district = models.CharField(max_length = 100, verbose_name = 'District' , null=True, blank=True)
	country = models.CharField(max_length = 100,verbose_name='Country')
	signed = models.CharField(max_length = 100, verbose_name = 'Updated By')

	date_created = models.DateTimeField(auto_now_add = True)

	date_modified = models.DateTimeField(auto_now = True)
	
	class Meta:
		unique_together = ('hospital_id','equipment_id')

	def __str__(self):
		return self.equipment_id

# class change_password(models.Model):

# 	old_password = models.CharField(max_length = 100 , verbose_name = 'Old Password')
# 	new_password1 = models.CharField(max_length = 100, verbose_name = 'New Password')
# 	new_password2 = models.CharField( max_length = 250 ,verbose_name= 'Confirm New Password')


# class userregister(models.Model):

# 	username = models.CharField(max_length = 100 , verbose_name = 'User ID')
# 	name = models.CharField(max_length = 100 , verbose_name = 'Name')
# 	email = models.CharField(max_length = 100 , verbose_name = 'Email')

# 	password1 = models.CharField(max_length = 50, verbose_name='Password1')
# 	password2 = models.CharField(max_length = 50, verbose_name='Password2')

# 	def __str__(self):
# 		return self.user_name

class hospital(models.Model):

	govt = 'Government'
	private = 'Private'

	yes = 'Yes'
	no = 'No'

	primary = 'Primary'
	secondary = 'Secondary'
	tertiary = 'Tertiary'

	TYPE_CAT = ((primary,primary),(secondary,secondary),(tertiary,tertiary),)

	YES_NO_LIST = ((no,no),(yes,yes),)

	TYPE_LIST = ((govt,govt),(private,private),)

	hospital_id_available = models.CharField(max_length = 3, verbose_name = 'Hospital ID', choices=YES_NO_LIST)

	hospital_id = models.CharField(max_length = 100, verbose_name = 'Enter Hospital ID',null=True, blank=True)
	hospital_name = models.CharField(max_length = 250, verbose_name = 'Hospital Name')
	hospital_type = models.CharField(max_length = 50, verbose_name = 'Category' , choices=TYPE_LIST)
	hospital_cat = models.CharField(max_length = 20, verbose_name = 'Hospital Type', choices=TYPE_CAT)
	email = models.EmailField(max_length = 100, verbose_name = 'Email ID')
	mobile = models.CharField(max_length = 10, verbose_name = 'Mobile Number')
	address = models.CharField(max_length = 600, verbose_name = 'Address')
	state = models.CharField(max_length = 30, verbose_name = 'State',null=True, blank=True)
	country = models.CharField(max_length = 100, verbose_name = 'Country')

	district = models.CharField(max_length = 100, verbose_name = 'District',null=True,blank=True)
	pincode = models.CharField(max_length = 12, verbose_name = 'Pin Code/Zip Code')

	def __str__(self):
		return self.hospital_id
	


def generate_filename(self, filename):
	url = "files/users/%s/%s/%s" % (self.state,self.mobile ,filename)
	print("file")
	return url

class request_for_country_admin(models.Model):
	afghanistan = 'Afghanistan'
	albania = 'Albania'
	algeria = 'Algeria'
	andorra = 'Andorra'
	angola = 'Angola'
	antiguaandbarbuda = 'Antigua and Barbuda'
	argentina = 'Argentina'
	armenia = 'Armenia'
	australia = 'Australia'
	austria = 'Austria'
	azerbaijan = 'Azerbaijan'
	bahamas = 'Bahamas'
	bahrain = 'Bahrain'
	bangladesh = 'Bangladesh'
	barbados = 'Barbados'
	belarus = 'Belarus'
	belgium = 'Belgium'
	belize = 'Belize'
	benin = 'Benin'
	bhutan = 'Bhutan'
	bolivia = 'Bolivia'
	bosniaandherzegovina = 'Bosnia and Herzegovina'
	botswana = 'Botswana'
	brazil = 'Brazil'
	brunei = 'Brunei'
	bulgaria = 'Bulgaria'
	burkinafaso = 'Burkina Faso'
	burundi = 'Burundi'
	caboverde = 'Cabo Verde'
	cambodia = 'Cambodia'
	cameroon = 'Cameroon'
	canada = 'Canada'
	centralafricanrepublic = 'Central African Republic'
	chad = 'Chad'
	chile = 'Chile'
	china = 'China'
	colombia = 'Colombia'
	comoros = 'Comoros'
	congorepublicofthe = 'Congo, Republic of the'
	congodemocraticrepublicofthe = 'Congo, Democratic Republic of the'
	costarica = 'Costa Rica'
	cotedivoire = "Cote d'Ivoire"
	croatia = 'Croatia'
	cuba = 'Cuba'
	cyprus = 'Cyprus'
	czechrepublic = 'Czech Republic'
	denmark = 'Denmark'
	djibouti = 'Djibouti'
	dominica = 'Dominica'
	dominicanrepublic = 'Dominican Republic'
	ecuador = 'Ecuador'
	egypt = 'Egypt'
	elsalvador = 'El Salvador'
	equatorialguinea = 'Equatorial Guinea'
	eritrea = 'Eritrea'
	estonia = 'Estonia'
	ethiopia = 'Ethiopia'
	fiji = 'Fiji'
	finland = 'Finland'
	france = 'France'
	gabon = 'Gabon'
	gambia = 'Gambia'
	georgia = 'Georgia'
	germany = 'Germany'
	ghana = 'Ghana'
	greece = 'Greece'
	grenada = 'Grenada'
	guatemala = 'Guatemala'
	guinea = 'Guinea'
	guineabissau = 'Guinea-Bissau'
	guyana = 'Guyana'
	haiti = 'Haiti'
	honduras = 'Honduras'
	hungary = 'Hungary'
	iceland = 'Iceland'
	indonesia = 'Indonesia'
	iran = 'Iran'
	iraq = 'Iraq'
	ireland = 'Ireland'
	israel = 'Israel'
	italy = 'Italy'
	jamaica = 'Jamaica'
	japan = 'Japan'
	jordan = 'Jordan'
	kazakhstan = 'Kazakhstan'
	kenya = 'Kenya'
	kiribati = 'Kiribati'
	kosovo = 'Kosovo'
	kuwait = 'Kuwait'
	kyrgyzstan = 'Kyrgyzstan'
	laos = 'Laos'
	latvia = 'Latvia'
	lebanon = 'Lebanon'
	lesotho = 'Lesotho'
	liberia = 'Liberia'
	libya = 'Libya'
	liechtenstein = 'Liechtenstein'
	lithuania = 'Lithuania'
	luxembourg = 'Luxembourg'
	macedonia = 'Macedonia'
	madagascar = 'Madagascar'
	malawi = 'Malawi'
	malaysia = 'Malaysia'
	maldives = 'Maldives'
	mali = 'Mali'
	malta = 'Malta'
	marshallislands = 'Marshall Islands'
	mauritania = 'Mauritania'
	mauritius = 'Mauritius'
	mexico = 'Mexico'
	micronesia = 'Micronesia'
	moldova = 'Moldova'
	monaco = 'Monaco'
	mongolia = 'Mongolia'
	montenegro = 'Montenegro'
	morocco = 'Morocco'
	mozambique = 'Mozambique'
	myanmarburma = 'Myanmar (Burma)'
	namibia = 'Namibia'
	nauru = 'Nauru'
	nepal = 'Nepal'
	netherlands = 'Netherlands'
	newzealand = 'New Zealand'
	nicaragua = 'Nicaragua'
	niger = 'Niger'
	nigeria = 'Nigeria'
	northkorea = 'North Korea'
	norway = 'Norway'
	oman = 'Oman'
	pakistan = 'Pakistan'
	palau = 'Palau'
	palestine = 'Palestine'
	panama = 'Panama'
	papuanewguinea = 'Papua New Guinea'
	paraguay = 'Paraguay'
	peru = 'Peru'
	philippines = 'Philippines'
	poland = 'Poland'
	portugal = 'Portugal'
	qatar = 'Qatar'
	romania = 'Romania'
	russia = 'Russia'
	rwanda = 'Rwanda'
	stkittsandnevis = 'St. Kitts and Nevis '
	stlucia = 'St. Lucia'
	stvincentandthegrenadines = 'St. Vincent and The Grenadines '
	samoa = 'Samoa'
	sanmarino = 'San Marino'
	saotomeandprincipe = 'Sao Tome and Principe '
	saudiarabia = 'Saudi Arabia'
	senegal = 'Senegal'
	serbia = 'Serbia'
	seychelles = 'Seychelles'
	sierraleone = 'Sierra Leone'
	singapore = 'Singapore'
	slovakia = 'Slovakia'
	slovenia = 'Slovenia'
	solomonislands = 'Solomon Islands'
	somalia = 'Somalia'
	southafrica = 'South Africa'
	southkorea = 'South Korea'
	southsudan = 'South Sudan'
	spain = 'Spain'
	srilanka = 'Sri Lanka'
	sudan = 'Sudan'
	suriname = 'Suriname'
	swaziland = 'Swaziland'
	sweden = 'Sweden'
	switzerland = 'Switzerland'
	syria = 'Syria'
	taiwan = 'Taiwan'
	tajikistan = 'Tajikistan'
	tanzania = 'Tanzania'
	thailand = 'Thailand'
	timorleste = 'Timor-Leste'
	togo = 'Togo'
	tonga = 'Tonga'
	trinidadandtobago = 'Trinidad and Tobago'
	tunisia = 'Tunisia'
	turkey = 'Turkey'
	turkmenistan = 'Turkmenistan'
	tuvalu = 'Tuvalu'
	uganda = 'Uganda'
	ukraine = 'Ukraine'
	unitedarabemirates = 'United Arab Emirates'
	unitedkingdomuk = 'United Kingdom (UK)'
	unitedstatesofamericausa = 'United States of America (USA)'
	uruguay = 'Uruguay'
	uzbekistan = 'Uzbekistan'
	vanuatu = 'Vanuatu'
	vaticancityholysee = 'Vatican City (Holy See)'
	venezuela = 'Venezuela'
	vietnam = 'Vietnam'
	yemen = 'Yemen'
	zambia = 'Zambia'
	zimbabwe = 'Zimbabwe'
	

	n_a = 'N/A'
	male = 'Male'
	female = 'Female'

	post_graduate = 'POST_GRADUATE'
	graduate = 'Graduate'
	vocational = 'Vocational'
	higher_secondary = 'Higher Secondary'
	secondary = 'Secondary'
	elementary = 'Elementary'

	EDUCATION_LIST = ((post_graduate,post_graduate),(graduate,graduate),(vocational,vocational),(higher_secondary,higher_secondary),(secondary,secondary),(elementary,elementary),)

	GENDER_LIST = ((n_a,n_a),(male,male),(female,female),)

	COUNTRY_LIST = ((afghanistan,afghanistan),(albania,albania),(algeria,algeria),(andorra,andorra),(angola,angola),(antiguaandbarbuda,antiguaandbarbuda),(argentina,argentina),(armenia,armenia),(australia,australia),(austria,austria),(azerbaijan,azerbaijan),(bahamas,bahamas),(bahrain,bahrain),(bangladesh,bangladesh),(barbados,barbados),(belarus,belarus),(belgium,belgium),(belize,belize),(benin,benin),(bhutan,bhutan),(bolivia,bolivia),(bosniaandherzegovina,bosniaandherzegovina),(botswana,botswana),(brazil,brazil),(brunei,brunei),(bulgaria,bulgaria),(burkinafaso,burkinafaso),(burundi,burundi),(caboverde,caboverde),(cambodia,cambodia),(cameroon,cameroon),(canada,canada),(centralafricanrepublic,centralafricanrepublic),(chad,chad),(chile,chile),(china,china),(colombia,colombia),(comoros,comoros),(congorepublicofthe,congorepublicofthe),(congodemocraticrepublicofthe,congodemocraticrepublicofthe),(costarica,costarica),(cotedivoire,cotedivoire),(croatia,croatia),(cuba,cuba),(cyprus,cyprus),(czechrepublic,czechrepublic),(denmark,denmark),(djibouti,djibouti),(dominica,dominica),(dominicanrepublic,dominicanrepublic),(ecuador,ecuador),(egypt,egypt),(elsalvador,elsalvador),(equatorialguinea,equatorialguinea),(eritrea,eritrea),(estonia,estonia),(ethiopia,ethiopia),(fiji,fiji),(finland,finland),(france,france),(gabon,gabon),(gambia,gambia),(georgia,georgia),(germany,germany),(ghana,ghana),(greece,greece),(grenada,grenada),(guatemala,guatemala),(guinea,guinea),(guineabissau,guineabissau),(guyana,guyana),(haiti,haiti),(honduras,honduras),(hungary,hungary),(iceland,iceland),(indonesia,indonesia),(iran,iran),(iraq,iraq),(ireland,ireland),(israel,israel),(italy,italy),(jamaica,jamaica),(japan,japan),(jordan,jordan),(kazakhstan,kazakhstan),(kenya,kenya),(kiribati,kiribati),(kosovo,kosovo),(kuwait,kuwait),(kyrgyzstan,kyrgyzstan),(laos,laos),(latvia,latvia),(lebanon,lebanon),(lesotho,lesotho),(liberia,liberia),(libya,libya),(liechtenstein,liechtenstein),(lithuania,lithuania),(luxembourg,luxembourg),(macedonia,macedonia),(madagascar,madagascar),(malawi,malawi),(malaysia,malaysia),(maldives,maldives),(mali,mali),(malta,malta),(marshallislands,marshallislands),(mauritania,mauritania),(mauritius,mauritius),(mexico,mexico),(micronesia,micronesia),(moldova,moldova),(monaco,monaco),(mongolia,mongolia),(montenegro,montenegro),(morocco,morocco),(mozambique,mozambique),(myanmarburma,myanmarburma),(namibia,namibia),(nauru,nauru),(nepal,nepal),(netherlands,netherlands),(newzealand,newzealand),(nicaragua,nicaragua),(niger,niger),(nigeria,nigeria),(northkorea,northkorea),(norway,norway),(oman,oman),(pakistan,pakistan),(palau,palau),(palestine,palestine),(panama,panama),(papuanewguinea,papuanewguinea),(paraguay,paraguay),(peru,peru),(philippines,philippines),(poland,poland),(portugal,portugal),(qatar,qatar),(romania,romania),(russia,russia),(rwanda,rwanda),(stkittsandnevis,stkittsandnevis),(stlucia,stlucia),(stvincentandthegrenadines,stvincentandthegrenadines),(samoa,samoa),(sanmarino,sanmarino),(saotomeandprincipe,saotomeandprincipe),(saudiarabia,saudiarabia),(senegal,senegal),(serbia,serbia),(seychelles,seychelles),(sierraleone,sierraleone),(singapore,singapore),(slovakia,slovakia),(slovenia,slovenia),(solomonislands,solomonislands),(somalia,somalia),(southafrica,southafrica),(southkorea,southkorea),(southsudan,southsudan),(spain,spain),(srilanka,srilanka),(sudan,sudan),(suriname,suriname),(swaziland,swaziland),(sweden,sweden),(switzerland,switzerland),(syria,syria),(taiwan,taiwan),(tajikistan,tajikistan),(tanzania,tanzania),(thailand,thailand),(timorleste,timorleste),(togo,togo),(tonga,tonga),(trinidadandtobago,trinidadandtobago),(tunisia,tunisia),(turkey,turkey),(turkmenistan,turkmenistan),(tuvalu,tuvalu),(uganda,uganda),(ukraine,ukraine),(unitedarabemirates,unitedarabemirates),(unitedkingdomuk,unitedkingdomuk),(unitedstatesofamericausa,unitedstatesofamericausa),(uruguay,uruguay),(uzbekistan,uzbekistan),(vanuatu,vanuatu),(vaticancityholysee,vaticancityholysee),(venezuela,venezuela),(vietnam,vietnam),(yemen,yemen),(zambia,zambia),(zimbabwe,zimbabwe),)

	email = models.EmailField(max_length = 100, verbose_name = 'Email ID', unique=True)
	first_name = models.CharField(max_length = 50, verbose_name = 'First Name')
	middle_name = models.CharField(max_length = 50, verbose_name = 'Middle Name', null=True, blank=True)
	last_name = models.CharField(max_length = 50, verbose_name = 'Last Name', null=True, blank=True)
	country = models.CharField(max_length = 50,verbose_name = 'Country', choices = COUNTRY_LIST )

	agex = models.DecimalField(max_digits = 3, decimal_places = 0, verbose_name = 'Age')

	gender = models.CharField(max_length = 6,verbose_name = 'Gender' , choices = GENDER_LIST)

	education = models.CharField(max_length = 50, verbose_name = 'Education' , choices = EDUCATION_LIST)

	mobile = models.CharField(max_length = 10, verbose_name = 'Mobile No' )

	file = models.FileField(verbose_name = 'Related documents' , upload_to = generate_filename , null=True, blank=True)

	# class Meta:
	# 	unique_together = ('email' , 'state')

	def __str__(self):
		return self.email

class country_admin(models.Model):
	
	email = models.EmailField(max_length = 100, verbose_name = 'Email ID/Username', unique=True)
	email2 = models.EmailField(max_length = 100, verbose_name = 'Alternate Email ID' , null =True, blank = True)
	first_name = models.CharField(max_length = 50, verbose_name = 'First Name')
	middle_name = models.CharField(max_length = 50, verbose_name = 'Middle Name', null=True, blank=True)
	last_name = models.CharField(max_length = 50, verbose_name = 'Last Name', null=True, blank=True)
	country = models.CharField(max_length = 50,verbose_name = 'Country' )

	mobile = models.CharField(max_length = 10, verbose_name = 'Mobile No' )
	mobile2 = models.CharField(max_length = 10, verbose_name = 'Alernate Mobile No', null=True, blank=True)

	agex = models.DecimalField(max_digits = 3, decimal_places = 0, verbose_name = 'Age')

	gender = models.CharField(max_length = 6,verbose_name = 'Gender')

	education = models.CharField(max_length = 50, verbose_name = 'Education')

	address = models.CharField(max_length = 500, verbose_name= 'Address' , null=True, blank=True)

	file = models.FileField(verbose_name = 'Related documents' , upload_to = generate_filename , null=True, blank=True)

	# class Meta:
	# 	unique_together = ('email' , 'state')

	def __str__(self):
		return self.email

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

	india = 'India'

	COUNTRY_LIST = ((india,india),)

	n_a = 'N/A'
	male = 'Male'
	female = 'Female'

	post_graduate = 'POST_GRADUATE'
	graduate = 'Graduate'
	vocational = 'Vocational'
	higher_secondary = 'Higher Secondary'
	secondary = 'Secondary'
	elementary = 'Elementary'

	EDUCATION_LIST = ((post_graduate,post_graduate),(graduate,graduate),(vocational,vocational),(higher_secondary,higher_secondary),(secondary,secondary),(elementary,elementary),)

	GENDER_LIST = ((n_a,n_a),(male,male),(female,female),)

	STATE_LIST = ((andaman,andaman),(andhra,andhra),(arunachal,arunachal),(assam,assam),(bihar,bihar),(chandigarh,chandigarh),(chattisgarh,chattisgarh),(dadra,dadra),(daman,daman),(delhi,delhi),(goa,goa),(gujrat,gujrat),(haryana,haryana),(himachal,himachal),(jammu,jammu),(jharkhand,jharkhand),(karnataka,karnataka),(kerala,kerala),(lakshadweep,lakshadweep),(madhya,madhya),(maharashtra,maharashtra),(manipur,manipur),(meghalaya,meghalaya),(mizoram,mizoram),(nagaland,nagaland),(odisha,odisha),(puducherry,puducherry),(punjab,punjab),(rajasthan,rajasthan),(sikkim,sikkim),(tamil,tamil),(telangana,telangana),(tripura,tripura),(uttar,uttar),(uttarakhand,uttarakhand),(west,west),)

	email = models.EmailField(max_length = 100, verbose_name = 'Email ID', unique=True)
	first_name = models.CharField(max_length = 50, verbose_name = 'First Name')
	middle_name = models.CharField(max_length = 50, verbose_name = 'Middle Name', null=True, blank=True)
	last_name = models.CharField(max_length = 50, verbose_name = 'Last Name', null=True, blank=True)
	country = models.CharField(max_length = 10, verbose_name = 'Country', choices = COUNTRY_LIST)
	state = models.CharField(max_length = 30,verbose_name = 'State', choices = STATE_LIST )

	agex = models.DecimalField(max_digits = 3, decimal_places = 0, verbose_name = 'Age')

	gender = models.CharField(max_length = 6,verbose_name = 'Gender' , choices = GENDER_LIST)

	education = models.CharField(max_length = 50, verbose_name = 'Education' , choices = EDUCATION_LIST)

	mobile = models.CharField(max_length = 10, verbose_name = 'Mobile No' )

	file = models.FileField(verbose_name = 'Related documents' , upload_to = generate_filename , null=True, blank=True)

	# class Meta:
	# 	unique_together = ('email' , 'state')

	def __str__(self):
		return self.email


class state_admin(models.Model):
	
	email = models.EmailField(max_length = 100, verbose_name = 'Email ID/Username', unique=True)
	email2 = models.EmailField(max_length = 100, verbose_name = 'Alternate Email ID' , null =True, blank = True)
	first_name = models.CharField(max_length = 50, verbose_name = 'First Name')
	middle_name = models.CharField(max_length = 50, verbose_name = 'Middle Name', null=True, blank=True)
	last_name = models.CharField(max_length = 50, verbose_name = 'Last Name', null=True, blank=True)
	country = models.CharField(max_length = 10,verbose_name = 'Country' )
	
	state = models.CharField(max_length = 30,verbose_name = 'State' )

	mobile = models.CharField(max_length = 10, verbose_name = 'Mobile No' )
	mobile2 = models.CharField(max_length = 10, verbose_name = 'Alernate Mobile No', null=True, blank=True)

	agex = models.DecimalField(max_digits = 3, decimal_places = 0, verbose_name = 'Age')

	gender = models.CharField(max_length = 6,verbose_name = 'Gender')

	education = models.CharField(max_length = 50, verbose_name = 'Education')

	address = models.CharField(max_length = 500, verbose_name= 'Address' , null=True, blank=True)

	file = models.FileField(verbose_name = 'Related documents' , upload_to = generate_filename , null=True, blank=True)

	# class Meta:
	# 	unique_together = ('email' , 'state')

	def __str__(self):
		return self.email


class request_for_district_admin(models.Model):
	
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
	
	n_a = 'N/A'
	male = 'Male'
	female = 'Female'

	india = 'India'

	COUNTRY_LIST = ((india,india),)

	post_graduate = 'POST_GRADUATE'
	graduate = 'Graduate'
	vocational = 'Vocational'
	higher_secondary = 'Higher Secondary'
	secondary = 'Secondary'
	elementary = 'Elementary'

	EDUCATION_LIST = ((post_graduate,post_graduate),(graduate,graduate),(vocational,vocational),(higher_secondary,higher_secondary),(secondary,secondary),(elementary,elementary),)

	GENDER_LIST = ((n_a,n_a),(male,male),(female,female),)
	
	
	email = models.EmailField(max_length = 100, verbose_name = 'Email ID', unique=True)
	first_name = models.CharField(max_length = 50, verbose_name = 'First Name')
	middle_name = models.CharField(max_length = 50, verbose_name = 'Middle Name', null=True, blank=True)
	last_name = models.CharField(max_length = 50, verbose_name = 'Last Name', null=True, blank=True)
	country = models.CharField(max_length = 10,verbose_name = 'Country', choices = COUNTRY_LIST )
	
	state = models.CharField(max_length = 30,verbose_name = 'State', choices = STATE_LIST )

	district = models.CharField(max_length = 30,verbose_name = 'District', choices = DISTRICT_LIST )

	mobile = models.CharField(max_length = 10, verbose_name = 'Mobile No' )

	agex = models.DecimalField(max_digits = 3, decimal_places = 0, verbose_name = 'Age')

	gender = models.CharField(max_length = 6,verbose_name = 'Gender' , choices = GENDER_LIST)

	education = models.CharField(max_length = 50, verbose_name = 'Education' , choices = EDUCATION_LIST)

	file = models.FileField(verbose_name = 'Related documents' , upload_to = generate_filename , null=True, blank=True)

	# class Meta:
	# 	unique_together = ('email' , 'state')

	def __str__(self):
		return self.email


class district_admin(models.Model):
	
	email = models.EmailField(max_length = 100, verbose_name = 'Email ID/Username', unique=True)
	email2 = models.EmailField(max_length = 100, verbose_name = 'Alternate Email ID' , null =True, blank = True)
	first_name = models.CharField(max_length = 50, verbose_name = 'First Name')
	middle_name = models.CharField(max_length = 50, verbose_name = 'Middle Name', null=True, blank=True)
	last_name = models.CharField(max_length = 50, verbose_name = 'Last Name', null=True, blank=True)
	country = models.CharField(max_length = 10,verbose_name = 'Country' )
	
	state = models.CharField(max_length = 30,verbose_name = 'State' )
	district = models.CharField(max_length = 100, verbose_name = 'District')

	mobile = models.CharField(max_length = 10, verbose_name = 'Mobile No' )
	mobile2 = models.CharField(max_length = 10, verbose_name = 'Alernate Mobile No', null=True, blank=True)

	agex = models.DecimalField(max_digits = 3, decimal_places = 0, verbose_name = 'Age')

	gender = models.CharField(max_length = 6,verbose_name = 'Gender' )

	education = models.CharField(max_length = 50, verbose_name = 'Education' )

	address = models.CharField(max_length = 500, verbose_name= 'Address' , null=True, blank=True)

	file = models.FileField(verbose_name = 'Related documents' , upload_to = generate_filename , null=True, blank=True)

	# class Meta:
	# 	unique_together = ('email' , 'state')

	def __str__(self):
		return self.email



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

# CONTINENTS = (
#     ('AF', _('Africa')),
#     ('NA', _('North America')),
#     ('EU',  _('Europe')),
#     ('AS', _('Asia')),
#     ('OC',  _('Oceania')),
#     ('SA', _('South America')),
#     ('AN', _('Antarctica'))
# )


# class Country(models.Model):
# 	iso2_code = models.CharField(_('ISO alpha-2'), max_length=2, unique=True)
# 	name = models.CharField(_('Official name (CAPS)'), max_length=128)
# 	printable_name = models.CharField(_('Country name'), max_length=128)
# 	iso3_code = models.CharField(_('ISO alpha-3'), max_length=3, unique=True)
# 	numcode = models.PositiveSmallIntegerField(_('ISO numeric'), null=True, blank=True)
# 	continent = models.CharField(_('Continent'), choices=CONTINENTS, max_length=2)
# 	active = models.BooleanField(_('Country is active'), default=True)

# 	class Meta:
# 		verbose_name = _('Country')
# 		verbose_name_plural = _('Countries')
# 		ordering = ('name',)

# 	def __unicode__(self):
# 		return self.printable_name


# class State(models.Model):
# 	country = models.ForeignKey(Country)
# 	name = models.CharField(_('State/Province name'), max_length=60)
# 	abbr = models.CharField(_('State/Province Abbreviation'), max_length=3, null=True, blank=True)
# 	active = models.BooleanField(_('State/Province is active'), default=True)

# 	class Meta:
# 		verbose_name = _('State/Province')
# 		verbose_name_plural = _('States/Provinces')
# 		ordering= ('name',)

# 	def __unicode__(self):
# 		return self.name


