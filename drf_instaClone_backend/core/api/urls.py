from django.urls import path, include
from core.api.views import (
    ProfileListAPIView, ProfileDetailedRUDAPIView, ProfilePictureListAPIView, ProfilePictureRUDAPIView, 
    PostListAPIView, PostDetailedRUDAPIView, PostPictureListAPIView, PostPictureRUDAPIView, 
    CommentListAPIView, CommentRUDAPIView, CommentCreateAPIView,
    LikeListAPIView, LikeCreateAPIView, LikeRDAPIView,
    FollowListAPIView, FollowCreateAPIView,
          )


urlpatterns= [

    #profile related url
    path('profile/', ProfileListAPIView.as_view(), name='porofile-list'),
    path('profile/<int:pk>/', ProfileDetailedRUDAPIView.as_view(), name='profile-detail'),

    #profile_picture 
    path('profile/picture/', ProfilePictureListAPIView.as_view(), name='profile-picture'),
    path('profile/picture/<int:pk>/', ProfilePictureRUDAPIView.as_view(), name='profile-picture'),  
    
    #post related url
    path('post/', PostListAPIView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailedRUDAPIView.as_view(), name='post-detail'),

    #post picture 
    path('post/picture/', PostPictureListAPIView.as_view(), name='post-picture'),
    path('post/picture/<int:pk>/', PostPictureRUDAPIView.as_view(), name='post-picture-detail'), 
    
    #comment
    path('comment/', CommentListAPIView.as_view(), name='comment'),        
    path('comment/<int:pk>/', CommentRUDAPIView.as_view(), name='comment-detail'),
    path('post/<int:pk>/comment/', CommentCreateAPIView.as_view(), name='comment-create'),
    
    #like related url
    path('like/', LikeListAPIView.as_view(), name='like-list'),
    path('post/<int:pk>/like/', LikeCreateAPIView.as_view(), name='like-create'),
    path('like/<int:pk>/', LikeRDAPIView.as_view(), name='like-detail'),

    #user_following related url
    path('follow/', FollowListAPIView.as_view(), name='follow-list'),
    path('profile/<int:pk>/follow', FollowCreateAPIView.as_view(), name='follow-create'),



    ]