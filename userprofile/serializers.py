from rest_framework import serializers
from .models import UserProfile, User

class UserProfileSerializer(serializers.ModelSerializer):
    detail_url = serializers.CharField(read_only=True)

    class Meta:
        model = UserProfile
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    detail_url = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = '__all__'
