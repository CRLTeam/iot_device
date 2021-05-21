# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin

from app.models import Log, Setting, Simulation, Status

admin.site.register(Log)
admin.site.register(Status)
admin.site.register(Setting)
admin.site.register(Simulation)

#from django.contrib.admin import AdminSite

#from basicdevice.models import Log, Setting, Simulation

#class MyAdminSite(AdminSite):
#    site_header = 'CRL Device Administration'

#admin_site = MyAdminSite(name='myadmin')
##admin_site.register(Log)
