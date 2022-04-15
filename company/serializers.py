# import model and serializer
from rest_framework import serializers
from company.models import Company

# import validation tools
from django.contrib.auth.hashers import make_password
from rest_framework.validators import UniqueValidator

class CompanySerializer(serializers.ModelSerializer):

    """ 
        A company serializer to create, update, retrieve and list the elements 
    """

    class Meta:
        model = Company
        fields = ["id", "company_name", "company_email", "password", "company_summary", "company_address"]

    company_email = serializers.EmailField(
        validators=[UniqueValidator(Company.objects.all())]
        )

    password = serializers.CharField(
        write_only = True,
        required = True,
        style = {"input_type": "password", "placeholder": "Password"}
    )

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data.get("password"))
        company = super().create(validated_data)
        company.save()
        return company

    