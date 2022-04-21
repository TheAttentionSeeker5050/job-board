# from tkinter.ttk import Style
from email.policy import default
from unittest.util import _MAX_LENGTH

# import model and serializer
from rest_framework import serializers
from candidate.models import Candidate, CVUpload, CV_CAT_CHOICES

# import validation tools
from django.contrib.auth.hashers import make_password
from rest_framework.validators import UniqueValidator

class CreateCandidateProfileSerializer(serializers.ModelSerializer):
    """ 
        With this serializer we interact with our rest api at an user (candidate) level
        we added some built-in hashing and password validators
        I am using a custom model view because I am making a custom user (candidate) model
     """

    class Meta:
        model = Candidate
        fields = ("pk", "user_id", "city_of_residence", "state_province", "country")

 


class FileUploadModelSerializer(serializers.ModelSerializer):
    """
        This serializer is in charge of serializing all the file upload requests valid on the ModelSerializer class 
    """
    class Meta:
        model = CVUpload
        fields = ["pk", "user_id", "file_category", "file"]



