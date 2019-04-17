from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListUsers.as_view(), name='users'),
    path('generate/', views.GenerateRandomUserView.as_view(), name='generate'),
]