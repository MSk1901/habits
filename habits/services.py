import json

import requests

from django.conf import settings
from django.utils import timezone
from django_celery_beat.models import IntervalSchedule, PeriodicTask

from habits.models import Habit


def remind_of_habit(habit_id):
    habit = Habit.objects.get(pk=habit_id)
    if habit.owner.chat_id:
        message = f'''Привет!\nНе забудь сегодня выполнить привычку: 
"{habit.action}" в {habit.time.strftime("%H:%M")}
Место: {habit.place}'''
        send_tg_message(message, habit.owner.chat_id)


def send_tg_message(message, chat_id):
    params = {
        'text': message,
        'chat_id': chat_id
    }
    try:
        response = requests.get(f'https://api.telegram.org/bot{settings.TG_BOT_TOKEN}/sendMessage', params=params)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Ошибка при отправке сообщения в Telegram: {e}")

    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")


def create_periodic_task(habit):
    schedule, created = IntervalSchedule.objects.get_or_create(
        every=habit.periodicity,
        period=IntervalSchedule.DAYS,
    )
    PeriodicTask.objects.create(
        interval=schedule,
        name=f'Send Habit {habit.pk} notification',
        task='habits.tasks.habit_reminder',
        kwargs=json.dumps({
            'habit_id': habit.pk,
        }),
        start_time=timezone.now()
    )


def update_periodic_task(habit):
    schedule, created = IntervalSchedule.objects.get_or_create(
        every=habit.periodicity,
        period=IntervalSchedule.DAYS,
    )

    task = PeriodicTask.objects.filter(name=f'Send Habit {habit.pk} notification').first()
    if task:
        task.interval = schedule
        task.save()
    else:
        create_periodic_task(habit)


def delete_periodic_task(habit):
    PeriodicTask.objects.filter(name=f'Send Habit {habit.pk} notification').delete()
