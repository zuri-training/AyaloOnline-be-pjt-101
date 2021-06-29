from django.shortcuts import render
from .serializers import  UserSerializer
from django.template.loader import render_to_string
from django.core.mail import send_mail
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



			user.set_password(password)
			user.cool_name =cool_name
			user.AccountType =AccountType
			if not must_validate_email:
				user.is_verified = True
				template_prefix='welcome_email'
				subject_file = 'templates/%s_subject.txt' % template_prefix
				txt_file = 'templates/%s.txt' % template_prefix
				subject = render_to_string(subject_file).strip()
				from_email = settings.EMAIL_FROM
				to = email
				context={'code':signup_code.code}
				text_content = render_to_string(txt_file, context)

				send_mail(subject, text_content, from_email, [to])

			user.save()


			if must_validate_email:
				# Create and associate signup code
				# ipaddr = self.request.META.get('REMOTE_ADDR', '0.0.0.0')
					signup_code = SignupCode.objects.create_signup_code(user, '127.0.0.1')
					template_prefix='signup_email'
					subject_file = '%s_subject.txt' % template_prefix
					txt_file = '%s.txt' % template_prefix
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
from authemail.serializers import SignupSerializer, LoginSerializer
from authemail.serializers import PasswordResetSerializer
from authemail.serializers import PasswordResetVerifiedSerializer
from authemail.serializers import EmailChangeSerializer
from authemail.serializers import PasswordChangeSerializer
from authemail.serializers import UserSerializer



class SignupVerify(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        code = request.GET.get('code', '')
        verified = SignupCode.objects.set_user_is_verified(code)

        if verified:
            try:
                signup_code = SignupCode.objects.get(code=code)
                signup_code.delete()
            except SignupCode.DoesNotExist:
                pass
            content = {'success': _('Email address verified.')}
            return Response(content, status=status.HTTP_200_OK)
        else:
            content = {'detail': _('Unable to verify user.')}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)


