# Generated by Django 3.2.5 on 2021-12-06 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserPosts', '0019_profile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]