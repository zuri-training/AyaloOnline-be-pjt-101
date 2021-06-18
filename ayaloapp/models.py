from django.db import models
from authemail.models import EmailUserManager
from authemail.models import EmailAbstractUser
# Create your models here.
 
class MyUser(EmailAbstractUser):
   objects=EmailUserManager
