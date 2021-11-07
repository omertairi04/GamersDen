
from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    GENDER = (
        ('M','MALE'),
        ('F','FEMALE')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default="I love Gamers Den!", max_length=100)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    gender = models.CharField(choices=GENDER , default='MALE' , max_length=1)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self , **kwargs):
        super(Profile, self).save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)