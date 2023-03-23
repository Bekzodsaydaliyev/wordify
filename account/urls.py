from django.urls import path
from .views import login_view, logout_view, Register

app_name = 'account'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', Register.as_view(), name='register'),
]