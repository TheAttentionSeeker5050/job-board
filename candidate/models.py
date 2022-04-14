# from asyncio.windows_events import NULL
from email.policy import default
from django.db import models

# the json decoders and encoders
from django.core.serializers.json import DjangoJSONEncoder
from json import JSONDecoder

# Create your models here.

class Candidate(models.Model):
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
    })

