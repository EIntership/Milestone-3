# Generated by Django 3.2.12 on 2022-04-01 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managers', '0007_time_work'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_finished',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='time_work',
            name='time_finish',
            field=models.DateTimeField(null=True),
        ),
    ]