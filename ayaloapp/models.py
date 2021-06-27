from django.db import models
from authemail.models import EmailUserManager
from authemail.models import EmailAbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, AbstractUser


class MyUser(EmailAbstractUser):
		choicess=[('Leeser', 'Leeser'), ('Leesee', 'Leessee')]
		AccountType=models.CharField(max_length=256, choices=choicess)
		email = models.EmailField(
		    verbose_name='email address',
		    max_length=255,
		    unique=True,
		)
		cool_name = models.CharField(
		verbose_name='Username',

        max_length=150,
        unique=True,
        validators=[UnicodeUsernameValidator],
        error_messages={
            'unique': ("A user with that username already exists."),
        },
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password', 'username']

    objects = EmailUserManager()





		# First_name=models.CharField(verbose_name='First Name')
		# Last_name=models.CharField(verbose_name='Last Name')
		# gender_choices=[('F', 'Female'), ('M', 'Male')]
		# Gender=models.CharField(max_length=2, choices=gender_choices)
		# Phone_number=models.CharField()
		# USERNAME_FIELD = 'email'
		# REQUIRED_FIELDS = ['password', 'username']



		def UserGrouper(self):
			if self.AccountType=='Leeser':
				is_vendor=True
			elif self.AccountType=='Leesee':
				is_vendor=False

			return is_vendor


