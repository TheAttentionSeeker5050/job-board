from django.shortcuts import render

# import some views and models
from rest_framework.views import APIView
from company.models import Company
from rest_framework.viewsets import ModelViewSet

from company.serializers import CompanySerializer
from app.permissions import UserIsLoggedIn

# Create your views here.
# Create your views here.
class CompanyViewset(ModelViewSet):
    """ 
        Creates, deletes and updates user instances, retrieves this is a custom view
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    # permission_classes = [UserIsLoggedIn,]

    