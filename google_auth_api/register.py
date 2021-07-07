
from django.contrib.auth import authenticate
from ayaloapp.models import MyUser
import os
import random
from rest_framework.exceptions import AuthenticationFailed


def generate_username(name):

    username = "".join(name.split(' ')).lower()
    if not MyUser.objects.filter(username=username).exists():
        return username
    else:
        random_username = username + str(random.randint(0, 1000))
        return generate_username(random_username)


def register_social_user(provider, user_id, email, name, AccountType):
    filtered_user_by_email = MyUser.objects.filter(email=email)

    if filtered_user_by_email.exists():

        if provider == filtered_user_by_email[0].auth_provider:

            registered_user = authenticate(
                email=email, password=os.environ.get('SOCIAL_SECRET'))

            return {
                'cool_name': registered_user.username,
                'email': registered_user.email,
                'tokens': registered_user.tokens(),
                'AccountType':registered_user.AccountType}

        else:
            raise AuthenticationFailed(
                detail='Please continue your login using ' + filtered_user_by_email[0].auth_provider)

    else:
        user = {
            'cool_name': generate_username(name), 'email': email,
            'password': os.environ.get('SOCIAL_SECRET'),'AccountType':AccountType}
        user = MyUser.objects.create_user(**user)
        user.is_verified = True
        user.auth_provider = provider
        user.save()

        new_user = authenticate(
            email=email, password=os.environ.get('SOCIAL_SECRET'))


        return {
            'email': new_user.email,
            'username': new_user.cool_name,
            'tokens': new_user.tokens(),
            'AccountType':AccountType
        }
