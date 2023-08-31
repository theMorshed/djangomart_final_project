from django.urls import path
from accounts.views import register, user_login, display_profile, user_logout

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('profile/', display_profile, name='profile'),
    path('logout/', user_logout, name='logout'),
]
