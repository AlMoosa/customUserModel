from django.shortcuts import render
from rest_framework import viewsets

from userapi.models import User
from userapi.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
