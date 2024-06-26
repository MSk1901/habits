from rest_framework import generics
from rest_framework.permissions import AllowAny

from habits.models import Habit
from habits.permissions import OwnerPermission
from habits.serializers import HabitSerializer
from habits.services import create_periodic_task, update_periodic_task, delete_periodic_task


class HabitCreateAPIView(generics.CreateAPIView):
    """Представление для создания новой привычки"""
    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        habit = serializer.save(owner=self.request.user)
        create_periodic_task(habit)


class HabitRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Представление для просмотра, обновления и удаления одной привычки"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [OwnerPermission]

    def perform_update(self, serializer):
        habit = serializer.save()
        update_periodic_task(habit)

    def perform_destroy(self, instance):
        delete_periodic_task(instance)
        return super().perform_destroy(instance)


class MyHabitListAPIView(generics.ListAPIView):
    """Представление для вывода списка привычек пользователя"""
    serializer_class = HabitSerializer

    def get_queryset(self):
        user = self.request.user
        return Habit.objects.filter(owner=user).order_by('id')


class PublicHabitListAPIView(generics.ListAPIView):
    """Представление для вывода списка публичных привычек"""
    serializer_class = HabitSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Habit.objects.filter(is_public=True).order_by('id')
