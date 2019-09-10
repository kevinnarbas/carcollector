from django.shortcuts import render
from .models import Car

# Create your views here.

def homepage(request):
  return render(request, 'main/homepage.html')

def about(request):
  return render(request, 'main/about.html')

def cars_index(request):
  cars = Car.objects.all()
  return render(request, 'main/cars/index.html', {'cars': cars})

def cars_detail(request, car_id):
  car = Car.objects.get(id=car_id)
  return render(request, 'main/cars/detail.html', {'car': car})





