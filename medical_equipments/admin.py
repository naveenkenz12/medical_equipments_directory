from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Register your models here.

from medical_equipments.models import equipment
from medical_equipments.models import request_for_state_admin
from medical_equipments.models import request_for_district_admin
from medical_equipments.models import request_for_country_admin


from medical_equipments.models import state_admin
from medical_equipments.models import district_admin
from medical_equipments.models import country_admin
from medical_equipments.models import hospital


import csv

from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.utils.translation import ugettext_lazy as _

class equipmentadmin(admin.ModelAdmin):
	class meta:
		model = equipment

admin.site.register(equipment,equipmentadmin)

class country_adminregisteradmin(admin.ModelAdmin):
	class meta:
		model = request_for_country_admin

admin.site.register(request_for_country_admin,country_adminregisteradmin)

class state_adminregisteradmin(admin.ModelAdmin):
	class meta:
		model = request_for_state_admin

admin.site.register(request_for_state_admin,state_adminregisteradmin)

class district_adminregisteradmin(admin.ModelAdmin):
	class meta:
		model = request_for_district_admin

admin.site.register(request_for_district_admin,district_adminregisteradmin)

class country_adminadmin(admin.ModelAdmin):
	class meta:
		model = country_admin

admin.site.register(country_admin,country_adminadmin)

class state_adminadmin(admin.ModelAdmin):
	class meta:
		model = state_admin

admin.site.register(state_admin,state_adminadmin)


class district_adminadmin(admin.ModelAdmin):
	class meta:
		model = district_admin

admin.site.register(district_admin,district_adminadmin)

class hospitaladmin(admin.ModelAdmin):
	class meta:
		model = hospital

admin.site.register(hospital,hospitaladmin)


# admin.site.unregister(User)

# class register_useradmin(UserAdmin):
# 	add_fieldsets = (
# 		(None,{
# 			'classes': ('wide',),
# 			'fields': ('username', 'email', 'first_name' , 'middle_name' , 'password1', 'password2')}
# 			),
# 		)

# admin.site.register(User, register_useradmin)