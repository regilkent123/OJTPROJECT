from rest_framework import viewsets
from .models import Workout, WorkoutVideo
from .serializers import WorkoutSerializer, WorkoutVideoSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class WorkoutViewset(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

    def create(self, request):
        serializer = WorkoutSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()        
        return Response()

    def get_object(self, pk):
        return Workout.objects.get(pk=pk)

    def retrieve(self, request, pk):
        work = self.get_object(pk)
        serializer = WorkoutSerializer(work)
        return Response(serializer.data)

class WorkoutVideoViewset(viewsets.ModelViewSet):
    queryset = WorkoutVideo.objects.all()
    serializer_class = WorkoutVideoSerializer

    def create(self, request):
        serializer = WorkoutVideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
        return Response()