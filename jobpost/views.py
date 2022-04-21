from urllib import request
from django.shortcuts import render

# import models
from jobpost.models import JobPost

# import http methods
from rest_framework.response import Response


# import serializers and viewsets
from jobpost.serializers import JobPostSerializer
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

# import permissions
from app.permissions import IsJobPostOwner


# Create your views here.


class OwnerJobPostViewset(ModelViewSet):
    """This is the base viewset which only the owner of the jobpost has access to"""
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer
    permission_classes = [IsJobPostOwner,]


    def list(self, request):
        """List all the jobpost owned by the user"""
        list_of_jobposts = JobPost.objects.filter(employer_id = request.user)
        serializer = self.get_serializer(list_of_jobposts, many=True)
        return Response(serializer.data)

class NonOwnerJobPostViewset(ReadOnlyModelViewSet):
    """
        This is the base viewset which lets the user interact with the jobposts
        It is readonly so the user cannot modify the information on the jobpost
    """
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer