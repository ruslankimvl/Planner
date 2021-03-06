# Generated by Django 3.0.8 on 2020-07-27 08:57

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
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.SlugField(max_length=150, unique=True)),
                ('body', models.TextField()),
                ('published', models.TimeField(auto_now=True)),
                ('created', models.TimeField(auto_now=True)),
                ('updated', models.TimeField(auto_now=True)),
                ('status', models.CharField(choices=[('choice', 'choice'), ('draft', 'draft'), ('published', 'published')], max_length=20)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
