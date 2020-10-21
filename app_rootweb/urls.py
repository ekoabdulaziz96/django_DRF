"""rootweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers, serializers, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

# from backend import views as views_backend
from . import views as views_root

from app_blog.urls import router as appBlogRouter
from app_snippet.urls import router as appSnippetRouter
#Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', views_root.UserViewSet)
router.registry.extend(appBlogRouter.registry)
router.registry.extend(appSnippetRouter.registry)

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'blog': reverse('ab:api', request=request, format=format),
        'snippets': reverse('as:api', request=request, format=format),
    })



urlpatterns = [
    path('admin/', admin.site.urls),
    # -----------------------------------------------------------app
    # path('app-blog/', include('app_blog.urls', namespace='ab')), # sudah di handle routing
    path('app-snippet/', include('app_snippet.urls', namespace='as')),
    
    # path('', views.index),
    # path('', views_root.ApiRoot.as_view(), name=views_root.ApiRoot.name),
    # path('ini-api/',views_root.ini_api, name='ini-api'),
    # path('coba/',views_root.Coba.as_view(), name='nyobo'),

    #*** ----- api root -> url pattern 
    path('', api_root), 
    
    #*** ----- api root -> routing
    path('routing/', include(router.urls), name='router'),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


