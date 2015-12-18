__author__ = 'nitinw'

from django.contrib.auth.models import User
from rest_framework import serializers
from models import MediaCompany , MetaData , MetaFields , MetaStatus


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaCompany
        extra_kwargs = {
            "id": {
                "read_only": False,
                "required": False,
            },
        }

class MetaDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetaData
        extra_kwargs = {
            "id": {
                "read_only": False,
                "required": False,
            },
        }

class MetaFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetaFields
        extra_kwargs = {
            "id": {
                "read_only": False,
                "required": False,
            },
        }


class MetaStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetaStatus
        extra_kwargs = {
            "id": {
                "read_only": False,
                "required": False,
            },
        }



