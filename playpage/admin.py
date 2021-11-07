from django.contrib import admin

from playpage.views import playpage
from . import models
# Register your models here.

admin.site.register(models.play)
