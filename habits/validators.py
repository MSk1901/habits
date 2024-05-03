from datetime import timedelta

from rest_framework import serializers


class HabitTreatValidator:
    """
    Валидатор поля treat (вознаграждение)
    Проверяет условия:
    - В модели не должно быть заполнено одновременно и поле вознаграждения, и поле связанной привычки.
    Можно заполнить только одно из двух полей.
    - У приятной привычки не может быть вознаграждения.
    """
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
    """
    Валидатор поля связанной приятной привычки (is_enjoyable)
    Проверяет условия:
    - У приятной привычки не может быть связанной привычки.
    - В связанные привычки могут попадать только привычки с признаком приятной привычки.
    """
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
    """
    Валидатор поля времени выполнения (duration)
    Проверяет условие:
    - Время выполнения привычки должно быть не больше 120 секунд.
    """
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        duration = value.get(self.field)
        if duration and duration > timedelta(minutes=2):
            raise serializers.ValidationError('Время выполнения привычки не должно превышать 2 минуты')
