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
from candidate.views import CandidateCustomView, FileUploadViewset
from company.views import CompanyViewset
import app.views as user_views


# import authentication
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = routers.DefaultRouter()
router.register(r'users', user_views.UserViewSet)
# router.register(r'groups', default_views.GroupViewSet)
router.register(r'candidate', CandidateCustomView, basename="candidate")
router.register(r'company', CompanyViewset, basename="company")
router.register(r'file-upload', FileUploadViewset, basename="file-upload")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

    # custom views
    

    # register urls
    path('api/register/', user_views.RegisterView.as_view()),
    path('api/change-password/<int:pk>', user_views.ChangePasswordView.as_view()),


    # authentication urls
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
