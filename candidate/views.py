from argparse import Action
import json
from urllib import response
from django.shortcuts import render

# import some views and models
from rest_framework.views import APIView
from candidate.models import Candidate, CVUpload
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework import generics



# import serializers
from candidate.serializers import CreateCandidateProfileSerializer, FileUploadModelSerializer

# some request and response libs
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

# permissions
from app.permissions import UserIsLoggedIn
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class CandidateCustomView(ModelViewSet):
    """ 
        Creates, deletes and updates user instances, retrieves this is a custom view
    """
    queryset = Candidate.objects.all()
    permission_classes = [UserIsLoggedIn,]
    serializer_class = CreateCandidateProfileSerializer


class FileUploadViewset(ModelViewSet):
    """ 
        Creates, deletes and updates file upload instances, retrieves this is a custom view
    """
    queryset = CVUpload.objects.all()
    serializer_class = FileUploadModelSerializer
    permission_classes = [UserIsLoggedIn,]


    def list(self, request):
        """ List all the files uploaded by user """
        list_of_files = CVUpload.objects.filter(user_id = request.user)
        serializer = self.get_serializer(list_of_files, many=True)
        return Response(serializer.data)


class CandidateBrowseView(generics.ListAPIView):
    """For listing the candidates, allows filters"""


    queryset = Candidate.objects.all()
    permission_classes = [IsAuthenticated,]
    serializer_class = CreateCandidateProfileSerializer

class CandidateRetrieveView(generics.RetrieveAPIView):
    """For retrieving candidates"""
    

    queryset = Candidate.objects.all()
    permission_classes = [IsAuthenticated,]
    serializer_class = CreateCandidateProfileSerializer