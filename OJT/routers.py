from rest_framework.routers import DefaultRouter
from workout.viewsets import WorkoutViewset

router = DefaultRouter()
router.register(r'workout', WorkoutViewset)