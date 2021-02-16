from django.db import models

# Create your models here.

class Book(models.Model):
    code = models.IntegerField(blank=False, null=False)
    name = models.CharField(max_length=255, blank=False, null=False)
    slug = models.SlugField(max_length=255, blank=False, null=False)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField(default=0, null=False, blank=False)
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    