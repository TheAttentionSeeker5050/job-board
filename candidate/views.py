from argparse import Action
import json
from django.shortcuts import render

# import some views and models
from rest_framework.views import APIView
from candidate.models import Candidate
from rest_framework.viewsets import ModelViewSet


# import serializers
from candidate.serializers import CandidateSerializer

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
    serializer_class = CandidateSerializer

    def get_object(self, pk):
        try:
            return Candidate.objects.get(pk=pk)
        except Candidate.DoesNotExist:
            raise Http404
    @action(detail=True, methods=["get"])
    def get(self, request, pk, format=None):
        # for retrieving candidate information
        candidate = self.get_object(pk)
        serializer = CandidateSerializer(candidate)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        # for updating candidate information
        candidate = self.get_object(pk)
        serializer = CandidateSerializer(candidate, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        # for deleting a candidate
        candidate = self.get_object(pk)
        candidate.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=["post"])
    def post(self, request, format=None):
        # create a new candidate profile
        serializer = CandidateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)