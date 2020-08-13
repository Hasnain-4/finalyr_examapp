# Generated by Django 3.0.6 on 2020-08-13 02:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentSubmit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeslot', models.CharField(max_length=150)),
                ('subject', models.CharField(max_length=150)),
                ('bestwish', models.CharField(blank=True, default=None, max_length=350, null=True)),
                ('warningmessage', models.CharField(blank=True, default=None, max_length=550, null=True)),
                ('date', models.DateTimeField(default=datetime.datetime(2020, 8, 13, 8, 21, 41, 501661))),
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
    ]
