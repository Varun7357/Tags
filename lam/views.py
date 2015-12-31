from django.shortcuts import render
from rest_framework import status
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from datetime import datetime
from dateutil import parser
from rest_framework import viewsets

import requests, json , csv , pandas as pa,numpy as np



# Create your views here.
from lam.models import InstallData,LAM_User
from lam.serializers import InstallDataSerializer, LAMUserSerializer


@api_view(['POST'])
def sync_installation_data(request):
    try:
        #increaseCount = False
        campaign = request.data['campaign']
        source = request.data['media_source']
        summary = request.data['install_time']
        media_source_user = LAM_User.objects.filter(media_source=source).first()
        if media_source_user is None:
            lam_user= LAM_User.objects.create(media_source = source)
            lam_user.save()
            media_source_user = lam_user

        install_data = InstallData.objects.create(campaign_name=campaign,media_source=media_source_user, summary=summary)
        install_data.save()
        media_source_user.install_count = media_source_user.install_count +1
        media_source_user.save()
        return Response("Synced successfully", status.HTTP_201_CREATED)
    except Exception, e:

        return Response(str(e), status.HTTP_400_BAD_REQUEST)


class InstallDataViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = InstallData.objects.all()
    serializer_class = InstallDataSerializer


