"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


# import external libs
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers


# the media url imports
from django.conf import settings
from django.conf.urls.static import static


# import the views
from candidate.views import CandidateCustomView, FileUploadViewset, CandidateBrowseView, CandidateRetrieveView
from company.views import CompanyViewset, CompanyBrowseView, CompanyRetrieveView
import app.views as user_views
from jobpost.views import OwnerJobPostViewset, NonOwnerJobPostViewset


# import authentication
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = routers.DefaultRouter()
router.register(r'users', user_views.UserViewSet)
router.register(r'candidate', CandidateCustomView, basename="candidate")
router.register(r'company', CompanyViewset, basename="company")
router.register(r'file-upload', FileUploadViewset, basename="file-upload")
router.register(r'employer-posts', OwnerJobPostViewset, basename="employer-posts")
router.register(r'browse-jobposts', NonOwnerJobPostViewset, basename="browse-jobposts")



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

    # retrieve and list candidates as another user
    path("api/browse/candidates/", CandidateBrowseView.as_view()),
    path("api/browse/candidates/<int:pk>", CandidateRetrieveView.as_view()),

    # retrieve and list companies as another user
    path("api/browse/companies/", CompanyBrowseView.as_view()),
    path("api/browse/companies/<int:pk>", CompanyRetrieveView.as_view()),

    # register urls
    path('api/register/', user_views.RegisterView.as_view()),
    path('api/change-password/<int:pk>', user_views.ChangePasswordView.as_view()),


    # authentication urls
    path('api/token/obtain/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
