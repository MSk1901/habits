# Generated by Django 5.0.4 on 2024-05-04 07:47

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0002_alter_habit_options_alter_habit_periodicity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='duration',
            field=models.DurationField(validators=[django.core.validators.MaxValueValidator(datetime.timedelta(seconds=120))], verbose_name='время на выполнение'),
        ),
    ]