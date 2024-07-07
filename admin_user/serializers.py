from rest_framework import serializers
from . models import Admin_User



class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin_User
        fields = ['id', 'email', 'first_name', 'last_name', 'is_staff']
        


# serializers.py
from rest_framework import serializers
from .models import Admin_User

class AdminUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin_User
        fields = ['id', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Admin_User.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        return super().update(instance, validated_data)