from django.db import models
from django.contrib.auth.models import User
from constants import MEDIA_TYPE, CONTENT_TYPE, THEMES , CATEGORY


# Create your models here.


class MetaStatus(models.Model):
    name = models.CharField(max_length=20)


class MediaCompany(models.Model):
    name = models.CharField(max_length=50, null=False)

class MediaType(models.Model):
    name = models.CharField(max_length=50, null=False)

class ContentType(models.Model):
    name = models.CharField(max_length=50, null=False)


class Themes(models.Model):
    name = models.CharField(max_length=50, null=False)

class Category(models.Model):
    name = models.CharField(max_length=50, null=False)


class MetaFields(models.Model):
    length = models.CharField(max_length=100, blank=True, null=True)
    version = models.CharField(max_length=20, blank=True, null=True)
    mediaType = models.ForeignKey(MediaType,blank=True, null=True, max_length=100, choices=MEDIA_TYPE)
    fileTitle = models.CharField(blank=True, null=True, max_length=150)
    description = models.CharField(blank=True, null=True, max_length=600)
    themes = models.ForeignKey(Themes,blank=True, null=True, max_length=200 , choices=THEMES)
    language = models.CharField(blank=True, null=True, max_length=200)
    duration = models.IntegerField(blank=True, null=True, max_length=200)
    seriesTitle = models.CharField(blank=True, null=True, max_length=200)
    seriesNumber = models.CharField(blank=True, null=True, max_length=200)
    contentType = models.ForeignKey(ContentType,blank=True, null=True, max_length=200, choices=CONTENT_TYPE)
    artist = models.CharField(blank=True, null=True, max_length=300)
    create_dt = models.DateTimeField(blank=True)
    category = models.ForeignKey(Category,blank=True, null=True, max_length=200,choices=CATEGORY)
    entity = models.CharField(blank=True, null=True, max_length=300)
    login_required = models.BooleanField(default=False)
    tags = models.CharField(blank=True, null=True, max_length=300)
    premium_required = models.BooleanField(default=False)
    monetize = models.BooleanField(default=True)



class MetaData(models.Model):
    company = models.ForeignKey(MediaCompany, max_length=100, blank=False, null=False)
    link = models.CharField(max_length=100, blank=True, null=True)
    metaFields = models.ForeignKey(MetaFields, blank=True, null=True)
    status = models.ForeignKey(MetaStatus, max_length=20, null=True)
