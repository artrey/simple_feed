from django.urls import path

from . import views

app_name = 'apps.feed'

urlpatterns = [
    path('', views.Posts.as_view(), name='posts'),
    path('<str:post_id>/', views.Posts.as_view(), name='posts'),
]
