from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from phone_verify.api import VerificationViewSet
from phone_verify import serializers as phone_serializers
from phone_verify.serializers import SMSVerificationSerializer

from .import serializers


class YourCustomViewSet(VerificationViewSet):

    @action(detail=False, methods=['POST'], permission_classes=[IsAuthenticated], serializer_class=SMSVerificationSerializer)
    def verify_and_register(self, request):
      

        serializer = phone_serializers.SMSVerificationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Add your custom code here.
        # An example is shown below:

        serializer = serializers.CompleteProfileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = services.create_user_account(**serializer.validated_data)

        return Response(serializer.data)