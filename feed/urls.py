from django.urls import path

from . import views

app_name = 'feed'

urlpatterns = [
    path('', views.Posts.as_view(), name='posts'),
    path('post/', views.NewPost.as_view(), name='new_post'),
    path('signup/', views.signup, name='signup'),
]
