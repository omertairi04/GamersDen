# Generated by Django 3.2.5 on 2021-10-22 15:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gamers', '0003_auto_20211022_1733'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamer',
            name='user',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='gamer',
            name='user_pfp',
            field=models.ImageField(default='gamers\\static\\gamers\\images\x07vatar.jpg', upload_to='profile_pics'),
        ),
    ]
