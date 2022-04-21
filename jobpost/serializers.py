from dataclasses import fields
from rest_framework import serializers
from jobpost.models import JobPost

"""
    This serializer will be able yo post new jobpost, request jobpost info, modify jobpost and delete
    It will be a normal model serializer for the moment...
"""

class JobPostSerializer(serializers.ModelSerializer):
    model = JobPost
    fields = ["pk", "employer_id", "job_position", "job_description", "hourly_salary", "years_of_experience_required", "certification_required"]