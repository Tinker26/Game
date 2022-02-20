from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
class Komandalar(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField(default="")
    data = models.DateField()
    category = models.ForeignKey('Category', related_name="category", on_delete=models.PROTECT)
    image = models.CharField(max_length=300)
    achko = models.IntegerField()
    class Meta():
        verbose_name = 'Komanda'
        verbose_name_plural = 'Komandalar'
        ordering = ['name']

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=300) 

    class Meta():
        ordering = ['name']

    class Meta():
        verbose_name = 'Categorya'
        verbose_name_plural = 'Categoryalar'
        ordering = ['name']

    def __str__(self):
        return self.name


class Blog(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField(default="")
    category = models.ForeignKey('Category', related_name="categorya", on_delete=models.PROTECT)
    image = models.ImageField(upload_to = 'photoes/products')

    class Meta():
        verbose_name = 'blog'
        verbose_name_plural = 'Blog'
        ordering = ['name']

    def __str__(self):
        return self.name