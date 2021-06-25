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

# from .models import SignupCode
from authemail.models import SignupCode
from .models import send_multi_format_email


# Create your views here.

class Signup(APIView):
	permission_classes = (AllowAny,)
	serializer_class = UserSerializer

	def post(self, request, format=None):
		serializer = self.serializer_class(data=request.data)

		if serializer.is_valid():
			cool_name = serializer.data['username']
			email = serializer.data['email']
			password = serializer.data['password']
			AccountType = serializer.data['AccountType']

			must_validate_email = getattr(settings, "AUTH_EMAIL_VERIFICATION", True)

			try:
				user = get_user_model().objects.get(email=email)
				if user.is_verified:
					content = {'detail': _('Email address already taken.')}
					return Response(content, status=status.HTTP_400_BAD_REQUEST)

				try:
				# Delete old signup codes
					signup_code =SignupCode.objects.get(user=user)
					signup_code.delete()
				except SignupCode.DoesNotExist:
					pass

			except get_user_model().DoesNotExist:
				user = get_user_model().objects.create_user(email=email)

			try:
				user = get_user_model().objects.get(cool_name=cool_name)
				if user.is_verified:
					content = {'detail': _('Username already taken.')}
					return Response(content, status=status.HTTP_400_BAD_REQUEST)

			except:
				pass



			user.set_password(password)
			user.cool_name =cool_name
			user.AccountType =AccountType
			if not must_validate_email:
				user.is_verified = True
				send_multi_format_email('welcome_email',
							{'email': user.email, },
							target_email=user.email)

			user.save()


			if must_validate_email:
				# Create and associate signup code
				# ipaddr = self.request.META.get('REMOTE_ADDR', '0.0.0.0')
				signup_code = SignupCode.objects.create_signup_code(user, '127.0.0.1')
				signup_code.send_signup_email()
				# print("HEY!!!!!! LOOOK HERE!!!! {}".format(ipaddr))

			content = {'email': email, 'cool_name': cool_name,
			' AccountType':  AccountType}
			return Response(content, status=status.HTTP_201_CREATED)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





	