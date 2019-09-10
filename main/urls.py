from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
  path('', views.homepage, name='homepage'),
  path('about/', views.about, name='about'),
  path('cars/', views.cars_index, name='index'),
  path('cars/<int:car_id>/', views.cars_detail, name='detail'),
]