from django.contrib import admin
from django.urls import path

from .views import UserAuthView, TodoView

urlpatterns = [
    path('todo/<int:id>/', TodoView.check_view),
    path('todo/', TodoView.as_view()),
    path('auth/register', UserAuthView.register),
    path('auth/login', UserAuthView.login),
    path('auth/logout', UserAuthView.logout),
    path('auth/info', UserAuthView.user_info),
    
]
