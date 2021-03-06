# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, include  # add this

urlpatterns = [
    path("", include("authentication.urls")), # Auth routes - login / register
    path("", include("app.urls")),             # UI Kits Html files
]
