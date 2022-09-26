from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import permissions, status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from serializers import serializer

from account.models import Account
from account.serializers import RegisterSerializer
from product.models import Cart


class RegisterApiView(APIView):
    permission_classes = [permissions.AllowAny]
    parser_classes = [JSONParser]

    def post(self, request):
        serializers = RegisterSerializer(data=request.data)
        if serializers.is_valid():
            user = User.objects.create(
                username=request.data['username'],
                email=request.data['email'],
            )
            user.set_password(request.data['password'])
            user.save()
            account = Account.objects.create(
                user=user,
                first_name=request.data['first_name'],
                second_name=request.data['second_name'],
                phone=request.data['phone'],
                is_vendor=request.data['is_vendor']
            )
            account.save()
            cart = Cart.objects.create(
                user=user
            )
            cart.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)



# class AccountListApiView(APIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#
#     def get(self, request):
#         users = Account.objects
#         serializer = RegisterSerialize(users, many=True)
#         return Response(serializer.data)