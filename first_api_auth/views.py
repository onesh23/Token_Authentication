from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


def get_student(request):
    if request.method == 'GET':
        username = request.GET.get('username')
        try:
            user = User.objects.get(username=username)
            user = authenticate(username = 'admin',password = 'admin')
            token = Token.objects.get_or_create(user=user)
        except:
            return Response({"message":"Invalid Useraname And password",
                                'status' : status.HTTP_404_NOT_FOUND
                            })
        return Response({
             'username': username,
             'token':token.key , 
             'status' : status.HTTP_200_OK
        })

