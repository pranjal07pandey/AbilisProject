
from .import views
from django.urls import path


from django.conf.urls import url , include




urlpatterns = [
    url(r'^document/$', views.document_list, name='document_list'),
    url(r'^document/new/$', views.document_new, name='document_new'),
    url(r'^document/(?P<pk>[0-9]+)/edit/$', views.document_edit, name='document_edit'),
    url(r'^document/(?P<pk>[0-9]+)/delete/$', views.document_delete, name='document_delete'),
    url(r'^category/$', views.list_category, name='list_category'),
    url(r'^category/new/$', views.add_category, name='add_category'),
    # url(r'^category/(?P<pk>[0-9]+)/edit/$', views.edit_category, name='edit_category'),
    url(r'^category/(?P<pk>[0-9]+)/delete/$', views.delete_category, name='delete_category'),
    url(r'^doc_list/$', views.list_document_category, name='list_document_category'),
    url(r'^doc_list/new/$', views.add_document_category, name='add_document_category'),
    # url(r'^category/(?P<pk>[0-9]+)/edit/$', views.edit_category, name='edit_category'),
    url(r'^doc_list/(?P<pk>[0-9]+)/delete/$', views.delete_document_category, name='delete_document_category'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^userlist/$', views.userList, name='userlist'),
    path('question_list/', views.question_list, name='question_list'),
    path('question_answer/<int:id>/', views.question_answer, name='question_answer'),
    path('user_question_list/<slug:name>/', views.get_user_question, name='user_question_list')
]


