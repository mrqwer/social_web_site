from .serializers import GetCustomUserSerializer, GetCustomUserPublicSerializer
from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView, ListAPIView, UpdateAPIView
from .models import CustomUser
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

#class GetCustomUserView(ListAPIView):
#    """ Вывод профиля пользователя """
#    queryset = CustomUser.objects.all()
#    serializer_class = GetCustomeUserSerializer

#class UpdateCustomUserView(UpdateAPIView):
#    """ Редактирование пользователя """
#    serializer_class = GetCustomeUserSerializer
#    permissions_classes = [permissions.IsAuthenticated]
#
#    def get_query_set(self):
#        return CustomUser.objects.filter(id=self.request.user.id)
#

class CustomUserPublicView(ModelViewSet):
    """ Вывод публичного профиля пользователя """
    
    queryset = CustomUser.objects.all()
    serializer_class = GetCustomUserPublicSerializer
    permission_classes = [permissions.AllowAny]


class CustomUserView(ModelViewSet):
    """ Вывод профиля пользователя """
    
    serializer_class = GetCustomUserSerializer
    permissions_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return CustomUser.objects.filter(id=self.request.user.id)
