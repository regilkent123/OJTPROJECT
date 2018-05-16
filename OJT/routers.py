from rest_framework.routers import DefaultRouter
from userprofile.viewsets import UserProfileViewset, UserViewset

router = DefaultRouter()
router.register(r'userprofile', UserProfileViewset)
router.register(r'user', UserViewset)