# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

class Log(models.Model):
    event_date = models.DateTimeField()
    event = models.TextField()

class Setting(models.Model):
    current = models.TextField()

class Status(models.Model):
    current = models.TextField()

class Simulation(models.Model):
    script = models.TextField()

