from django.db import models
from django.contrib import admin

# Create your models here.

class Participantlist(models.Model):

    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    Age = models.CharField(max_length=100)

class ParticipantlistAdmin(admin.ModelAdmin):
    list_Participant = ('name','email','phone','age')
