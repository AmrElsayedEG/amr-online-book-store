from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView

app_name = 'authenticate'

urlpatterns = [
    # Register Endpoints
    path('register/', RegisterView.as_view(), name='register'),

    # Login and Logout and Refresh Token Endpoints
    path('login/', LoginView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh_token'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
