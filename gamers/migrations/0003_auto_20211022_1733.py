# Generated by Django 3.2.5 on 2021-10-22 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamers', '0002_auto_20211022_1624'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gamer',
            name='description',
        ),
        migrations.RemoveField(
            model_name='gamer',
            name='pfp',
        ),
    ]
