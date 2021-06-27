import binascii
import os
from django.db import models
from authemail.models import EmailUserManager
from authemail.models import EmailAbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
# Create your models here.
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.core.mail.message import EmailMultiAlternatives
# from authemail.models import SignupCodeManager, AbstractBaseCode, SignupCode 





def _generate_code():
    return binascii.hexlify(os.urandom(20)).decode('utf-8')

class MyUser(EmailAbstractUser):
<<<<<<< HEAD
    choicess = [(1, 'Leeser'), (2, 'leasee')]
    AccountType = models.CharField(max_length=2, choices=choicess)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    username = models.CharField(
=======
		choicess=[('Leeser', 'Leeser'), ('Leesee', 'Leessee')]
		AccountType=models.CharField(max_length=256, choices=choicess)
		email = models.EmailField(
		    verbose_name='email address',
		    max_length=255,
		    unique=True
	
		)
		cool_name = models.CharField(
		verbose_name='Username',
>>>>>>> 5fae535ab9faf9a9b98ef1f242e69896ef63b07c
        max_length=150,
        validators=[UnicodeUsernameValidator]
   
    )
<<<<<<< HEAD
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password', 'username']

    objects = EmailUserManager()


class Category(models.Model):
    title = models.CharField(max_length=250)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title


class Product(models.Model):
    product_tag = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    brand_name = models.CharField(150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.IntegerField()
    picture = models.URLField()
    description = models.TextField()
    status = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True)
=======


		# First_name=models.CharField(verbose_name='First Name')
		# Last_name=models.CharField(verbose_name='Last Name')
		# gender_choices=[('F', 'Female'), ('M', 'Male')]
		# Gender=models.CharField(max_length=2, choices=gender_choices)
		# Phone_number=models.CharField()
<<<<<<< HEAD
		# USERNAME_FIELD = 'email'
		# REQUIRED_FIELDS = ['password', 'username']
>>>>>>> 5fae535ab9faf9a9b98ef1f242e69896ef63b07c
=======
		USERNAME_FIELD = 'email'
		
>>>>>>> 91dd32c46fc337f92001517e5da2bf5be7dbb913

    class Meta:
        ordering = ['-date_created']

<<<<<<< HEAD
    def __str__(self):
        return '{} {}'.format(self.product_tag, self.name)
=======
		def UserGrouper(self):
			if self.AccountType=='Leeser':
				is_vendor=True
			elif self.AccountType=='Leesee':
				is_vendor=False

			return is_vendor

<<<<<<< HEAD
>>>>>>> 5fae535ab9faf9a9b98ef1f242e69896ef63b07c
=======






# class CustomSignupCodeManager(SignupCodeManager):
# 	def create_signup_code(self, user):
# 		code = _generate_code()
# 		signup_code = self.create(user=user, code=code)

# 		return signup_code




# class CustomSignupCode(SignupCode):
# 		SignupCode.ipaddr= models.GenericIPAddressField(null=True)

# 		objects = CustomSignupCodeManager()

 
>>>>>>> 91dd32c46fc337f92001517e5da2bf5be7dbb913
