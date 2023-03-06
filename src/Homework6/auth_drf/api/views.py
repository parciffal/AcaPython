from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import (
    LoginSerializer, RegistrationSerializer, UserSerializer,
)

from .renderer import UserJSONRenderer
from .tools.email_tools import my_send_email
from .tools.verify_tools import generate_verify_code
from .tools.http_tools import ok_status

import json

class ActivateAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    def post(self, request):
        try:
            data = json.loads(request.body.decode("utf-8"))
            user = self.serializer_class.objects.get(pk=data['user_id'])
        except KeyError:
            return  Response({"status": "User does not exist"})
        else:
            if data['verify_code'] == user.verify_code:
                user.is_active = True
                user.verify_code = 'Activate'
                user.save()
                return ok_status()

class RegistrationAPIView(APIView):
    
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer
    renderer_classes = (UserJSONRenderer,)

    def post(self, request):
        user = request.data.get('user', {})
        activate_code = generate_verify_code()
        user.verify_code = activate_code
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {}
        
        data['subject'] = 'Activate your account'
        data['message'] = 'Here is your activate code\n{}'.format(activate_code)
        data['to'] = [user.email]
        my_send_email(data)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = LoginSerializer

    def post(self, request):
        user = request.data.get('user', {})

        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        serializer_data = request.data.get('user', {})

        serializer = self.serializer_class(
            request.user, data=serializer_data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)