from rest_framework import serializers

from habits.models import Habit
from habits.validators import HabitTreatValidator, LinkedHabitValidator, HabitDurationValidator


class HabitSerializer(serializers.ModelSerializer):
    """Сериализотор модели привычки"""
    class Meta:
        model = Habit
        fields = '__all__'
        read_only_fields = ['owner']
        validators = [
            HabitTreatValidator(field='treat'),
            LinkedHabitValidator(field='linked_habit'),
            HabitDurationValidator(field='duration')
        ]
