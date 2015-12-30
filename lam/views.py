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
        increaseCount = False
        campaign = request.data['campaign']
        source = request.data['media_source']
        install_date = request.data['install_time']
        media_source = LAM_User.objects.filter(media_source=source).first()
        if media_source is None:
            summary = source + " " + install_date
        else:
            increaseCount = True
            summary= install_date
        install_data = InstallData.objects.create(campaign_name=campaign,media_source=media_source, summary=summary)
        install_data.save()
        if increaseCount:
            media_source.install_count = media_source.install_count +1
            media_source.save()
        return Response("Synced successfully", status.HTTP_201_CREATED)
    except Exception, e:
        return Response(str(e), status.HTTP_400_BAD_REQUEST)


class InstallDataViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = InstallData.objects.all()
    serializer_class = InstallDataSerializer


