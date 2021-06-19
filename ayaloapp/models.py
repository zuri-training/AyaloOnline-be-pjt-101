from django.db import models
from authemail.models import EmailUserManager
from authemail.models import EmailAbstractUser
from django.contrib.auth.validators	import UnicodeUsernameValidator	
# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, AbstractUser


class MyUser(EmailAbstractUser):
		choicess=[(1, 'Leeser'), (2, 'leasee')]
		AccountType=models.CharField(max_length=2, choices=choicess)
		email = models.EmailField(
		    verbose_name='email address',
		    max_length=255,
		    unique=True,
		)
		username = models.CharField(
        max_length=150,
        unique=True,
        validators=[UnicodeUsernameValidator],
        error_messages={
            'unique': ("A user with that username already exists."),
        },
    )
		USERNAME_FIELD = 'email'
		REQUIRED_FIELDS = ['password', 'username', 'AccountType']

		objects=EmailUserManager()

