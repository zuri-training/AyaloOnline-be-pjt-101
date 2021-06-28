from django.shortcuts import render
<<<<<<< HEAD
from .models import Category, Product
from .serializers import UserSerializer, CategorySerializer, ProductSerializer

=======
from .serializers import  UserSerializer
from django.template.loader import render_to_string
from django.core.mail import send_mail
>>>>>>> 91dd32c46fc337f92001517e5da2bf5be7dbb913
from datetime import date

from django.conf import settings
from django.contrib.auth import authenticate, get_user_model
from django.utils.translation import gettext as _

from rest_framework import status, generics
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

# from .models import SignupCode
from authemail.models import SignupCode



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
				# except SignupCode.MultipleObjectsReturned:
				# 	for obj in signup_code:
				# 		obj.delete()
			except get_user_model().DoesNotExist:
				user = get_user_model().objects.create_user(email=email)

			try:
				user = get_user_model().objects.get(cool_name=cool_name)
				if user.is_verified:
					content = {'detail': _('Username already taken.')}
					return Response(content, status=status.HTTP_400_BAD_REQUEST)

			except:
				pass


<<<<<<< HEAD
            user.set_password(password)
            user.username = username
            user.AccountType = AccountType
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
                       ' AccountType': AccountType}
            return Response(content, status=status.HTTP_201_CREATED)
=======

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
					template_prefix='signup_email'
					subject_file = 'authemail/%s_subject.txt' % template_prefix
					txt_file = 'authemail/%s.txt' % template_prefix
					subject = render_to_string(subject_file).strip()
					from_email = settings.EMAIL_FROM
					to = email
					context={'code':signup_code.code}
					text_content = render_to_string(txt_file, context)

					send_mail(subject, text_content, from_email, [to])
				# print("HEY!!!!!! LOOOK HERE!!!! {}".format(ipaddr))

			content = {'email': email, 'cool_name': cool_name,
			' AccountType':  AccountType}
			return Response(content, status=status.HTTP_201_CREATED)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



>>>>>>> 5fae535ab9faf9a9b98ef1f242e69896ef63b07c


<<<<<<< HEAD

class ListCategory(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class DetailCategory(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ListProduct(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class DetailProduct(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
=======
	
>>>>>>> 91dd32c46fc337f92001517e5da2bf5be7dbb913
