from django.urls import include, path
from rest_framework import routers, renderers
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from . import views, views_apiView, views_classBased, views_modelMixins, views_genericApi
from . import views_useAuth
from . import views_viewSets
app_name = 'app_snippet'

# router = routers.DefaultRouter()
# router.register(r'snippets-classBased', views_classBased.SnippetList)

# ---------------------------------------------------------------------------------------------routing viewset
# --------------------url pattern
snippet_list = views_viewSets.SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
snippet_detail = views_viewSets.SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
snippet_highlight = views_viewSets.SnippetViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])
# --------------------user
user_list = views_viewSets.UserViewSet.as_view({
    'get': 'list'
})
user_detail = views_viewSets.UserViewSet.as_view({
    'get': 'retrieve'
})

# --------------------router
router = routers.DefaultRouter()
router.register(r'snippet', views_viewSets.SnippetViewSet)
router.register(r'user', views_viewSets.UserViewSet)

# ---------------------------------------------------------------------------------------------
@api_view(['GET'])
def api_snippet(request, format=None):
    return Response({
        'snippets': reverse('as:snippet-list', request=request, format=format),
        'user': reverse('as:user-list', request=request, format=format),
        'Routing-snippets': reverse('as:snippetRouting-list', request=request, format=format),
        'Routing-user': reverse('as:userRouting-list', request=request, format=format)
    })

urlpatterns = [
    path('', api_snippet,name='api'),

    # --------------------------------------
    path('snippets-genericApi/', views_genericApi.SnippetList.as_view(), name='snippet-list'),
    path('snippets-genericApi/<int:pk>/', views_genericApi.SnippetDetail.as_view(),  name='snippet-detail'),
    path('snippets-genericApi/<int:pk>/highlight/', views_genericApi.SnippetHighlight.as_view(),name='snippet-highlight'),

    path('snippets-modelMixins/', views_modelMixins.SnippetList.as_view()),
    path('snippets-modelMixins/<int:pk>/', views_modelMixins.SnippetDetail.as_view()),

    path('snippets-classBased/', views_classBased.SnippetList.as_view()),
    path('snippets-classBased/<int:pk>/', views_classBased.SnippetDetail.as_view()),

    path('snippets-apiView/', views_apiView.snippet_list),
    path('snippets-apiView/<int:pk>/', views_apiView.snippet_detail),

    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),

    # --------------------------------------
    path('users/', views_useAuth.UserList.as_view(),name='user-list'),
    path('users/<int:pk>/', views_useAuth.UserDetail.as_view(),name='user-detail'),


# ---------------------------------------------------------------------------------------------routing viewset
    path('snippets-routing/', snippet_list, name='snippetRouting-list'),
    path('snippets-routing/<int:pk>/', snippet_detail, name='snippetRouting-detail'),
    path('snippets-routing/<int:pk>/highlight/', snippet_highlight, name='snippetRouting-highlight'),
    # --------------------------------------
    path('users-routing/', user_list, name='userRouting-list'),
    path('users-routing/<int:pk>/', user_detail, name='userRouting-detail')
]

# urlpatterns = format_suffix_patterns(urlpatterns)
