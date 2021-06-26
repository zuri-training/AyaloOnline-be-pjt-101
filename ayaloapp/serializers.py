from rest_framework import serializers
<<<<<<< HEAD
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
=======
from .models import  MyUser
from django.contrib.auth.validators	import UnicodeUsernameValidator
from .customvalidators import EmailSerializerUniquenessValidator, UsernameSerializerUniquenessValidator	
from phone_verify.serializers import PhoneSerializer

class UserSerializer(serializers.Serializer):
		choicess=[('Leeser', 'Leeser'), ('Leesee', 'Leessee')]
		username=serializers.CharField(validators=[UnicodeUsernameValidator(), UsernameSerializerUniquenessValidator()])
		email=serializers.EmailField(validators=[EmailSerializerUniquenessValidator()])
		password=serializers.CharField()
		AccountType=serializers.ChoiceField(choices=choicess, allow_blank=False)
			


# class CompleteProfileSerializer(serializer.Serializer, PhoneSerializer):

# 		First_name=serializers.CharField()
# 		Last_name=serializers.CharField()
# 		gender_choices=[('F', 'Female'), ('M', 'Male')]
# 		Gender=serializers.CharField(max_length=2, choices=gender_choices)
>>>>>>> 5fae535ab9faf9a9b98ef1f242e69896ef63b07c

