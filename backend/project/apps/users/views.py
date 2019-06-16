# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from project.apps.users.serializers import UserSerializer


class UsersView(APIView):

    @staticmethod
    def post(request):
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            username = user_serializer.validated_data['username']
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                result = {
                    'msg': 'User {} does not exists'.format(username),
                }
                status_result = status.HTTP_404_NOT_FOUND
            else:
                result = {
                    'msg': 'OK',
                    'user_info': {
                        'username': username,
                        'is_staff': user.is_staff,
                        'is_superuser': user.is_superuser,
                    },
                }
                status_result = status.HTTP_404_NOT_FOUND
            finally:
                response = Response(
                    result,
                    status=status_result,
                )

        else:
            response = Response(
                {
                    'msg': 'Request is not valid',
                    'errors': user_serializer.errors,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        return response
