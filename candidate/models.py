# models and model libs
from django.db import models
from django.contrib.auth.models import User

# the json decoders and encoders
from django.core.serializers.json import DjangoJSONEncoder
from json import JSONDecoder


# Create your models here.

class Candidate(models.Model):
    """This is the candidate profile model linked to the base user model"""
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

    def __str__(self):
        return self.user_id.first_name + " " +  self.user_id.last_name



CV_CAT_CHOICES = [
    ("CV", "CV"),
    ("COVER_LETTER", "Cover letter")
]

class CVUpload(models.Model):
    """This model is for uploading documents like the CV or the cover letter"""

    user_id = models.ForeignKey(User, models.CASCADE, null=True)
    file_category = models.CharField(max_length=25, 
    choices=CV_CAT_CHOICES,
    default="CV")
    file = models.FileField(upload_to="media/uploads/")

