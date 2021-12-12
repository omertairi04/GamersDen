# Generated by Django 3.2.5 on 2021-12-12 10:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('UserPosts', '0008_auto_20211212_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='game_image',
            field=models.ImageField(default='root/playpage/images/def_img.jpg', upload_to='games/images'),
        ),
        migrations.AlterField(
            model_name='game',
            name='likes',
            field=models.ManyToManyField(related_name='liked_games', to=settings.AUTH_USER_MODEL),
        ),
    ]
