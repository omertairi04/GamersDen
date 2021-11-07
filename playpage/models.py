from django.db import models

# Create your models here.
class play(models.Model):
    title = models.CharField(max_length=99)
    slug = models.SlugField()
    description = models.TextField(max_length=800)
    date_added = models.DateTimeField(auto_now_add=True)
    #image = models.ImageField()
    #posted_by = models.CharField
