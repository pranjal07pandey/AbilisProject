
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from account import views
from django.conf.urls import url


from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'users', views.UserList)
router.register(r'Dcategory', views.DocumentCategoryList)
router.register(r'subcategory', views.categoryList)
router.register(r'documentation',views.DocumentationList)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.logout_user, name='logout'),

    path('document/',include('account.urls')),

    path('dashboard/',include('account.urls')),
    path('userlist/', include('account.urls')),

    path('category/', include('account.urls')),

    path('doc_category/', include('account.urls')),

    url(r'^api/', include(router.urls)),

    path('api/Validusers/', views.UserLogin),




]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

