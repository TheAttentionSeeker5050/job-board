# from asyncio.windows_events import NULL
from rest_framework.permissions import BasePermission

from django.contrib.auth.models import User

class UserIsLoggedIn(BasePermission):
    def has_object_permission(self, request, view, obj):
        """ This permission object checks if the user is logged in and is the owner of this account """

        if request.user.is_authenticated:
            return obj.user_id == request.user
        return False

class IsJobPostOwner(BasePermission):
    """This permission allows us to modify the jobposts only if the user owns the jobpost"""
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            return obj.employer_id == request.user
        return False