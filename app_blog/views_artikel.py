from rest_framework import viewsets
from rest_framework import permissions

# -------------------------------------------------------------Model
from .models_artikel import Artikel as ArtikelModel

# -------------------------------------------------------------Serializer
from .serializer_artikel import ArtikelSerializer

class ArtikelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ArtikelModel.objects.all().order_by('-title')
    serializer_class = ArtikelSerializer
    # permission_classes = [permissions.IsAuthenticated]