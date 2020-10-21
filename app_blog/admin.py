from django.contrib import admin

from .models_artikel import Artikel as ArtikelModel
from .models import Todo as TodoModel

admin.site.register([ArtikelModel,TodoModel])
