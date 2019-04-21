from django.urls import path

from . import views

urlpatterns = [
    path('0/', views.fetch_data_view, name='fetch-data'),
    path('1/', views.fetch_data_no_celery_view, name='fetch-data-no-celery'),
]