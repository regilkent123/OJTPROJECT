from rest_framework import serializers
from .models import UserProfile, User

class UserProfileSerializer(serializers.ModelSerializer):
    detail_url = serializers.CharField(read_only=True)
    usertype = serializers.SerializerMethodField()
    gender = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = '__all__'

    usertype = serializers.CharField(source = 'get_usertype_display')
    gender = serializers.CharField(source = 'get_gender_display')

class UserSerializer(serializers.ModelSerializer):
    detail_url = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ['username','first_name','last_name','detail_url','email']