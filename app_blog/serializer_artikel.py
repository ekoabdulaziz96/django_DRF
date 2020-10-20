from rest_framework import serializers

from .models_artikel import Artikel as ArtikelModel


class ArtikelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ArtikelModel
        fields = ['url','title','content']

