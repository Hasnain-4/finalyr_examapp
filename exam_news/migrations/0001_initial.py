# Generated by Django 3.0.6 on 2020-08-10 01:19

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeslot', models.CharField(max_length=150)),
                ('subject', models.CharField(max_length=150)),
                ('bestwish', models.CharField(blank=True, default=None, max_length=350, null=True)),
                ('warningmessage', models.CharField(blank=True, default=None, max_length=550, null=True)),
                ('date', models.DateTimeField(default=datetime.datetime(2020, 8, 10, 6, 49, 52, 378840))),
            ],
        ),
        migrations.CreateModel(
            name='TecherData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('writtenquestion', models.CharField(blank=True, default='', max_length=330, null=True)),
                ('imagequestion', models.ImageField(blank=True, default=None, null=True, upload_to='')),
                ('option1', models.CharField(default='A', max_length=150)),
                ('option2', models.CharField(default='B', max_length=150)),
                ('option3', models.CharField(default='C', max_length=150)),
                ('option4', models.CharField(default='D', max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='StudentData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stdname', models.CharField(blank=True, max_length=255, null=True)),
                ('answer', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
