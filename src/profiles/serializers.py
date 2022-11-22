from rest_framework import serializers
# ModelSerialize
from .models import CustomUser

class GetCustomUserSerializer(serializers.ModelSerializer):
    """"""
    avatar = serializers.ImageField(write_only=True)
    
    class Meta:
        model = CustomUser
        exclude = ("groups",
                    "user_permissions", 
                    "password", 
                    "last_login", 
                    "is_active", 
                    "is_staff", 
                    "is_superuser"
                    )


class GetCustomUserPublicSerializer(serializers.ModelSerializer):
    """  """
    
    class Meta:
        model = CustomUser
        exclude = ("phone",
                    "groups", 
                    "user_permissions", 
                    "email", 
                    "password", 
                    "last_login", 
                    "is_active", 
                    "is_staff", 
                    "is_superuser"
                    )