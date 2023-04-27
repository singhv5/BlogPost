from django.urls import path
from myblogapp.register import register
from myblogapp.userlogin import userlogin
from myblogapp.userlogout import userlogout
from myblogapp.home import home
from myblogapp.postCreateView import postCreateView
from myblogapp.postListView import postListView
from myblogapp.postUpdateView import postUpdateView
from myblogapp.postDeleteView import postDeleteView
from myblogapp.postSearchView import postSearchView
from myblogapp.profileView import profile_view
from myblogapp.postDetails import post_detail
from myblogapp.commentView import add_comment_to_post
from myblogapp.ratingView import add_rating
from django.urls import include


urlpatterns = [
    path('register/', register, name='register'),
    path('', userlogin, name='login'),
    path('', userlogout, name='logout'),
    path('home/', home, name='home'),
    path('createPost/', postCreateView.as_view(), name='postCreateView'),
    path('getAllPosts/', postListView.as_view(), name='postListView'),
    path('<int:pk>/updatePost/', postUpdateView.as_view(), name='postUpdateView'),
    path('<int:pk>/deletePost/', postDeleteView.as_view(), name='postDeleteView'),
    path('searchPost/', postSearchView.as_view(), name='postSearchView'),
    path('<int:pk>/searchedPosts/', postListView.as_view(), name='viewSearchedPost'),
    path('getAllCommentedPosts/<int:pk>/', postListView.as_view(), name='postcommentedListView'),
    path('getAllRatedPosts/<int:pk>/', postListView.as_view(), name='postRatedListView'),
    path('viewProfile/<str:username>/', profile_view, name='profile_view'),
    path('<int:pk>/share/', post_detail, name='post_detail'), 
    path('rating/<int:pk>/', add_rating, name='add_rating'),
    path('comment/<int:pk>/', add_comment_to_post, name='add_comment_to_post'),   
]
