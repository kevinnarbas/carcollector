from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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
  navcars = Car.objects.all()
  car = Car.objects.get(id=car_id)
  return render(request, 'main/cars/detail.html', {'car': car, 'navcars': navcars})

class CarCreate(CreateView):
  model = Car
  template_name = 'main/create.html'
  fields = '__all__'

class CarUpdate(UpdateView):
  model = Car
  template_name = 'main/create.html'
  fields = ['description']

class CarDelete(DeleteView):
  model = Car
  template_name = 'main/delete.html'
  success_url = '/cars/'







