from django.shortcuts import render, get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import UserSerializer, UserUpdateSerializer
from .models import User

class AccountSignupAPIView(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def delete(self, request):
        self.permission_classes = [IsAuthenticated]
        user = request.user 
        password = request.data['password']
        if user.check_password(password):
            user.delete()
            return Response(status=status.HTTP_200_OK)


class AccountDetailAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    def put(self, request, username):
        instance = get_object_or_404(User, username=username)
        serializer = UserUpdateSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

class AccountPasswordAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def put(self, request):
        user = request.user
        old_password = request.data['old_password']
        new_password = request.data['new_password']
        if user.check_password(old_password):
            if not old_password == new_password:
                user.set_password(new_password)
                user.save()
                return Response(status=status.HTTP_200_OK)
                