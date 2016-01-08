import urllib2
from django.shortcuts import render
from rest_framework import status
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from datetime import datetime
from dateutil import parser
from rest_framework import viewsets
import logging
import requests, json, csv, pandas as pa, numpy as np
# Create your views here.
from lam.models import InstallData, LAM_User
from lam.serializers import InstallDataSerializer, LAMUserSerializer

logger = logging.getLogger(__name__)


@api_view(['POST'])
def sync_installation_data(request):
    try:
        # increaseCount = False
        logger.error(request.data)
        campaign = request.data['campaign']
        source = request.data['media_source']
        summary = request.data['install_time']
        media_source_user = LAM_User.objects.filter(media_source=source).first()
        if media_source_user is None:
            lam_user = LAM_User.objects.create(media_source=source)
            lam_user.save()
            media_source_user = lam_user

        install_data = InstallData.objects.create(campaign_name=campaign, media_source=media_source_user,
                                                  summary=summary)
        install_data.save()
        media_source_user.install_count = media_source_user.install_count + 1
        media_source_user.save()
        return Response("Synced successfully", status.HTTP_201_CREATED)
    except Exception, e:
        logger.error(str(e))
        logger.error("error while registering media source", exc_info=True)
        return Response(str(e), status.HTTP_400_BAD_REQUEST)



class InstallDataViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = InstallData.objects.all()
    serializer_class = InstallDataSerializer



@api_view(['GET'])
def sync_android_data(request):
    url = 'https://hq.appsflyer.com/export/com.lookatme/partners_report?api_token=ad78e794-7cb4-48e0-a49a-11c62507240b&from=2015-12-31&to=2016-03-31'
    first_row = True
    response = urllib2.urlopen(url)
    if response.code == 200:

        cr = csv.reader(response)

        for row in cr:
            if first_row:
                first_row = False
                continue
            source = row[01]
            media_source = LAM_User.objects.filter(media_source=source).first()
            if media_source is not None:
                media_source.android_count = row[04]
                media_source.save()
        return Response("Synced successfully", status.HTTP_200_OK)
    return Response("Sync not successful", status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def sync_ios_data(request):
    url = 'https://hq.appsflyer.com/export/id1014906882/partners_report?api_token=ad78e794-7cb4-48e0-a49a-11c62507240b&from=2015-12-31&to=2016-03-31'
    first_row = True
    response = urllib2.urlopen(url)
    if response.code == 200:

        cr = csv.reader(response)

        for row in cr:
            if first_row:
                first_row = False
                continue
            source = row[01]
            media_source = LAM_User.objects.filter(media_source=source).first()
            if media_source is not None:
                media_source.ios_count = row[04]
                media_source.save()
        return Response("Synced successfully", status.HTTP_200_OK)
    return Response("Sync not successful", status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def compare_install(request):
    try:

        media_sources = LAM_User.objects.all()
        for source in media_sources:
            exact_count = source.android_count + source.ios_count
            if source.install_count < exact_count:
                source.install_count = exact_count
                source.save()
        return Response("Synced successfully", status.HTTP_200_OK)

    except Exception, e:
        logger.error(str(e))
        logger.error("error while comparing installs", exc_info=True)
        return Response(str(e), status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def update_profile(request):
    try:
        first_row = True
        response = request.FILES['fileUpload']
        cr = csv.reader(response)
        for row in cr:
            if first_row:
                first_row = False
                continue
            source = str(row[02])
            media_source = LAM_User.objects.filter(media_source=source).first()
            if media_source is not None:
                media_source.name = row[0]
                media_source.email = row[1]
                if row[4] =='T':
                    media_source.is_intern = False
                    media_source.is_leader = True
                else:
                    media_source.is_leader = False
                    media_source.leader =LAM_User.objects.filter(media_source=row[3]).first()
                media_source.save()
        return Response("Synced successfully", status.HTTP_200_OK)
    except Exception, e:
        return Response("Sync not successful", status.HTTP_500_INTERNAL_SERVER_ERROR)
