# Generated by Django 3.2.12 on 2022-04-06 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('managers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasklist',
            name='tasks',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.DeleteModel(
            name='TaskList',
        ),
    ]
