# Generated by Django 5.0.4 on 2024-04-30 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='habit',
            options={'verbose_name': 'привычка', 'verbose_name_plural': 'привычки'},
        ),
        migrations.AlterField(
            model_name='habit',
            name='periodicity',
            field=models.IntegerField(blank=True, choices=[(1, 'каждый день'), (2, 'через день'), (3, 'каждый третий день'), (4, 'каждый четвертый день'), (5, 'каждый пятый день'), (6, 'каждый шестой день'), (7, 'каждую неделю')], default=1, null=True, verbose_name='периодичность'),
        ),
    ]