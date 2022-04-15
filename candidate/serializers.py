# from tkinter.ttk import Style
from unittest.util import _MAX_LENGTH

# import model and serializer
from rest_framework import serializers
from candidate.models import Candidate

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
        fields = ("pk","email", "username", "password", "first_names", "last_name")

    email = serializers.EmailField(
        validators=[UniqueValidator(Candidate.objects.all())]
        )
    username = serializers.CharField(
        min_length = 8,
        max_length = 45,
        allow_null = False,
        allow_blank = False,
        validators=[UniqueValidator(Candidate.objects.all())]
        )
    password = serializers.CharField(
        write_only = True,
        required = True,
        style = {"input_type": "password", "placeholder": "Password"}
    )


    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data.get("password"))
        candidate = super().create(validated_data)
        candidate.save()
        return candidate


    def update(self, instance, validated_data):
        candidate = super().update(instance, validated_data)
        try:
            candidate.set_password(validated_data["password"])
            candidate.save()
        except KeyError:
            pass
        return candidate

