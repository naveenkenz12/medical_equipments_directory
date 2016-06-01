from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Register your models here.

from medical_equipments.models import userpost
from medical_equipments.models import request_for_state_admin

import csv

from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.utils.translation import ugettext_lazy as _

class userpostadmin(admin.ModelAdmin):
	class meta:
		model = userpost

admin.site.register(userpost,userpostadmin)


class state_adminregisteradmin(admin.ModelAdmin):
	class meta:
		model = request_for_state_admin

admin.site.register(request_for_state_admin,state_adminregisteradmin)


# admin.site.unregister(User)

# class register_useradmin(UserAdmin):
# 	add_fieldsets = (
# 		(None,{
# 			'classes': ('wide',),
# 			'fields': ('username', 'email', 'first_name' , 'middle_name' , 'password1', 'password2')}
# 			),
# 		)

# admin.site.register(User, register_useradmin)