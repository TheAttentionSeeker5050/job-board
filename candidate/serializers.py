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
        fields = ("pk", "user_id", "first_names", "last_name")

    # email = serializers.EmailField(
    #     validators=[UniqueValidator(Candidate.objects.all())]
    #     )
    # username = serializers.CharField(
    #     min_length = 8,
    #     max_length = 45,
    #     allow_null = False,
    #     allow_blank = False,
    #     validators=[UniqueValidator(Candidate.objects.all())]
    #     )
    # password = serializers.CharField(
    #     write_only = True,
    #     required = False,
    #     style = {"input_type": "password", "placeholder": "Password"}
    # )


    # def create(self, validated_data):
    #     validated_data["password"] = make_password(validated_data.get("password"))
    #     candidate = super().create(validated_data)
    #     candidate.save()
    #     return candidate


    # def update(self, instance, validated_data):
    #     fields = ["email", "username", "first_names", "last_name"]
    #     data = {f: validated_data.get(f) for f in fields}
    #     candidate = super().update(instance, data)
    #     candidate.save()
    #     return candidate




class FileUploadModelSerializer(serializers.ModelSerializer):
    """
        This serializer is in charge of serializing all the file upload requests valid on the ModelSerializer class 
    """
    class Meta:
        model = CVUpload
        fields = ["pk", "candidate", "file_category", "file"]
        




# class FileUploadSerializer(serializers.Serializer):
#     # model = CVUpload
#     # fields = ["pk", "candidate", "file_category", "file"]
#     pk = serializers.IntegerField(read_only=True)
#     candidate = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
#     file_category = serializers.ChoiceField(choices=CV_CAT_CHOICES, default= "CV")
#     file = serializers.FileField(use_url=True)
#         # "media/uploads/", recursive=True)

#     def create(self, validated_data):
#         """
#             Create and return a new file upload instance
#         """
#         return CVUpload.objects.create(**validated_data)

