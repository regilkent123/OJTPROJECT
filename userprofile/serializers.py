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
    fullname = serializers.CharField(source='user.get_full_name', required=False, read_only=True)
    email = serializers.CharField(source='user.email', required=False, read_only=True)


class UserSerializer(serializers.ModelSerializer):
    detail_url = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username','first_name','last_name','detail_url','email', 'fullname']

    fullname = serializers.CharField(source='get_full_name', required=False)