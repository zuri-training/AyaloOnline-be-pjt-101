from rest_framework import serializers
from .models import MyUser, Category, Product
from django.contrib.auth.validators import UnicodeUsernameValidator
from .customvalidators import EmailSerializerUniquenessValidator, UsernameSerializerUniquenessValidator


class UserSerializer(serializers.Serializer):
    choicess = [(1, 'Leeser'), (2, 'leasee')]
    username = serializers.CharField(validators=[UnicodeUsernameValidator(), UsernameSerializerUniquenessValidator()])
    email = serializers.EmailField(validators=[EmailSerializerUniquenessValidator()])
    password = serializers.CharField()
    AccountType = serializers.ChoiceField(choices=choicess, allow_blank=False)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id',
                  'title')
        model = Category


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

