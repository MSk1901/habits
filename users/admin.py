from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Отображение объектов модели пользователя в админке"""
    list_display = ('email', 'is_superuser')
