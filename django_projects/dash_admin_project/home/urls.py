from django.urls import path
from home import views

urlpatterns = [
    path('index', views.home, name='home'),
    path('', views.home, name='home'),
]