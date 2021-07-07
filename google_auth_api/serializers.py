from rest_framework import serializers
from . import google
from .register import register_social_user
import os
from rest_framework.exceptions import AuthenticationFailed



class GoogleSocialAuthSerializer(serializers.Serializer):
    choicess=[('Leeser', 'Leeser'), ('Leesee', 'Leessee')]
    auth_token = serializers.CharField()
    AccountType=serializers.ChoiceField(choices=choicess, allow_blank=False)

    def validate(self, data):
        user_data = google.Google.validate(data['auth_token'])
        try:
            user_data['sub']
        except:
            raise serializers.ValidationError(
                'The token is invalid or expired. Please login again.'
            )

        if user_data['aud'] != os.environ.get('GOOGLE_CLIENT_ID'):

            raise AuthenticationFailed('oops, who are you?')

        user_id = user_data['sub']
        email = user_data['email']
        name = user_data['name']
        provider = 'google'

        return register_social_user(
            provider=provider, user_id=user_id, email=email, name=name, AccountType=data['AccountType'] )


