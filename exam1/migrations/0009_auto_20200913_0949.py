# Generated by Django 3.0.6 on 2020-09-13 04:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam1', '0008_auto_20200912_0905'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.AlterField(
            model_name='imagepost',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 13, 9, 49, 2, 885172)),
        ),
        migrations.AlterField(
            model_name='videopost',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 13, 9, 49, 2, 888172)),
        ),
    ]