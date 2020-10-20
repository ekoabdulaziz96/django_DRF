from django.contrib import admin

from .models import Snippet as SnippetModel

admin.site.register([SnippetModel])