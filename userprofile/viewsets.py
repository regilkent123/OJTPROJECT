from rest_framework import viewsets
from .models import UserProfile, User
from .serializers import UserProfileSerializer, UserSerializer
from rest_framework.response import Response

class UserProfileViewset(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def retrieve(self, request, pk):
        profile = request.user.userprofile
        serializer = UserProfileSerializer(profile)
        return Response(serializer.data)

    def update(self, request, pk):
        profile = request.user.userprofile
        serializer = UserProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save();
        return Response()

class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def retrieve(self, request, pk):
        profile = request.user
        serializer = UserSerializer(profile)
        return Response(serializer.data)