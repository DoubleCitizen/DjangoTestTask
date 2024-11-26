from django.contrib.auth import get_user_model, login
from rest_framework import generics
from rest_framework.response import Response

from user.models import User
from user.serializers import RegistrationSerializer, LoginSerializer, UserSerializer


class RegistrationView(generics.CreateAPIView):
    """Вьюшка регистрации"""
    model = User
    serializer_class = RegistrationSerializer

class ListView(generics.ListAPIView):
    """Вьюшка регистрации"""
    model = User
    serializer_class = UserSerializer
    queryset = User.objects.all()


class LoginView(generics.GenericAPIView):
    """Вьюшка авторизации"""
    model = User
    serializer_class = LoginSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        login(request=request, user=user)
        return Response(serializer.data)