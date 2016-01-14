__author__ = 'nitinw'

from django.contrib.auth.models import User
from rest_framework import serializers
from models import MediaCompany , MetaData , MetaFields , MetaStatus, MediaType, Themes , ContentType, Category


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


class MediaTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaType
        extra_kwargs = {
            "id": {
                "read_only": False,
                "required": False,
            },
        }

class ThemesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Themes
        extra_kwargs = {
            "id": {
                "read_only": False,
                "required": False,
            },
        }

class ContentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentType
        extra_kwargs = {
            "id": {
                "read_only": False,
                "required": False,
            },
        }

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        extra_kwargs = {
            "id": {
                "read_only": False,
                "required": False,
            },
        }
