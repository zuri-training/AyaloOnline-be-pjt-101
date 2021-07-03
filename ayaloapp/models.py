from django.db import models
from authemail.models import EmailUserManager
from authemail.models import EmailAbstractUser
from django.contrib.auth.validators	import UnicodeUsernameValidator	
# Create your models here.
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from rest_framework_simplejwt.tokens import RefreshToken
import math
import random

# from authemail.models import SignupCodeManager, AbstractBaseCode, SignupCode 





AUTH_PROVIDERS = {'google': 'google'}


class MyUser(EmailAbstractUser):
		choicess=[('Leesee', 'Leesee'), ('Leeser', 'Leesser')]
		AccountType=models.CharField(max_length=256, choices=choicess)
		# auth_provider = models.CharField(
  #       max_length=255, blank=True,
  #       null=True, default=AUTH_PROVIDERS.get('email'))
		email = models.EmailField(
		    verbose_name='email address',
		    max_length=255,
		    unique=True
	
		)
		cool_name = models.CharField(
		verbose_name='Username',
        max_length=150,
        validators=[UnicodeUsernameValidator]
   
    )


		# First_name=models.CharField(max_length=255, verbose_name='First Name')
		# Last_name=models.CharField(max_length=255, verbose_name='Last Name')
		gender_choices=[('Female', 'Female'), ('Male', 'Male')]
		Gender=models.CharField(max_length=255, choices=gender_choices)
		Phone_number=models.CharField(max_length=255)
		is_completely_verified = models.BooleanField(default=False)
		USERNAME_FIELD = 'email'
		

		objects=EmailUserManager()
		# def tokens(self):
		# 	refresh = RefreshToken.for_user(self)
		# 	return {
		# 	'refresh': str(refresh),
		# 	'access': str(refresh.access_token)}
		# def UserGrouper(self):
		# 	if self.AccountType=='Leeser':
		# 		is_vendor=True
		# 	elif self.AccountType=='Leesee':
		# 		is_vendor=False

		# 	return is_vendor


class ModelLeesee(models.Model):
			Leesee = models.OneToOneField(MyUser, on_delete=models.CASCADE, primary_key=True)
			Business_name = models.CharField(max_length=150)
			business_address=models.CharField(max_length=150)
			CAC=models.CharField(max_length=150)
			choicess=[('BVN', 'BVN'), ('NIN', 'NIN')]
			VerificationMethod=models.CharField(max_length=256, choices=choicess)
			VerificationField=models.IntegerField()

			def __str__(self):
				return '{} , {} {}'.format(self.Business_name, self.Leesee.first_name, self.Leesee.last_name)


def generate_OTP():
	digits='0123456789'
	OTP=''
	for i in range(4):
		OTP+=digits[math.floor(random.random()*10)]
		return OTP

class TwilioTokenManager(models.Manager):
	def create_token(self, phone_number):
		Token=generate_OTP()
		self.Token=Token
		self.phone_number=phone_number

		return self.Token

class TwilioToken(models.Model):
	Token=models.IntegerField()
	Phone_number =models.CharField(max_length=150)

	objects=TwilioTokenManager()

	# def verify_token(token, phone_number, user):
	# 		Token_object=TwilioToken.objects.get(Phone_number=phone_number)
	# 		if Token_object.Token==token:
	# 			for item in temp_user:











# class CustomSignupCodeManager(SignupCodeManager):
# 	def create_signup_code(self, user):
# 		code = _generate_code()
# 		signup_code = self.create(user=user, code=code)

# 		return signup_code




# class CustomSignupCode(SignupCode):
# 		SignupCode.ipaddr= models.GenericIPAddressField(null=True)

# 		objects = CustomSignupCodeManager()

 