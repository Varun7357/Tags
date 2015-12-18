from django.shortcuts import render
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
import boto
from serializer import CompanySerializer ,MetaDataSerializer ,MetaFieldSerializer
from models import MediaCompany, MetaData, MetaStatus, MetaFields
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from constants import MetaStatusConstants
from django.db import transaction
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
import django_filters




# Create your views here.


def login(request):
    return render(request, 'views/index.html')


def dashboard(request):
    return render(request, 'views/searchCompany.html')


#
# def logout(request):
# auth_logout(request)
#     return redirect('/')


@api_view(['GET'])
def sync_companies(request):
    try:
        AWS_ACCESS_KEY_ID = 'AKIAJCLD2GUHLS6VY3LQ'
        AWS_SECRET_ACCESS_KEY = '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'
        conn = boto.connect_s3(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
        bucket = conn.get_bucket('hog-production')
        companies = bucket.list("", "/")
        existing_companies = MediaCompany.objects.all()
        for company in companies:
            isNewCompany = True
            for existing_company in existing_companies:
                if existing_company.name == existing_company.name:
                    isNewCompany = False
                    break
            if isNewCompany:
                mediacompany = MediaCompany.objects.create(name=company.name)
                mediacompany.save()

        return Response("Synced successfully", status.HTTP_201_CREATED)
    except Exception, e:
        return Response(str(e), status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def sync_files(request, company_id):
    try:
        AWS_ACCESS_KEY_ID = 'AKIAJCLD2GUHLS6VY3LQ'
        AWS_SECRET_ACCESS_KEY = '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'
        conn = boto.connect_s3(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
        company = MediaCompany.objects.filter(id=company_id).first()
        bucket = conn.get_bucket('hog-production')
        files = list(bucket.list(company.name, "/"))

        existing_files = MetaData.objects.filter(company=company)
        status_incomplete = MetaStatus.objects.filter(name=MetaStatusConstants.INCOMPLETE).first()
        for file in files:
            is_new_file = True
            for existing_file in existing_files:
                if file.name == existing_file.link:
                    is_new_file = False
                    break

            if is_new_file:
                if file.name != company.name:
                    meta = MetaData.objects.create(company=company, link=file.name, status=status_incomplete)
                    meta.save()

        return Response("Files synced successfully", status.HTTP_201_CREATED)
    except Exception, e:
        return Response(str(e), status.HTTP_400_BAD_REQUEST)

@transaction.atomic
@api_view(['POST'])
@authentication_classes((TokenAuthentication, SessionAuthentication,))
@permission_classes((IsAuthenticated,))
def save_metadata(request, meta_id):
    try:

        length = request.data['length']
        version = request.data['version']
        mediaType = request.data['mediaType']
        meta_fields = MetaFields.objects.create(length=length, version=version, mediaType=mediaType)
        meta_fields.save()
        meta_data = MetaData.objects.filter(id=meta_id).first()
        meta_data.metaFields_id = meta_fields.id
        meta_data.save()
        # status_incomplete = MetaStatus.objects.filter(name=MetaStatusConstants.INCOMPLETE).first()

        return Response("OK", status.HTTP_200_OK)
    except Exception, e:
        return Response(str(e), status.HTTP_400_BAD_REQUEST)



@authentication_classes((TokenAuthentication, SessionAuthentication,))
@permission_classes((IsAuthenticated,))
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = MediaCompany.objects.all()
    serializer_class = CompanySerializer


@authentication_classes((TokenAuthentication, SessionAuthentication,))
@permission_classes((IsAuthenticated,))
class MetaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MetaData.objects.all()
    serializer_class = MetaDataSerializer


@authentication_classes((TokenAuthentication, SessionAuthentication,))
@permission_classes((IsAuthenticated,))
class FieldViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MetaFields.objects.all()
    serializer_class = MetaFieldSerializer


@authentication_classes((TokenAuthentication, SessionAuthentication,))
@permission_classes((IsAuthenticated,))
class MetaStatusViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MetaStatus.objects.all()
    serializer_class = MetaFieldSerializer


@authentication_classes((TokenAuthentication, SessionAuthentication,))
@permission_classes((IsAuthenticated,))
class MetaDataFilter(django_filters.FilterSet):
    company = django_filters.CharFilter(name='name')



@authentication_classes((TokenAuthentication, SessionAuthentication,))
@permission_classes((IsAuthenticated,))
class FethMetaDataForCompany(viewsets.ModelViewSet):
    queryset = MetaData.objects.all()
    serializer_class = MetaDataSerializer
    filter_class = MetaDataFilter
    paginate_by = 6
    paginate_by_param = 'page_size'
    max_paginate_by = 10
    queryset._result_cache = None