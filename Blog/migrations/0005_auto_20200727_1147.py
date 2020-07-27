# Generated by Django 3.0.8 on 2020-07-27 11:47

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0004_auto_20200727_1050'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='date',
            field=models.DateField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='meeting',
            name='duration',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Blog.Room'),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='start_time',
            field=models.TimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='title',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='room',
            name='floor',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_number',
            field=models.IntegerField(),
        ),
    ]