from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

import boto3
import uuid

from .models import Car, Driver, Photo
from .forms import OilchangeForm

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'kna-catcollector'

# Create your views here.

def homepage(request):
  return render(request, 'main/homepage.html')

def about(request):
  return render(request, 'main/about.html')

@login_required
def cars_index(request):
  cars = Car.objects.filter(user=request.user)
  return render(request, 'main/cars/index.html', {'cars': cars})

@login_required
def cars_detail(request, car_id):
  navcars = Car.objects.all()
  car = Car.objects.get(id=car_id)
  not_drivers = Driver.objects.exclude(id__in = car.drivers.all().values_list('id'))
  are_drivers = Driver.objects.filter(id__in = car.drivers.all().values_list('id'))
  oilchange_form = OilchangeForm()
  return render(request, 'main/cars/detail.html', {'car': car, 'navcars': navcars, 'oilchange_form':oilchange_form, 'not_drivers': not_drivers, 'are_drivers': are_drivers})

@login_required
def oilchange(request, car_id):
  form = OilchangeForm(request.POST)
  if form.is_valid():
    new_oilchange = form.save(commit=False)
    new_oilchange.car_id = car_id
    new_oilchange.save()
  return redirect('main:detail', car_id=car_id)

@login_required
def add_driver(request, car_id, driver_id):
  Car.objects.get(id=car_id).drivers.add(driver_id)
  return redirect('main:detail', car_id=car_id)

@login_required
def rem_driver(request, car_id, driver_id):
  Car.objects.get(id=car_id).drivers.remove(driver_id)
  return redirect('main:detail', car_id=car_id)

@login_required
def add_photo(request, car_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      url = f'{S3_BASE_URL}{BUCKET}/{key}'
      photo = Photo(url=url, car_id=car_id)
      photo.save()
    except:
      print('An error occurred uploading file to S3')
  return redirect('main:detail', car_id=car_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      username = form.cleaned_data.get('username')
      messages.success(request, f'New Account Created: {username}')
      login(request, user)
      messages.info(request, f'You are now logged in as {username}')
      return redirect('main:index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def logout_request(request):
  logout(request)
  messages.info(request, 'Logged out successfully!')
  return redirect('/')

def login_request(request):
  if request.method == 'POST':
    form = AuthenticationForm(request, request.POST)
    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      user = authenticate(username=username, password=password)
      if user is not None:
        login(request, user)
        messages.info(request, f'You are now logged in as {username}')
        return redirect('main:index')
      else:
        messages.error(request, 'Invalid username or password')
    else:
      messages.error(request, 'Invalid username or password')

  form = AuthenticationForm()
  return render(request, 'main/login.html', {'form': form})
      

class CarCreate(LoginRequiredMixin, CreateView):
  model = Car
  template_name = 'main/create.html'
  fields = '__all__'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class CarUpdate(LoginRequiredMixin, UpdateView):
  model = Car
  template_name = 'main/create.html'
  fields = ['color','description']

class CarDelete(DeleteView):
  model = Car
  template_name = 'main/delete.html'
  success_url = '/cars/'

class DriverList(LoginRequiredMixin, ListView):
  model = Driver


class DriverDetail(LoginRequiredMixin, DetailView):
  model = Driver

class DriverCreate(LoginRequiredMixin, CreateView):
  model = Driver
  fields = '__all__'

class DriverUpdate(LoginRequiredMixin, UpdateView):
  model = Driver
  fields = ['name', 'age']

class DriverDelete(LoginRequiredMixin, DeleteView):
  model = Driver
  success_url = '/drivers/'





