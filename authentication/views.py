from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from .serializers import RegisterSerializer
from django.conf import settings
from rest_framework import status
from django.contrib import auth
import jwt
from .serializers import UserSerializer
# Create your views here.

class RegisterView(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class LoginView(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        data = request.data
        username = data.get('username', '')
        password = data.get('password', '')
        user = auth.authenticate(username=username, password=password)

        if user:
            auth_token = jwt.encode({
                'username': user.username
            }, settings.JWT_SECRET_KEY)

            serializer = UserSerializer(user)

            data = {
                "user": serializer.data,
                "token": auth_token
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = {
                "error": "Invalid credentials"
            }
            return Response(data, status=status.HTTP_401_UNAUTHORIZED)
