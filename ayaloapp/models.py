import binascii
import os
from django.db import models
from authemail.models import EmailUserManager
from authemail.models import EmailAbstractUser
from django.contrib.auth.validators	import UnicodeUsernameValidator	
# Create your models here.
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.core.mail.message import EmailMultiAlternatives
# from authemail.models import SignupCodeManager, AbstractBaseCode, SignupCode 





def _generate_code():
    return binascii.hexlify(os.urandom(20)).decode('utf-8')

class MyUser(EmailAbstractUser):
		choicess=[('Leeser', 'Leeser'), ('Leesee', 'Leessee')]
		AccountType=models.CharField(max_length=256, choices=choicess)
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


		# First_name=models.CharField(verbose_name='First Name')
		# Last_name=models.CharField(verbose_name='Last Name')
		# gender_choices=[('F', 'Female'), ('M', 'Male')]
		# Gender=models.CharField(max_length=2, choices=gender_choices)
		# Phone_number=models.CharField()
		USERNAME_FIELD = 'email'
		

		objects=EmailUserManager()

		def UserGrouper(self):
			if self.AccountType=='Leeser':
				is_vendor=True
			elif self.AccountType=='Leesee':
				is_vendor=False

			return is_vendor







# class CustomSignupCodeManager(SignupCodeManager):
# 	def create_signup_code(self, user):
# 		code = _generate_code()
# 		signup_code = self.create(user=user, code=code)

# 		return signup_code




# class CustomSignupCode(SignupCode):
# 		SignupCode.ipaddr= models.GenericIPAddressField(null=True)

# 		objects = CustomSignupCodeManager()

 