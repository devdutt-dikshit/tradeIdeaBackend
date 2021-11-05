from rest_framework import fields, serializers 
from django.contrib.auth.models import User
from .models import *
import re


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']

class CryptoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crypto
        fields = '__all__'



class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user


class TradeIdeaSerializer(serializers.ModelSerializer):
    createdBy = UserSerializer()
    crypto = CryptoSerializer()
    class Meta:
        model = TradeIdea
        fields = '__all__'

