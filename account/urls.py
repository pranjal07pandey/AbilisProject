from django.contrib import admin
from django.urls import path , include
from .import views
from django.conf.urls import url

urlpatterns = [
    url(r'^document/$', views.document_list, name='document_list'),
    url(r'^document/new/$', views.document_new, name='document_new'),
    url(r'^document/(?P<pk>[0-9]+)/edit/$', views.document_edit, name='document_edit'),
    url(r'^document/(?P<pk>[0-9]+)/delete/$', views.document_delete, name='document_delete'),

    url(r'^dashboard/$', views.dashboard, name='dashboard'),

]


