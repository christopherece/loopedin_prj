from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('profile/<str:username>/', views.user_profile, name='user-profile'),
]
