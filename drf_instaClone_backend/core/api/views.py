from rest_framework import generics, mixins, status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from core.api.serializers import ProfileSerializer,ProfileImageSerializer, UserFollowingSerializer, PostSerializer, PostImageSerializer, LikeSerializer, CommentSerializer
from core.models import Profile, UserFollowing, PostModel, LikeModel, CommentModel
from core.api.permissions import IsAdminUserOrReadOnly, IsProfileOwnerOrAdminOrReadOnly
from rest_framework.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
 

class ProfileListAPIView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class ProfileDetailedRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsProfileOwnerOrAdminOrReadOnly]


class ProfilePictureListAPIView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileImageSerializer
    permission_classes = [IsAuthenticated]


class ProfilePictureRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileImageSerializer


class PostListAPIView(generics.ListCreateAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer


class PostDetailedRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer


class PostPictureListAPIView(generics.ListAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostImageSerializer


class PostPictureRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostImageSerializer


class CommentListAPIView(generics.ListAPIView):
    queryset = CommentModel.objects.all()
    serializer_class = CommentSerializer


class CommentRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CommentModel.objects.all()
    serializer_class = CommentSerializer     


class CommentCreateAPIView(generics.CreateAPIView):
    queryset = CommentModel.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        post_pk = self.kwargs.get('pk')
        comment_owner = self.request.user
        post = generics.get_object_or_404(PostModel, pk=post_pk)
        serializer.save(comment_owner=comment_owner,commented_post=post)


class LikeListAPIView(generics.ListAPIView):
    queryset = LikeModel.objects.all()
    serializer_class = LikeSerializer

class LikeCreateAPIView(generics.CreateAPIView):
    queryset = LikeModel.objects.all()
    serializer_class = LikeSerializer

    def perform_create(self,serializer):
        post_pk = self.kwargs.get('pk')
        like_owner = self.request.user
        liked_post = generics.get_object_or_404(PostModel, pk=post_pk)
        serializer.save(like_owner=like_owner, liked_post=liked_post)

class LikeRDAPIView(generics.RetrieveDestroyAPIView):
    queryset = LikeModel.objects.all()
    serializer_class = LikeSerializer


class FollowListAPIView(generics.ListAPIView):
    queryset = UserFollowing.objects.all()
    serializer_class = UserFollowingSerializer


class FollowCreateAPIView(generics.CreateAPIView):
    queryset = UserFollowing.objects.all()
    serializer_class = UserFollowingSerializer

    def perform_create(self, serializer):
        user_id = self.request.user
        serializer.save(user_id=user_id)









