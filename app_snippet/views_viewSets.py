from rest_framework import viewsets,permissions, renderers
from rest_framework.decorators import action
from rest_framework.response import Response

from django.contrib.auth.models import User   # model
from .models import Snippet
from . import serializers_viewSets
from .permissions import IsOwnerOrReadOnly

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    # serializer_class = UserSerializer
    serializer_class = serializers_viewSets.UserModelSerializer



class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Snippet.objects.all()
    # serializer_class = SnippetSerializer
    serializer_class = serializers_viewSets.SnippetModelSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)