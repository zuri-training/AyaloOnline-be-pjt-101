from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from rest_framework import serializers


class EmailSerializerUniquenessValidator(object):

  def __call__(self, value):
	  try:
	  	user = get_user_model().objects.get(email=email)
  		if user.is_verified:
      				raise serializers.ValidationError('Email address already exists!')
	  except:
	  	pass


	  return value


class UsernameSerializerUniquenessValidator(object):
	def __call__(self, value):
		try:
			user = get_user_model().objects.get(username=username)
			if user.is_verified:
				raise serializers.ValidationError('Username already taken')

		except:
			pass 
		return value

# class UsernameFormatValidator(object, RegexValidator):


