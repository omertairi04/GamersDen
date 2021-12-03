# Generated by Django 3.2.5 on 2021-11-27 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserPosts', '0013_post_post_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='Minecraft', max_length=255),
        ),
    ]
