from argparse import Action
import json
from urllib import response
from django.shortcuts import render

# import some views and models
from rest_framework.views import APIView
from candidate.models import Candidate, CVUpload
from rest_framework.viewsets import ModelViewSet, ViewSet



# import serializers
from candidate.serializers import CreateCandidateProfileSerializer, FileUploadModelSerializer

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


class FileUploadViewset(ModelViewSet):
    """ 
        Creates, deletes and updates file upload instances, retrieves this is a custom view
    """
    queryset = CVUpload.objects.all()
    serializer_class = FileUploadModelSerializer


# class FileUploadView(APIView):
#     """
#         A viewset to upload files and retrieve a list of them as the proprietor of the file
#     """
#     def get(self, request, format=None):
#         files = CVUpload.objects.all()
#         serializer = FileUploadSerializer(files, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         # file = request.data.get("file")
#         serializer = FileUploadSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status= status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class FileDetailView(APIView):
#     """
#         Retrieve, update and delete a file
#     """

#     def get_object(self, pk):
#         try:
#             return CVUpload.objects.get(pk=pk)
#         except CVUpload.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         file = self.get_object(pk)
#         serializer = FileUploadSerializer(file)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         file = self.get_object(pk)
#         serializer = FileUploadSerializer(file, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         file = self.get_object(pk)
#         file.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)