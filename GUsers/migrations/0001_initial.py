# Generated by Django 4.1.1 on 2022-09-10 11:02

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
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, default=None, null=True)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='user/profile_pics')),
                ('Website', models.CharField(blank=True, max_length=255, null=True)),
                ('Facebook', models.CharField(blank=True, max_length=255, null=True)),
                ('Twitter', models.CharField(blank=True, max_length=255, null=True)),
                ('Instagram', models.CharField(blank=True, max_length=255, null=True)),
                ('Steam', models.CharField(blank=True, max_length=255, null=True)),
                ('following', models.ManyToManyField(blank=True, related_name='followers', to='GUsers.profile')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
