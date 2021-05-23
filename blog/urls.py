from django.urls import path
from . import views
# spr

urlpatterns = [
    path('', views.post_list, name='post_list'),
    # Możemy dostać się do klucza podstawowego przez wpisanie post.pk,
    # tak samo jak otrzymujemy dostęp do innych pól (title, author, itd.) w naszym obiekcie Post!
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]