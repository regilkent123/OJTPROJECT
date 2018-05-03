from rest_framework import serializers
from .models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
	detail_url = serializers.CharField(read_only=True)

	class Meta:
		model = UserProfile
		fields = '__all__'