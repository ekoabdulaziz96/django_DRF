from django.urls import include, path
from rest_framework import routers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from rest_framework.urlpatterns import format_suffix_patterns

from . import views_artikel
app_name = 'app_blog'

router = routers.DefaultRouter()
router.register(r'artikel', views_artikel.ArtikelViewSet)

@api_view(['GET'])
def api_blog(request, format=None):
    return Response({
        'artikel': reverse('ab:artikel', request=request, format=format),
    })

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', api_blog, name='api'),
    path('artikel/', views_artikel.ArtikelViewSet, name='artikel'),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
