from rest_framework import serializers
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

