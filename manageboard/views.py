from django.shortcuts import render
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
import boto
from serializer import CompanySerializer, MetaDataSerializer, MetaFieldSerializer
from models import MediaCompany, MetaData, MetaStatus, MetaFields
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from constants import MetaStatusConstants, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY
from django.db import transaction
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
import django_filters
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template.context import RequestContext
from util import email_check
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth import logout as auth_logout




# Create your views here.



def login(request):
    return render(request, 'views/index.html')


@user_passes_test(email_check, login_url='/')
def dashboard(request):
    return render(request, 'views/searchCompany.html')


def get_metafields(request, meta_id):
    meta_obj = get_object_or_404(MetaData, pk=meta_id)
    context = RequestContext(request, {'user': request.user, 'meta_obj': meta_obj})
    return render_to_response('views/edit_metafields.html', context_instance=context)


@user_passes_test(email_check, login_url='/')
def logout(request):
    auth_logout(request)
    return redirect('/')


@api_view(['GET'])
def sync_companies(request):
    try:
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
        meta_obj = MetaData.objects.filter(id=meta_id).first()
        length = request.data['length']
        version = request.data['version']
        mediaType = request.data['mediaType']
        fileTitle = request.data['fileTitle']
        description = request.data['description']
        themes = request.data['themes']
        god = request.data['god']
        book = request.data['book']
        shrines = request.data['shrines']
        topic = request.data['topic']
        language = request.data['language']
        duration = request.data['duration']
        seriesTitle = request.data['seriesTitle']
        seriesNumber = request.data['seriesNumber']
        episodeNumber = request.data['episodeNumber']
        contentType = request.data['contentType']
        artist = request.data['artist']

        if meta_obj.metaFields is None:
            meta_fields = MetaFields.objects.create(length=length, version=version, mediaType=mediaType,
                                                    fileTitle=fileTitle, description=description,
                                                    themes=themes, god=god, book=book, shrines=shrines, topic=topic,
                                                    language=language, duration=duration, seriesTitle=seriesTitle,
                                                    seriesNumber=seriesNumber, episodeNumber=episodeNumber,
                                                    contentType=contentType, artist=artist)
            meta_obj.metaFields_id = meta_fields.id
            meta_obj.save()
        else:
            meta_fields = meta_obj.metaFields
            meta_fields.length = length
            meta_fields.version = version
            meta_fields.mediaType = mediaType
            meta_fields.fileTitle = fileTitle
            meta_fields.description = description
            meta_fields.themes = themes
            meta_fields.god = god
            meta_fields.book = book
            meta_fields.shrines = shrines
            meta_fields.topic = topic
            meta_fields.language = language
            meta_fields.duration = duration
            meta_fields.seriesTitle = seriesTitle
            meta_fields.seriesNumber = seriesNumber
            meta_fields.episodeNumber = episodeNumber
            meta_fields.contentType = contentType
            meta_fields.artist = artist

        meta_fields.save()

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
    # status = django_filters.CharFilter(name='currentDataState__name')
    name = django_filters.CharFilter(name='name')


    class Meta:
        model = MetaData


@authentication_classes((TokenAuthentication, SessionAuthentication,))
@permission_classes((IsAuthenticated,))
class MetaDataViewSet(viewsets.ModelViewSet):
    serializer_class = MetaDataSerializer
    queryset = MetaData.objects.all()
    filter_class = MetaDataFilter
    paginate_by = 6
    paginate_by_param = 'page_size'
    queryset._result_cache = None


@api_view(['GET'])
def fetch_metadata(request, meta_id):
    try:
        meta_obj = MetaData.objects.filter(id=meta_id).first()
        meta_fields = meta_obj.metaFields
        serializer = MetaFieldSerializer(instance=meta_fields)

    except Exception, e:
        return Response(str(e), status.HTTP_400_BAD_REQUEST)
    return Response(serializer.data, status.HTTP_201_CREATED)


@api_view(['GET'])
def exists_metadata(request, meta_id):
    try:
        is_exists = True
        meta_obj = MetaData.objects.filter(id=meta_id).first()
        if meta_obj.metaFields == None:
            is_exists = False

    except Exception, e:
        return Response(str(e), status.HTTP_400_BAD_REQUEST)
    return Response(is_exists, status.HTTP_200_OK)
