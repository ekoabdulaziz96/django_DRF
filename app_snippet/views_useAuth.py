
from rest_framework import generics
from rest_framework import permissions

from .serializers_user import UserSerializer, UserModelSerializer
from django.contrib.auth.models import User   # model
from .permissions import IsOwnerOrReadOnly 

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    # serializer_class = UserSerializer
    serializer_class = UserModelSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    # serializer_class = UserSerializer
    serializer_class = UserModelSerializer