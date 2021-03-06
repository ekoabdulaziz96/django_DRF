from rest_framework.response import Response
from rest_framework import generics, permissions, renderers

from .permissions import IsOwnerOrReadOnly 
from .models import Snippet
from .serializers import SnippetSerializer,SnippetModelSerializer_new, SnippetModelSerializer

class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    # serializer_class = SnippetSerializer
    # serializer_class = SnippetModelSerializer_new
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    # serializer_class = SnippetSerializer
    # serializer_class = SnippetModelSerializer
    serializer_class = SnippetModelSerializer_new

    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

class SnippetHighlight(generics.GenericAPIView):
    queryset = Snippet.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)