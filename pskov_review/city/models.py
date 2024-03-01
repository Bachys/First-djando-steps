from django.db import models


class City(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='city/images/')
    url = models.URLField(blank=True)
