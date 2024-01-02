from core.models import Profile, UserFollowing, PostModel, LikeModel, CommentModel
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    profile_image = serializers.ImageField(read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'

    
class ProfileImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['id','profile_image']


class LikeSerializer(serializers.ModelSerializer):
    like_owner = serializers.StringRelatedField(read_only=True)
    liked_post = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = LikeModel
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    comment_owner = serializers.StringRelatedField(read_only=True)
    commented_post = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = CommentModel
        fields = '__all__'
        


class PostSerializer(serializers.ModelSerializer):
    post_owner = serializers.StringRelatedField(read_only=True)
    #like = serializers.StringRelatedField(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = PostModel
        fields = '__all__'
    

class PostImageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PostModel
        fields = ['id', 'post_image']




class UserFollowingSerializer(serializers.ModelSerializer):
    user_id = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = UserFollowing
        fields = '__all__'
