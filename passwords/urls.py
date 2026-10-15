from django.urls import path
from . import views

urlpatterns = [
    path('', views.password_dashboard, name='password_dashboard'),
]