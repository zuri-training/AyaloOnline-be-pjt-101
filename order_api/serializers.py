from rest_framework import serializers
from .model import Order

class Orderserializer(serializers.ModelSerializer):
	class Meta:
		model=Order
		exclude=['Product']