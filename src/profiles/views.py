from .serializers import GetCustomeUserSerializer
from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView, ListAPIView, UpdateAPIView
from .models import CustomUser
from rest_framework import permissions

class GetCustomUserView(ListAPIView):
    """ Вывод профиля пользователя """
    queryset = CustomUser.objects.all()
    serializer_class = GetCustomeUserSerializer

class UpdateCustomUserView(UpdateAPIView):
    """ Редактирование пользователя """
    serializer_class = GetCustomeUserSerializer

    permissions_classes = [permissions.IsAuthenticated]

    def get_query_set(self):
        return CustomUser.objects.filter(id=self.request.user.id)

