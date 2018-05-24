from rest_framework.routers import DefaultRouter
from video.viewsets import WorkoutViewset
from userprofile.viewsets import UserProfileViewset, UserViewset
from workout.viewsets import WorkoutViewset

router = DefaultRouter()
router.register(r'workout', WorkoutViewset)
router.register(r'userprofile', UserProfileViewset)
router.register(r'user', UserViewset)

