from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
  path('', views.homepage, name='homepage'),
  path('about/', views.about, name='about'),
  path('cars/', views.cars_index, name='index'),
  path('cars/create/', views.CarCreate.as_view(), name='create'),
  path('cars/<int:car_id>/', views.cars_detail, name='detail'),
  path('cars/<int:pk>/update', views.CarUpdate.as_view(), name='update'),
  path('cars/<int:pk>/delete', views.CarDelete.as_view(), name='delete'),
]