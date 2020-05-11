# Generated by Django 3.0.5 on 2020-05-08 18:20

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('instagram', '0002_usersarticles'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersarticles',
            name='user_id',
        ),
        migrations.AddField(
            model_name='usersarticles',
            name='ulikes',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='likes'),
        ),
    ]
