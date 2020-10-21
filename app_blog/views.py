from rest_framework import viewsets
from rest_framework import permissions

# -------------------------------------------------------------Model
from .models import Todo as TodoModel

# -------------------------------------------------------------Serializer
from .serializer import TodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = TodoModel.objects.all().order_by('-activity')
    serializer_class = TodoSerializer
    # permission_classes = [permissions.IsAuthenticated]