# Generated by Django 3.0.6 on 2020-08-10 01:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam1', '0002_auto_20200810_0650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagepost',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 10, 6, 55, 17, 745232)),
        ),
        migrations.AlterField(
            model_name='videopost',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 10, 6, 55, 17, 748232)),
        ),
    ]
