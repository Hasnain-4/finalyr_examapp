# Generated by Django 3.0.6 on 2020-09-12 01:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher_quiz_text',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 12, 6, 55, 16, 418945)),
        ),
    ]
