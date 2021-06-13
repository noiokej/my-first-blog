from django.urls import path
from . import views, api



urlpatterns = [
    path('', views.post_list, name='post_list'),
    # Możemy dostać się do klucza podstawowego przez wpisanie post.pk,
    # tak samo jak otrzymujemy dostęp do innych pól (title, author, itd.) w naszym obiekcie Post
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/comment/new/', views.comment_new, name='comment_new'),
    path('terminarz/', views.callendar, name='callendar'),
    path('weather/', api.weather, name='weather'),
    #path('post/<int:pk>/', views.comment_list, name='comment_list'),
    #path('post/comment_list/', views.comment_list, name='comment_list')

]