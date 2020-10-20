from django.shortcuts import render
from django.http import JsonResponse

from rest_framework import routers, serializers, viewsets
from rest_framework import generics, filters, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from rest_framework.views import APIView
from rest_framework import status

import json
import pandas as pd

from django.contrib.auth.models import User

# Create your views here.
class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            "Jajal Api": reverse('ini-api', request=request),
            "nyobo url parameter": reverse('nyobo', request=request),
            # "Test Electrical -> Turn Ratio": reverse('be:get-te-turn-ratio', request=request),
            # "----------------------------------------------------------------------------------,

        })

def index(request):
    return JsonResponse('ok', safe=False)

def ini_api(request):
    query_params = request.query_params
    ngomong = query_params.get('ngomong', None)

    return JsonResponse(ngomong, safe=False)



class Coba(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        # snippets = Snippet.objects.all()
        # serializer = SnippetSerializer(snippets, many=True)
        # return Response(serializer.data)

        query_params = request.query_params
        ngomong = query_params.get('ngomong', None)

        return JsonResponse(ngomong, safe=False)

    # def post(self, request, format=None):
    #     serializer = SnippetSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer