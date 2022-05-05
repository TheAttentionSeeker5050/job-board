from django.shortcuts import render

# import some views and models
from rest_framework.views import APIView
from company.models import Company
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics

from company.serializers import CompanySerializer
from app.permissions import UserIsLoggedIn
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class CompanyViewset(ModelViewSet):
    """ 
        Creates, deletes and updates user instances, retrieves this is a custom view
    """
    permission_classes = [UserIsLoggedIn,]
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CompanyBrowseView(generics.ListAPIView):
    """For listing the candidates, allows filters"""
    

    queryset = Company.objects.all()
    permission_classes = [IsAuthenticated,]
    serializer_class = CompanySerializer

class CompanyRetrieveView(generics.RetrieveAPIView):
    """For listing the candidates, allows filters"""
    

    queryset = Company.objects.all()
    permission_classes = [IsAuthenticated,]
    serializer_class = CompanySerializer