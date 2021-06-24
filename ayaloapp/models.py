from django.db import models
from authemail.models import EmailUserManager
from authemail.models import EmailAbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, AbstractUser


class MyUser(EmailAbstractUser):
    choicess = [(1, 'Leeser'), (2, 'leasee')]
    AccountType = models.CharField(max_length=2, choices=choicess)
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

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return '{} {}'.format(self.product_tag, self.name)
