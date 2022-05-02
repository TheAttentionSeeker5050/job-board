from argparse import ONE_OR_MORE

from django.db import models

# import the user model which we will use later
from django.contrib.auth.models import User
from company.models import Company
from candidate.models import Candidate

CERT_CHOICES = [
    ("", ""),
    ("MIDDLE_SCHOOL","Middle School Diploma"),
    ("HIGH_SCHOOL", "High School Diploma"),
    ("TRADE_SCHOOL", "Vocational or Trade School Diploma"),
    ("OTHER", "Other")
]


# Create your models here.
class JobPost(models.Model):
    employer_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False) # this is the user model that will post the job
    employer_name = models.ForeignKey(Company, on_delete=models.CASCADE, null=False, blank=False, default="")
    job_position = models.CharField(max_length=45, null=False, blank=False)
    job_description = models.TextField(default="")
    hourly_salary = models.FloatField(blank=True, null=True)
    years_of_experience_required = models.IntegerField(blank=True, null=True)
    certification_required = models.CharField(default="", choices=CERT_CHOICES, max_length=100)


class JobCandidateApply(models.Model):
    candidate_user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False) # this is different from the next attribute, maybe in the future we may need a user key
    candidate_id = models.ForeignKey(Candidate, on_delete=models.CASCADE, null=False, blank=False)
    employer_id = models.ForeignKey(Company, on_delete=models.CASCADE, null=False, blank=False)
    uploaded_file_address = models.CharField(max_length=500)


