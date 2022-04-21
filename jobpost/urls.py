from django.urls import include, path
from rest_framework import routers
from .views import OwnerJobPostViewset, NonOwnerJobPostViewset

job_router = routers.DefaultRouter()
job_router.register(r'employer-posts', OwnerJobPostViewset, basename="employer-posts")


urlpatters = [
    path('', include(job_router.urls)),

]