# Generated by Django 3.0.6 on 2020-09-12 01:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam_news', '0010_auto_20200912_0655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 12, 6, 55, 43, 867515)),
        ),
    ]
