from django.db import models

from django.contrib.auth.models import User


# Create your models here.
class Company(models.Model):
    user_id = models.ForeignKey(User, models.SET_NULL, null=True, blank=False)
    company_name = models.CharField(max_length=50, null=False, blank=False)
    company_email = models.EmailField(unique=True, null=False, default="")
    company_summary = models.TextField(default="")
    company_address = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self) -> str:
        return self.company_name