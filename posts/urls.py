from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:post_id>/', views.delete, name='delete'),
    path('update/<int:pk>/', views.update_tweet, name='update_tweet'),
    path('postLikeAdd/<int:post_id>', views.postLikeAdd, name='likeAdd'),
]
