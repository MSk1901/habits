# Generated by Django 5.0.4 on 2024-05-03 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='chat_id',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='ID чата в Telegram'),
        ),
    ]
