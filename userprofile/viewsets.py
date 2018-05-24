from rest_framework import viewsets
from .models import UserProfile, User
from .serializers import UserProfileSerializer, UserSerializer

class UserProfileViewset(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer