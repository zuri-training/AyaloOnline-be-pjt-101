from django.db import models
from ayaloapp.models import ModelLeesee
from django.conf import settings


class Category(models.Model):
    title = models.CharField(max_length=250)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title

class Product(models.Model):
    Leesee=models.ForeignKey('ayaloapp.ModelLeesee', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name='Name of product')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category')
    location = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.IntegerField(verbose_name='Rental fee')
    picture = models.ImageField('/media')
    description = models.TextField()
    status = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True)
    

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return '{}'.format(self.name)

class ProductBookmark(models.Model):
    User=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Product=models.ForeignKey(Product, on_delete=models.CASCADE)