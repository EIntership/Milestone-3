# Generated by Django 3.2.12 on 2022-04-01 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managers', '0009_time_work_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateTimeField(null=True),
        ),
    ]