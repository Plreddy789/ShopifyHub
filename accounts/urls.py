from django.urls import path
from .views import UserProfileDetailView, register_user

urlpatterns = [
    path('profile/', UserProfileDetailView.as_view(), name='profile-detail'),
    path('register/', register_user, name='register_user'),


]
