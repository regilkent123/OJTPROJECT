from django.contrib import admin
from django.urls import path, include
from .routers import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('userprofile.urls')),
    path('', include('videostream.urls')),
    path('', include('workout.urls')),
    path('', include('video.urls')),
    path('api/', include(router.urls)),
]