"""medical_equipments_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from medical_equipments_django import settings


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$' , 'medical_equipments.views.create_admin' , name = 'index'),

    ### added
    url(r'^home/$' , 'medical_equipments.views.index' , name = 'index'),


    url(r'^summary/' , 'medical_equipments.views.summary' , name = 'summary'),

    url(r'^contact_us/' , 'medical_equipments.views.contact_us' , name = 'contact_us'),

    url(r'^medical_equipments_form/$', 'medical_equipments.views.medical_equipments_form', name='medical_equipments_form'),

    url(r'^login/$' , 'medical_equipments.views.login' , name = 'medical_equipments_form' ),

    url(r'^logout/$' , 'medical_equipments.views.logout' , name = 'medical_equipments_form' ),

    #url(r'^register/' , 'medical_equipments.views.register' , name = 'register'),

    url(r'^authorized/' , 'medical_equipments.views.authorized_view' , name = 'authorized_view'),

    url(r'^user/' , 'medical_equipments.views.user' , name = 'user'),
    
    url(r'^request_sent/' , 'medical_equipments.views.request_sent' , name = 'request'),

    #url(r'^invalid_request/' , 'medical_equipments.views.invalid_request' , name = 'invalid'),

    url(r'^admin_register_form/state/' , 'medical_equipments.views.state_admin_register_form' , name = 'state_admin_register_form'),

    url(r'^admin_register_form/country/' , 'medical_equipments.views.country_admin_register_form' , name = 'country_admin_register_form'),

    url(r'^admin_register_form/district/' , 'medical_equipments.views.district_admin_register_form' , name = 'district_admin_register_form'),

    url(r'^state_requests/' , 'medical_equipments.views.state_requests' , name = 'state_requests'),

    url(r'^country_requests/' , 'medical_equipments.views.country_requests' , name = 'country_requests'),

    url(r'^district_requests/' , 'medical_equipments.views.district_requests' , name = 'district_requests'),

    

    url(r'^district_approve/$' , 'medical_equipments.views.district_approve' , name = 'approve'),

    url(r'^district_reject/$' , 'medical_equipments.views.district_reject' , name = 'reject'),

    url(r'^state_approve/$' , 'medical_equipments.views.state_approve' , name = 'approve'),

    url(r'^state_reject/$' , 'medical_equipments.views.state_reject' , name = 'reject'),

    url(r'^country_approve/$' , 'medical_equipments.views.country_approve' , name = 'approve'),

    url(r'^country_reject/$' , 'medical_equipments.views.country_reject' , name = 'reject'),

    url(r'^state_admin/' , 'medical_equipments.views.show_state_admin' , name = 'state_admin'),

    url(r'^country_admin/' , 'medical_equipments.views.show_country_admin' , name = 'country_admin'),
    
    url(r'^district_admin/' , 'medical_equipments.views.show_district_admin' , name = 'district_admin'),

    url(r'^state_remove/$' , 'medical_equipments.views.state_remove' , name = 'state_remove'),

    url(r'^country_remove/$' , 'medical_equipments.views.country_remove' , name = 'country_remove'),

    url(r'^district_remove/$' , 'medical_equipments.views.district_remove' , name = 'district_remove'),

    url(r'^register_hospital/' , 'medical_equipments.views.register_hospital' , name = 'register_hospital'),

    url(r'^current_hospital/' , 'medical_equipments.views.current_hospital' , name = 'current_hospital'),

    url(r'^change_password/' , 'medical_equipments.views.change_password' , name = 'change_password'),

    #url(r'^captcha/', include('captcha.urls')),

    url(r'^forgot_password/' , 'medical_equipments.views.forgot_password' , name = 'forgot_password'),

    url(r'^see_equipments/$' , 'medical_equipments.views.see_equipments' , name = 'see_equipments'),

    url(r'^hospital_equipments/$' , 'medical_equipments.views.hospital_equipments' , name = 'see_equipments'),

    url(r'^equipments/district/$' , 'medical_equipments.views.district_equipments' , name = 'district_equipments'),

    url(r'^equipments/state/$' , 'medical_equipments.views.state_equipments' , name = 'state_equipments'),

    url(r'^equipments/all/' , 'medical_equipments.views.all_equipments' , name = 'all_equipments'),

    url(r'^equipment_view/$' , 'medical_equipments.views.equipment_view' , name = 'equipment_view' ),

    url(r'^hospital_view/$' , 'medical_equipments.views.hospital_view' , name = 'hospital_view' ),

    url(r'^registration/hospital/success/$' , 'medical_equipments.views.valid_hospital_registration' , name = 'Success' ),

    url(r'^registration/equipment/success/$' , 'medical_equipments.views.valid_equipment_registration' , name = 'Success' ),

    url(r'^state_hospital/$' , 'medical_equipments.views.state_hospital' , name = 'state_hospital'),

    url(r'^all_hospital/' , 'medical_equipments.views.all_hospital' , name = 'all_hospital'),

    url(r'^equipment_query/' , 'medical_equipments.views.equipment_query' , name = 'Search'),

    url(r'^show_country/$' , 'medical_equipments.views.show_country' , name = 'summary'),

    url(r'^show_state/$' , 'medical_equipments.views.show_state' , name = 'summary'),

    url(r'^show_district/$' , 'medical_equipments.views.show_district' , name = 'summary'),

    url(r'^show_hospital/$' , 'medical_equipments.views.show_hospital' , name = 'summary'),

    url(r'^summary_india/' , 'medical_equipments.views.summary_india' , name = 'summary'),

    url(r'^summary_India/' , 'medical_equipments.views.summary_india' , name = 'summary'),

    url(r'^summary_country/$' , 'medical_equipments.views.summary_country' , name = 'summary'),

    url(r'^summary_state/$' , 'medical_equipments.views.summary_state' , name = 'summary'),

    url(r'^summary_district/$' , 'medical_equipments.views.summary_district' , name = 'summary'),

    url(r'^summary_hospital/$' , 'medical_equipments.views.summary_hospital' , name = 'summary'),

    #url(r'^map/' , 'medical_equipments.views.map' , name = 'map'),

    url(r'^upload/' , 'medical_equipments.views.upload_file' , name = 'file'),

    url(r'^success/' , 'medical_equipments.views.success' , name = 'success'),

    url(r'^download/$' , 'medical_equipments.views.download' , name = 'download'),

    url(r'^register_select/$' , 'medical_equipments.views.register_select' , name = 'register'),

    url(r'^feedback/$' , 'medical_equipments.views.feedback' , name = 'feedback'),

    url(r'^maintain/1/add/$' , 'medical_equipments.views.add_country' , name = 'maintain'),
    url(r'^maintain/2/add/$' , 'medical_equipments.views.add_state' , name = 'maintain'),
    url(r'^maintain/3/add/$' , 'medical_equipments.views.add_district' , name = 'maintain'),
    url(r'^maintain/1/delete/$' , 'medical_equipments.views.delete_country' , name = 'maintain'),
    url(r'^maintain/2/delete/$' , 'medical_equipments.views.delete_state' , name = 'maintain'),
    url(r'^maintain/3/delete/$' , 'medical_equipments.views.delete_district' , name = 'maintain'),

    url(r'^settings/$' , 'medical_equipments.views.setting' , name = 'maintain'),

    url(r'^register_new/' , 'medical_equipments.views.register_new' , name = 'register'),

    url(r'^db/' , 'medical_equipments.views.db' , name = 'register'),
    url(r'^bems_offline/' , 'medical_equipments.views.bems_offline' , name = 'offline'),
    url(r'^instruction/' , 'medical_equipments.views.instruction' , name = 'help'),
#
    #url(r'^view_hospital/$' , 'medical_equipments.views.view_hospital' , name = 'equipments'),


    #url(r'^home2/' , 'medical_equipments.views.home2' , name = 'home2'),    
    
    #url(r'^countries_states/$', 'countries_states.views.countries_states_view', name='countries-states'),

    #url(r'^ajax_populate_states/$', 'countries_states.views.ajax_populate_states', name='populate-states'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += patterns('',(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),)

urlpatterns += patterns('',(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),)

admin.site.site_header = 'Biomedical Equipments Management System'
