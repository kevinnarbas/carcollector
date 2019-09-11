from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Car
from .forms import OilchangeForm

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
  oilchange_form = OilchangeForm()
  return render(request, 'main/cars/detail.html', {'car': car, 'navcars': navcars, 'oilchange_form':oilchange_form})

def oilchange(request, car_id):
  form = OilchangeForm(request.POST)
  if form.is_valid():
    new_oilchange = form.save(commit=False)
    new_oilchange.car_id = car_id
    new_oilchange.save()
  return redirect('main:detail', car_id=car_id)

class CarCreate(CreateView):
  model = Car
  template_name = 'main/create.html'
  fields = '__all__'

class CarUpdate(UpdateView):
  model = Car
  template_name = 'main/create.html'
  fields = ['color','description']

class CarDelete(DeleteView):
  model = Car
  template_name = 'main/delete.html'
  success_url = '/cars/'







