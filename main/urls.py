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
  path('cars/<int:car_id>/oilchange', views.oilchange, name='oilchange'),
  path('cars/<int:car_id>/add_driver/<int:driver_id>/', views.add_driver, name='add_driver'),
  path('cars/<int:car_id>/rem_driver/<int:driver_id>/', views.rem_driver, name='rem_driver'),
  path('cars/<int:car_id>/add_photo/', views.add_photo, name='add_photo'),
  path('drivers/', views.DriverList.as_view(), name='drivers_index'),
  path('drivers/create/', views.DriverCreate.as_view(), name='drivers_create'),
  path('drivers/<int:pk>/', views.DriverDetail.as_view(), name='drivers_detail'),
  path('drivers/<int:pk>/update/', views.DriverUpdate.as_view(), name='drivers_update'),
  path('drivers/<int:pk>/delete/', views.DriverDelete.as_view(), name='drivers_delete'),
  path('accounts/signup/', views.signup, name='signup'),
  path('logout/', views.logout_request, name='logout'),
  path('login/', views.login_request, name='login'),
]