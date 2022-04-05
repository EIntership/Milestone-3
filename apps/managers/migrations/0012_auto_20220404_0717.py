# Generated by Django 3.2.12 on 2022-04-04 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('managers', '0011_alter_task_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='date',
        ),
        migrations.RemoveField(
            model_name='task',
            name='date_finished',
        ),
        migrations.RemoveField(
            model_name='task',
            name='time',
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(null=True)),
                ('date_finished', models.DateTimeField(null=True)),
                ('hours', models.IntegerField()),
                ('minutes', models.IntegerField()),
                ('time', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='time', to='managers.task')),
            ],
        ),
    ]