# Generated by Django 3.0.6 on 2020-08-19 14:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagepost',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 19, 19, 46, 34, 833343)),
        ),
        migrations.AlterField(
            model_name='videopost',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 19, 19, 46, 34, 836343)),
        ),
    ]