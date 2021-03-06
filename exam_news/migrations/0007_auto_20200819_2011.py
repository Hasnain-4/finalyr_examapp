# Generated by Django 3.0.6 on 2020-08-19 14:41

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exam_news', '0006_auto_20200819_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stud',
            name='stdname',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 19, 20, 11, 37, 500785)),
        ),
        migrations.AlterField(
            model_name='teacher_quiz_text',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 19, 20, 11, 37, 507785)),
        ),
    ]
