from rest_framework import serializers
# ModelSerialize
from .models import CustomUser

class GetCustomeUserSerializer(serializers.ModelSerializer):
    """"""

    class Meta:
        model = CustomUser
        exclude = ("password", "last_login", "is_active", "is_staff", "is_superuser")