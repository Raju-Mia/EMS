# Generated by Django 4.1.7 on 2023-04-08 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ppemsapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='done_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='pending_status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='working_status',
            field=models.BooleanField(default=False),
        ),
    ]
