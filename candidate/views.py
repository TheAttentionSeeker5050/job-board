from argparse import Action
import json
from django.shortcuts import render

# import some views and models
from rest_framework.views import APIView
from candidate.models import Candidate
from rest_framework.viewsets import ModelViewSet


# import serializers
from candidate.serializers import CreateCandidateProfileSerializer

# some request and response libs
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action


# Create your views here.
class CandidateCustomView(ModelViewSet):
    """ 
        Creates, deletes and updates user instances, retrieves this is a custom view
    """
    queryset = Candidate.objects.all()
    serializer_class = CreateCandidateProfileSerializer

