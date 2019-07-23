from django.urls import path
from accounts.views import register,login,profileUser, logout_view

app_name = 'accounts'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('profile/', profileUser, name='profile'),
    path('logout/', logout_view, name="logout")
]
