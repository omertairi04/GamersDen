# Generated by Django 3.2.10 on 2021-12-30 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GUsers', '0002_followercount'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FollowerCount',
        ),
    ]