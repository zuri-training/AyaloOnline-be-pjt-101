from django.db import models
from django.conf import settings
from productlisting_api.models import Product

# Create your models here.


class Order(models.Model):
	Customer=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	# Seller=models.ForeignKey(ModelLeesee, on_delete=models.CASCADE)
	Quantity=models.IntegerField()
	Product=models.ForeignKey('productlisting_api.Product', on_delete=models.CASCADE)
	Date_of_order=models.DateField(auto_now_add=True)
	Time_of_order=models.TimeField(auto_now_add=True)
	choice=[('Pick-up', 'Pick-up'), ('House delivery', 'House delivery')]
	Delivery=models.CharField(max_length=256, choices=choice)
	Date_of_return=models.DateTimeField()