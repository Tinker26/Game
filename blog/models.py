from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField(default="")
    category = models.ForeignKey('Categorya', related_name="categorya", on_delete=models.PROTECT)
    image = models.ImageField(upload_to = 'BlogPhotoes/products')
    data = models.CharField(max_length=300)

    class Meta():
        verbose_name = 'blog'
        verbose_name_plural = 'Blog'
        ordering = ['name']

    def __str__(self):
        return self.name

class Categorya(models.Model):
    name = models.CharField(max_length=300) 

    class Meta():
        ordering = ['name']

    class Meta():
        verbose_name = 'Categorya'
        verbose_name_plural = 'Categoryalar'
        ordering = ['name']

    def __str__(self):
        return self.name