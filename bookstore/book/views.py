from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status

class RegisterView(APIView):

    def post(self, request):
        serializer=UserSerializer(request.data)
        if serializer.is_valid():
            User.objects.create_user(
                serializer.initial_data["username"],
                serializer.initial_data["password"]
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)