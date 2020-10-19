from django.contrib import admin

from .models_artikel import Artikel as ArtikelModel

admin.site.register([ArtikelModel])
