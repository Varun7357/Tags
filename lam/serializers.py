
from django.contrib.auth.models import User
from rest_framework import serializers
from models import InstallData, LAM_User

class InstallDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstallData
        extra_kwargs = {
            "id": {
                "read_only": False,
                "required": False,
            },
        }


class LAMUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = LAM_User
        extra_kwargs = {
            "id": {
                "read_only": False,
                "required": False,
            },
        }