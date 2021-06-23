from rest_framework import serializers
from .models import  MyUser
from django.contrib.auth.validators	import UnicodeUsernameValidator
from .customvalidators import EmailSerializerUniquenessValidator, UsernameSerializerUniquenessValidator	

class UserSerializer(serializers.Serializer):
		choicess=[(1, 'Leeser'), (2, 'leesee')]
		username=serializers.CharField(validators=[UnicodeUsernameValidator(), UsernameSerializerUniquenessValidator()])
		email=serializers.EmailField(validators=[EmailSerializerUniquenessValidator()])
		password=serializers.CharField()
		AccountType=serializers.ChoiceField(choices=choicess, allow_blank=False)
			