from django.db import models
from django.contrib.auth.models import User
import uuid
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.CharField(max_length=300, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    working_at = models.CharField(max_length=100, default='#', blank=True, null=True)
    profile_image = models.ImageField(upload_to="profile_images/%Y/%m/%d/", blank=True, null=True)

    def __str__(self):
        return self.user.username
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.profile_image:
            image = Image.open(self.profile_image.path)
            if image.height > 600 or image.width > 600:
                output_size = (600, 600)
                image.thumbnail(output_size)
                image.save(self.profile_image.path)


class PostModel(models.Model):
    post_image = models.ImageField(upload_to="post_images/%Y/%m/%d/")
    post_caption = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    post_owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_owner')
    like = models.ManyToManyField(User, related_name='like', blank=True, through='LikeModel')

    def __str__(self):
        return f"{self.post_owner} uploaded new photo at {self.created_at}"
    
    class Meta:
        ordering = ('-created_at',)


class CommentModel(models.Model):
    comment_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    commented_post = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class LikeModel(models.Model):
    like_owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like_owner')
    liked_post = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name='liked_post')
    liked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (("like_owner", "liked_post"),)

    def __str__(self):
        return f"{self.like_owner} liked {self.liked_post.post_owner}'s photo at {self.liked_at}"


class UserFollowing(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_id')
    following_user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following_user_id')  
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        unique_together = (('user_id', 'following_user_id'),)
        ordering = ['created_at']

    def __str__(self):
        return f"{self.user_id} follows {self.following_user_id}"