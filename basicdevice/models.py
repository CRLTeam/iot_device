from django.db import models

class Log(models.Model):
    event_date = models.DateTimeField()
    event = models.TextField()

class Setting(models.Model):
    current = models.TextField()

class Status(models.Model):
    current = models.TextField()

class Simulation(models.Model):
    script = models.TextField()
