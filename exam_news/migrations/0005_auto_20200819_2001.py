# Generated by Django 3.0.6 on 2020-08-19 14:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam_news', '0004_auto_20200819_1953'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stud',
            name='user',
        ),
        migrations.AlterField(
            model_name='teacher',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 19, 20, 1, 56, 510241)),
        ),
        migrations.AlterField(
            model_name='teacher_quiz_text',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 19, 20, 1, 56, 510241)),
        ),
    ]