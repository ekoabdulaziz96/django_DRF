from django.db import models
from django.utils.text import slugify
# from django.http import JsonResponse


class Artikel(models.Model):
    title = models.CharField(max_length=200,default='-')
    content = models.TextField(default='-')

    slug = models.SlugField(blank=True, editable=False)

    def save(self, **kwargs):
        self.slug = slugify(self.title)
        super(Artikel, self).save()

    def __str__(self):
        return "[{}] Artikel berjudul {}".format(self.id,self.title)