from django.urls import path
from post.views import index,post_detail, post_create

app_name = "post"

urlpatterns = [
    path('', index, name = 'index'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('post/', post_create, name='post_create'),
]