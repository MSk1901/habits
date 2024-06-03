from django.urls import path

from habits.apps import HabitsConfig
from habits.views import HabitCreateAPIView, MyHabitListAPIView, PublicHabitListAPIView, \
    HabitRetrieveUpdateDestroyAPIView

app_name = HabitsConfig.name

urlpatterns = [
    path('', HabitCreateAPIView.as_view(), name='create'),
    path('<int:pk>/', HabitRetrieveUpdateDestroyAPIView.as_view(), name='habit'),
    path('my/', MyHabitListAPIView.as_view(), name='my'),
    path('public/', PublicHabitListAPIView.as_view(), name='public'),
]
