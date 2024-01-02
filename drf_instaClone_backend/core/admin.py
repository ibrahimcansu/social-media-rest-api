from django.contrib import admin
from .models import Profile, UserFollowing, PostModel, LikeModel,CommentModel

# Register your models here.
admin.site.register(Profile)
admin.site.register(UserFollowing)
admin.site.register(PostModel)
admin.site.register(LikeModel)
admin.site.register(CommentModel)