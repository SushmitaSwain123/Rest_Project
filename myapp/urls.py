from django.urls import path
from .views import LoginView, UserProfileView

urlpatterns = [
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/profile/', UserProfileView.as_view(), name='profile'),
]