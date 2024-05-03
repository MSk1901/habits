from celery import shared_task

from habits.services import remind_of_habit


@shared_task
def habit_reminder(habit_id):
    """
    Таск Celery для напоминания о выполнении привычки
    :param habit_id: id объекта привычки (Habit)
    """
    remind_of_habit(habit_id)