class Login(APIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            email = serializer.data['email']
            password = serializer.data['password']
            user = authenticate(email=email, password=password)

            if user:
                if user.is_verified:
                    if user.is_active:
                        token, created = Token.objects.get_or_create(user=user)
                        return Response({'token': token.key},
                                        status=status.HTTP_200_OK)
                    else:
                        content = {'detail': _('User account not active.')}
                        return Response(content,
                                        status=status.HTTP_401_UNAUTHORIZED)
                else:
                    content = {'detail':
                               _('User account not verified.')}
                    return Response(content, status=status.HTTP_401_UNAUTHORIZED)
            else:
                content = {'detail':
                           _('Unable to login with provided credentials.')}
                return Response(content, status=status.HTTP_401_UNAUTHORIZED)

        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class Logout(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        """
        Remove all auth tokens owned by request.user.
        """
        tokens = Token.objects.filter(user=request.user)
        for token in tokens:
            token.delete()
        content = {'success': _('User logged out.')}
        return Response(content, status=status.HTTP_200_OK)


class PasswordReset(APIView):
	permission_classes = (AllowAny,)
	serializer_class = PasswordResetSerializer

	def post(self, request, format=None):
		serializer = self.serializer_class(data=request.data)

		if serializer.is_valid():
			email = serializer.data['email']

			try:
				user = get_user_model().objects.get(email=email)

				# Delete all unused password reset codes
				PasswordResetCode.objects.filter(user=user).delete()

				if user.is_verified and user.is_active:
					password_reset_code = PasswordResetCode.objects.create_password_reset_code(user)
					context={'code':password_reset_code.code}
					template_prefix='password_reset_email'
					subject_file = '%s_subject.txt' % template_prefix
					txt_file = '%s.txt' % template_prefix
					subject = render_to_string(subject_file).strip()
					from_email = settings.EMAIL_FROM
					to = email
					context={'code':signup_code.code}
					text_content = render_to_string(txt_file, context)

					send_mail(subject, text_content, from_email, [to])
					content = {'email': email}
					return Response(content, status=status.HTTP_201_CREATED)

			except get_user_model().DoesNotExist:
				pass

			# Since this is AllowAny, don't give away error.
			content = {'detail': _('Password reset not allowed.')}
			return Response(content, status=status.HTTP_400_BAD_REQUEST)

		else:
			return Response(serializer.errors,
			status=status.HTTP_400_BAD_REQUEST)


class PasswordResetVerify(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        code = request.GET.get('code', '')

        try:
            password_reset_code = PasswordResetCode.objects.get(code=code)

            # Delete password reset code if older than expiry period
            delta = date.today() - password_reset_code.created_at.date()
            if delta.days > PasswordResetCode.objects.get_expiry_period():
                password_reset_code.delete()
                raise PasswordResetCode.DoesNotExist()

            content = {'success': _('Email address verified.')}
            return Response(content, status=status.HTTP_200_OK)
        except PasswordResetCode.DoesNotExist:
            content = {'detail': _('Unable to verify user.')}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)


class PasswordResetVerified(APIView):
    permission_classes = (AllowAny,)
    serializer_class = PasswordResetVerifiedSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            code = serializer.data['code']
            password = serializer.data['password']

            try:
                password_reset_code = PasswordResetCode.objects.get(code=code)
                password_reset_code.user.set_password(password)
                password_reset_code.user.save()

                # Delete password reset code just used
                password_reset_code.delete()

                content = {'success': _('Password reset.')}
                return Response(content, status=status.HTTP_200_OK)
            except PasswordResetCode.DoesNotExist:
                content = {'detail': _('Unable to verify user.')}
                return Response(content, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class EmailChange(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = EmailChangeSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user = request.user

            # Delete all unused email change codes
            EmailChangeCode.objects.filter(user=user).delete()

            email_new = serializer.data['email']

            try:
                user_with_email = get_user_model().objects.get(email=email_new)
                if user_with_email.is_verified:
                    content = {'detail': _('Email address already taken.')}
                    return Response(content, status=status.HTTP_400_BAD_REQUEST)
                else:
                    # If the account with this email address is not verified,
                    # give this user a chance to verify and grab this email address
                    raise get_user_model().DoesNotExist

            except get_user_model().DoesNotExist:
                email_change_code = EmailChangeCode.objects.create_email_change_code(user, email_new)

                email_change_code.send_email_change_emails()

                content = {'email': email_new}
                return Response(content, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class EmailChangeVerify(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        code = request.GET.get('code', '')

        try:
            # Check if the code exists.
            email_change_code = EmailChangeCode.objects.get(code=code)

            # Check if the code has expired.
            delta = date.today() - email_change_code.created_at.date()
            if delta.days > EmailChangeCode.objects.get_expiry_period():
                email_change_code.delete()
                raise EmailChangeCode.DoesNotExist()

            # Check if the email address is being used by a verified user.
            try:
                user_with_email = get_user_model().objects.get(email=email_change_code.email)
                if user_with_email.is_verified:
                    # Delete email change code since won't be used
                    email_change_code.delete()

                    content = {'detail': _('Email address already taken.')}
                    return Response(content, status=status.HTTP_400_BAD_REQUEST)
                else:
                    # If the account with this email address is not verified,
                    # delete the account (and signup code) because the email
                    # address will be used for the user who just verified.
                    user_with_email.delete()
            except get_user_model().DoesNotExist:
                pass

            # If all is well, change the email address.
            email_change_code.user.email = email_change_code.email
            email_change_code.user.save()

            # Delete email change code just used
            email_change_code.delete()

            content = {'success': _('Email address changed.')}
            return Response(content, status=status.HTTP_200_OK)
        except EmailChangeCode.DoesNotExist:
            content = {'detail': _('Unable to verify user.')}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)


class PasswordChange(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PasswordChangeSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user = request.user

            password = serializer.data['password']
            user.set_password(password)
            user.save()

            content = {'success': _('Password changed.')}
            return Response(content, status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class UserMe(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get(self, request, format=None):
        return Response(self.serializer_class(request.user).data)


	