from rest_framework import serializers
from rest_framework.reverse import reverse

from django.contrib.auth.models import User
from .models import Snippet

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
    # snippets = serializers.HyperlinkedRelatedField(many=True, view_name='as:snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']

class UserModelSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='as:snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets']