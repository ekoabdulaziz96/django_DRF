from rest_framework import serializers

from .models import Todo as TodoModel


class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TodoModel
        fields = ['url','activity','done']

