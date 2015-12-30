from django.db import models
from django.contrib.auth.models import User
from constants import MEDIA_TYPE , CONTENT_TYPE



# Create your models here.


class MetaStatus(models.Model):
    name = models.CharField(max_length=20)


class MediaCompany(models.Model):
    name = models.CharField(max_length=50, null=False)


class MetaFields(models.Model):
    length = models.CharField(max_length=100, blank=True, null=True)
    version = models.CharField(max_length=20, blank=True, null=True)
    mediaType = models.CharField(blank=True, null=True, max_length=100, choices=MEDIA_TYPE)
    fileTitle = models.CharField(blank=True, null=True, max_length=200)
    description = models.CharField(blank=True, null=True, max_length=600)
    themes = models.CharField(blank=True, null=True, max_length=200)
    god = models.CharField(blank=True, null=True, max_length=200)
    book = models.CharField(blank=True, null=True, max_length=200)
    shrines = models.CharField(blank=True, null=True, max_length=200)
    topic = models.CharField(blank=True, null=True, max_length=200)
    language = models.CharField(blank=True, null=True, max_length=200)
    duration = models.CharField(blank=True, null=True, max_length=200)
    seriesTitle = models.CharField(blank=True, null=True, max_length=200)
    seriesNumber = models.CharField(blank=True, null=True, max_length=200)
    episodeNumber = models.CharField(blank=True, null=True, max_length=200)
    contentType = models.CharField(blank=True, null=True, max_length=200 , choices = CONTENT_TYPE)
    artist = models.CharField(blank=True, null=True, max_length=200)


class MetaData(models.Model):
    company = models.ForeignKey(MediaCompany, max_length=100, blank=False, null=False)
    link = models.CharField(max_length=100, blank=True, null=True)
    metaFields = models.ForeignKey(MetaFields, blank=True, null=True)
    status = models.ForeignKey(MetaStatus, max_length=20, null=True)



