from django.db import models
from django.contrib.auth.models import User



# Create your models here.


class MetaStatus(models.Model):
    name = models.CharField(max_length=20)


class MediaCompany(models.Model):
    name = models.CharField(max_length=50, null=False)


class MetaFields(models.Model):
    length = models.CharField(max_length=100, blank=True, null=True)
    version = models.CharField(max_length=20, blank=True, null=True)
    mediaType = models.CharField(blank=True, null=True, max_length=100)


class MetaData(models.Model):
    company = models.ForeignKey(MediaCompany, max_length=100, blank=False, null=False)
    link = models.CharField(max_length=100, blank=True, null=True)
    metaFields = models.ForeignKey(MetaFields, blank=True, null=True)
    status = models.ForeignKey(MetaStatus, max_length=20, null=True)
