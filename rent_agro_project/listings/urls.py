from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),  # Список объявлений
    path('create/', views.create_listing, name='create_post'),  # Создание объявления
    path('<int:pk>/', views.listing_detail, name='detail'),  # Детальная страница объявления
]
