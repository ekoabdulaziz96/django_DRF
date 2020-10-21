from django.db import models
from django.utils.text import slugify
# from django.http import JsonResponse


class Todo(models.Model):
    activity = models.TextField(max_length=200,default='-')
    done = models.BooleanField(default=False)

    slug = models.SlugField(blank=True, editable=False)

    def save(self, **kwargs):
        self.slug = slugify(self.activity)
        super(Todo, self).save()

    def __str__(self):
        return "[{}] {}".format(self.id,self.activity)