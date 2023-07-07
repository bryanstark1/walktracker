from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('walks/', views.walks_index, name='index')
]