from django.db import models

# Create your models here.
class top_header(models.Model):
    image = models.ImageField()

class center_header(models.Model):
    image = models.ImageField()

class bottom_header(models.Model):
    image = models.ImageField()