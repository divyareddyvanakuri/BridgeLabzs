from .models import UserModel
from rest_framework import serializers
from django.contrib.auth.models import User


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        Model = UserModel
        field = '__all__'


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        Model = User
        field = ['username', 'password']


class PasswordResetSerializer(serializers.ModelSerializer):
    class Meta:
        Model = UserModel
        field = ['email','password','confirmpassword']

class ForgotPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        Model = UserModel
        field = ['password','confirmpassword']