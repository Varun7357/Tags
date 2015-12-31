# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InstallData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('campaign_name', models.CharField(max_length=100, blank=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('summary', models.CharField(max_length=200, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LAM_User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('media_source', models.CharField(max_length=100, null=True, blank=True)),
                ('email', models.CharField(max_length=100, null=True, blank=True)),
                ('name', models.CharField(max_length=100, null=True, blank=True)),
                ('install_count', models.IntegerField(default=0, max_length=100)),
                ('is_leader', models.BooleanField(default=False)),
                ('is_intern', models.BooleanField(default=True)),
                ('leader', models.ForeignKey(default=None, to='lam.LAM_User', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='installdata',
            name='media_source',
            field=models.ForeignKey(blank=True, to='lam.LAM_User', null=True),
            preserve_default=True,
        ),
    ]
