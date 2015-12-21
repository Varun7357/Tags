from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from manageboard import views


router = routers.DefaultRouter()
router.register(r'company/all', views.CompanyViewSet)
router.register(r'metadata/all', views.MetaViewSet)
router.register(r'metafields/all', views.MetaViewSet)
router.register(r'metastatus/all', views.MetaViewSet)
router.register(r'metafiles', views.MetaDataViewSet)

urlpatterns = patterns('', url(r'^ssadmin/', include(router.urls)),
                       url('', include('social.apps.django_app.urls', namespace='social')),
                       url(r'^$', 'manageboard.views.login'),
                       url(r'admin/', include(admin.site.urls)),
                       url(r'^index/$', views.dashboard),
                       url(r'^sync/companies/$', views.sync_companies),
                       url(r'^sync/files/(?P<company_id>\d+)', views.sync_files),
                       #url(r'^get/meta/(?P<company_id>\d+)', views.FethMetaDataForCompany),
                       url(r'^save/meta/(?P<meta_id>\d+)', views.save_metadata),





)
