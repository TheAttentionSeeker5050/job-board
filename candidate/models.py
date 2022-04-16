# from asyncio.windows_events import NULL
from email.policy import default
# from tkinter import CASCADE
from django.db import models

from django.contrib.auth.models import User

# the json decoders and encoders
from django.core.serializers.json import DjangoJSONEncoder
from json import JSONDecoder

from django.contrib.auth.models import AbstractUser

# Create your models here.

class Candidate(models.Model):
    # email = models.EmailField(unique=True, null=False, default="")
    # username = models.CharField(max_length=45, unique=True, null=False, blank=False)
    # password = models.CharField(max_length=64, null=False, default="")
    user_id = models.ForeignKey(User, models.SET_NULL, null=True, blank=False)
    first_names = models.CharField(max_length=65, default="")
    last_name = models.CharField(max_length=45, default="")
    city_of_residence = models.CharField(max_length=45, default="")
    state_province = models.CharField(max_length=45, default="")
    country = models.CharField(max_length=45, default="")
    work_experience = models.JSONField(encoder=DjangoJSONEncoder, decoder=JSONDecoder, default={
        "company": "",
        "position": "",
        "start_date": "",
        "end_date": "",
    })
    certifications = models.JSONField(encoder=DjangoJSONEncoder, decoder=JSONDecoder, default={

        "certification_name":"",
        "date_of_completion": "",
        "institution": ""
    })

""" class Candidate(models.Model):
    email = models.EmailField(unique=True, null=False, default="")
    username = models.CharField(max_length=45, unique=True, null=False, blank=False)
    password = models.CharField(max_length=64, null=False, default="")
    first_names = models.CharField(max_length=65, default="")
    last_name = models.CharField(max_length=45, default="")
    city_of_residence = models.CharField(max_length=45, default="")
    state_province = models.CharField(max_length=45, default="")
    country = models.CharField(max_length=45, default="")
    work_experience = models.JSONField(encoder=DjangoJSONEncoder, decoder=JSONDecoder, default={
        "company": "",
        "position": "",
        "start_date": "",
        "end_date": "",
    })
    certifications = models.JSONField(encoder=DjangoJSONEncoder, decoder=JSONDecoder, default={

        "certification_name":"",
        "date_of_completion": "",
        "institution": ""
    }) """


CV_CAT_CHOICES = [
    ("CV", "CV"),
    ("COVER_LETTER", "Cover letter")
]

class CVUpload(models.Model):


    candidate = models.ForeignKey(Candidate, models.CASCADE, null=True)
    file_category = models.CharField(max_length=25, 
    choices=CV_CAT_CHOICES,
    default="CV")
    file = models.FileField(upload_to="media/uploads/")
    # file = models.FileField(upload_to="media/uploads/{}/".format(candidate.pk))

