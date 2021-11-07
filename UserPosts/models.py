from django.db import models

# Create your models here.
class UserPosts(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default="UserPosts/static/user_posts/images/noimg.png")
    # posted_by

    def __str__(self):
        return self.title
