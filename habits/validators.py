from datetime import timedelta

from rest_framework import serializers


class HabitTreatValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        treat = value.get(self.field)
        linked_habit = value.get('linked_habit')
        is_enjoyable = value.get('is_enjoyable')
        if treat and is_enjoyable:
            raise serializers.ValidationError('У приятной привычки не может быть вознаграждения')
        elif treat and linked_habit:
            raise serializers.ValidationError('У привычки может быть либо вознаграждение,'
                                              'либо приятная привычка')


class LinkedHabitValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        linked_habit = value.get(self.field)
        is_enjoyable = value.get('is_enjoyable')
        if linked_habit and is_enjoyable:
            raise serializers.ValidationError('У приятной привычки не может быть связанной привычки.')

        if linked_habit and not linked_habit.is_enjoyable:
            raise serializers.ValidationError('Связанная привычка должна быть приятной')


class HabitDurationValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        duration = value.get(self.field)
        if duration > timedelta(minutes=2):
            raise serializers.ValidationError('Время выполнения привычки не должно превышать 2 минуты')
