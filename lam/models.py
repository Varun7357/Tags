from django.db import models

# Create your models here.

class LAM_User(models.Model):
    media_source = models.CharField(max_length=100, blank=True, null=False)
    email = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    install_count = models.IntegerField(max_length=100,default=0)
    is_leader= models.BooleanField(default=False)
    is_intern = models.BooleanField(default=True)
    leader = models.ForeignKey("self" , null=True,default=None)


    def __unicode__(self):
        return str(self.email)



class InstallData(models.Model):
    campaign_name = models.CharField(max_length=100, blank=True, null=False)
    media_source=models.ForeignKey(LAM_User, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    summary = models.CharField(max_length=200, blank=True, null=True)