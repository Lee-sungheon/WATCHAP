from rest_framework import serializers
from django.contrib.auth import get_user_model
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
from urllib.parse import quote_plus
import random


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'profileurl')

class UserFollowSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    followers = UserSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'profileurl' ,'followings', 'followers')