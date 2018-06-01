from rest_framework import serializers
from .models import UserProfile, User

class UserProfileSerializer(serializers.ModelSerializer):
    detail_url = serializers.CharField(read_only=True)


    class Meta:
        model = UserProfile
        fields = '__all__'


    user_type = serializers.CharField(source='get_usertype_display', required=False)
    usertype = serializers.ChoiceField(choices=UserProfile.utype)
    sex = serializers.CharField(source='get_gender_display', required=False)
    gender = serializers.ChoiceField(choices=UserProfile.sex)
    birthdate = serializers.DateField(format="%Y-%m-%d")


class UserSerializer(serializers.ModelSerializer):
    detail_url = serializers.CharField(read_only=True)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','detail_url','email']