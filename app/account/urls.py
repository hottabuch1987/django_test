from django.urls import path
from .views import *
from django.views.generic import TemplateView

urlpatterns = [
    path('api/auth/registration/', AuthCode.as_view(), name='user_registration'),
    path('api/auth/login/', UserLogin.as_view(), name='user_login'),
    path('api/auth/profile/<str:email>/', UserProfile.as_view(), name='user_profile'),


]
