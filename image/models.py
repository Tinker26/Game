from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField(default="")
    category = models.ForeignKey('Categoryas', related_name="categoryas", on_delete=models.PROTECT)
    image = models.CharField(max_length=300)
    data = models.CharField(max_length=300)

    class Meta():
        verbose_name = 'Rasm'
        verbose_name_plural = 'Rasmlar'
        ordering = ['name']

    def __str__(self):
        return self.name


class Categoryas(models.Model):
    name = models.CharField(max_length=300) 

    class Meta():
        ordering = ['name']

    class Meta():
        verbose_name = 'Categorya'
        verbose_name_plural = 'Categoryalar'
        ordering = ['name']

    def __str__(self):
        return self.name
