from rest_framework import generics

from habits.models import Habit
from habits.permissions import OwnerPermission
from habits.serializers import HabitSerializer


class HabitCreateAPIView(generics.CreateAPIView):
    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [OwnerPermission]


class HabitUpdateAPIView(generics.UpdateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [OwnerPermission]


class HabitDestroyAPIView(generics.DestroyAPIView):
    queryset = Habit.objects.all()
    permission_classes = [OwnerPermission]
