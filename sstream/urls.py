from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from manageboard import views
from lam.views import sync_installation_data ,sync_android_data,sync_ios_data


router = routers.DefaultRouter()
router.register(r'company/all', views.CompanyViewSet)
router.register(r'metadata/all', views.MetaViewSet)
router.register(r'metafields/all', views.MetaViewSet)
router.register(r'metastatus/all', views.MetaViewSet)
router.register(r'metafiles', views.MetaDataViewSet)
router.register(r'leaderboard/all', views.LAMUserDataViewSet)

urlpatterns = patterns('', url(r'^ssadmin/', include(router.urls)),
                       url('', include('social.apps.django_app.urls', namespace='social')),
                       url(r'^$', 'manageboard.views.login'),
                       url(r'admin/', include(admin.site.urls)),
                       url(r'^index/$', views.dashboard),
                       url(r'^sync/companies/$', views.sync_companies),
                       url(r'^sync/files/(?P<company_id>\d+)', views.sync_files),
                       url(r'^get/metadata/(?P<meta_id>\d+)', views.fetch_metadata),
                       url(r'^metafile/edit/(?P<meta_id>\d+)', views.get_metafields),
                       url(r'^save/meta/(?P<meta_id>\d+)', views.save_metadata),
                       url(r'^metadata/exists/(?P<meta_id>\d+)', views.exists_metadata),
                       url(r'^logout/$', views.logout, name='logout'),
                       url(r'^lam/data/$', sync_installation_data),
                       url(r'^sync/android/$', sync_android_data),
                       url(r'^sync/ios/$', sync_ios_data)



)
