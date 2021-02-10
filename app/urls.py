# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.contrib import admin
from django.urls import path, re_path, include
from app import views


urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('device/', include('basicdevice.urls')),
    path('admin/', admin.site.urls),          # Django admin route

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),


]
