# Generated by Django 3.0.6 on 2020-09-12 03:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam1', '0007_auto_20200912_0903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagepost',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 12, 9, 5, 2, 848930)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='about',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='videopost',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 12, 9, 5, 2, 852930)),
        ),
    ]
