# Generated by Django 3.0.6 on 2020-08-19 14:38

import datetime
import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam_news', '0005_auto_20200819_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stud',
            name='stdname',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name=django.contrib.auth.models.User),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 19, 20, 8, 44, 706439)),
        ),
        migrations.AlterField(
            model_name='teacher_quiz_text',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 19, 20, 8, 44, 710439)),
        ),
    ]