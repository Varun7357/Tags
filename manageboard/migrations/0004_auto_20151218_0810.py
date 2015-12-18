# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manageboard', '0003_auto_20151217_0844'),
    ]

    operations = [
        migrations.CreateModel(
            name='MetaData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('link', models.CharField(max_length=100, null=True, blank=True)),
                ('company', models.ForeignKey(to='manageboard.MediaCompany', max_length=100)),
                ('metaFields', models.ForeignKey(blank=True, to='manageboard.MetaFields', null=True)),
                ('status', models.ForeignKey(to='manageboard.MetaStatus', max_length=20, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='meta',
            name='company',
        ),
        migrations.RemoveField(
            model_name='meta',
            name='metaFields',
        ),
        migrations.RemoveField(
            model_name='meta',
            name='status',
        ),
        migrations.DeleteModel(
            name='Meta',
        ),
    ]
