from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('walks/', views.walks_index, name='index'),
    path('walks/<int:walk_id>/', views.walks_detail, name='detail'),
    path('walks/create/', views.WalkCreate.as_view(), name='walks_create'),
    path('walks/<int:pk>/update/', views.WalkUpdate.as_view(), name='walks_update'),
    path('walks/<int:pk>/delete/', views.WalkDelete.as_view(), name='walks_delete')
]