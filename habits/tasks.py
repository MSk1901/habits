from celery import shared_task

from habits.services import remind_of_habit


@shared_task
def habit_reminder(habit_id):
    remind_of_habit(habit_id)
