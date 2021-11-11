from django.contrib import admin

from UserPosts.models import AddGame, UserPosts, VideoUpload

admin.site.register(UserPosts)
admin.site.register(VideoUpload)
admin.site.register(AddGame)

