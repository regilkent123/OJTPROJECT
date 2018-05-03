from rest_framework.routers import DefaultRouter
from userprofile.viewsets import UserProfileViewset

router = DefaultRouter()
router.register(r'userprofile', UserProfileViewset)