# Generated by Django 4.0.1 on 2022-01-06 12:24

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
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, default=None, max_length=500, null=True)),
                ('game_image', models.ImageField(default='root/playpage/images/def_img.jpg', upload_to='games/images')),
                ('category', models.CharField(choices=[('Shooter', 'Shooter'), ('RPG', 'RPG'), ('Online', 'Online'), ('Offline', 'Offline')], default='Shooter', max_length=255)),
                ('steam_page', models.CharField(blank=True, max_length=255, null=True)),
                ('date_added', models.DateField(auto_now_add=True)),
                ('likes', models.ManyToManyField(related_name='game_posts', to=settings.AUTH_USER_MODEL)),
                ('published_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='published_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('header_image', models.ImageField(default='UserPosts/static/user_posts/images/game.png', upload_to='user/images')),
                ('game', models.CharField(default='Minecraft', max_length=255)),
                ('body', models.TextField(blank=True, null=True)),
                ('post_date', models.DateField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(related_name='explore_posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GameComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(default=None, max_length=255)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gamecomments', to='UserPosts.game')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gamecomments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(max_length=255)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='UserPosts.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
