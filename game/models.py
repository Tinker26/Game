from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
class Komandalar(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField(default="")
    data = models.DateField()
    category = models.ForeignKey('Category', related_name="category", on_delete=models.PROTECT)
    image = models.CharField(max_length=100)
    achko = models.IntegerField()
    class Meta():
        verbose_name = 'Kiyim'
        verbose_name_plural = 'Kiyimlar'
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