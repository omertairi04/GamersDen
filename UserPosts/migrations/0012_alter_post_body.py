# Generated by Django 3.2.10 on 2021-12-31 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserPosts', '0011_alter_game_published_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
    ]
