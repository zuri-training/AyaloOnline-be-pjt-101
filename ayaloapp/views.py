from django.shortcuts import render
from .serializers import  UserSerializer

from datetime import date

from django.conf import settings
from django.contrib.auth import authenticate, get_user_model
from django.utils.translation import gettext as _

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from authemail.models import SignupCode, EmailChangeCode, PasswordResetCode
from authemail.models import send_multi_format_email


# Create your views here.

class Signup(APIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            username = serializer.data['username']
            email = serializer.data['email']
            password = serializer.data['password']
            AccountType = serializer.data['AccountType']

            must_validate_email = getattr(settings, "AUTH_EMAIL_VERIFICATION", True)

            user = get_user_model().objects.create_user(email=email)


            user.set_password(password)
            user.username =username
            user.AccountType =AccountType
            if not must_validate_email:
                user.is_verified = True
                send_multi_format_email('welcome_email',
                                        {'email': user.email, },
                                        target_email=user.email)
            user.save()

            
            if must_validate_email:
                # Create and associate signup code
                ipaddr = self.request.META.get('REMOTE_ADDR', '0.0.0.0')
                signup_code = SignupCode.objects.create_signup_code(user, ipaddr)
                signup_code.send_signup_email()

            content = {'email': email, 'username': username,
                       ' AccountType':  AccountType}
            return Response(content, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

