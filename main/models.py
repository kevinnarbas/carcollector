from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date


# Create your models here.

YESNO = (
  ('Y', 'Yes'),
  ('N', 'No'),
)

class Driver(models.Model):
  name = models.CharField(max_length=20)
  age = models.IntegerField()

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('main:drivers_detail', kwargs={'pk': self.id})


class Car(models.Model):
  model = models.CharField(max_length=50)
  make = models.CharField(max_length=50)
  color = models.CharField(max_length=20)
  year = models.IntegerField()
  description = models.TextField() 
  drivers = models.ManyToManyField(Driver)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return f'({self.id}) {self.model}'

  def get_absolute_url(self):
    return reverse('main:detail', kwargs={'car_id': self.id})


class Oilchange(models.Model):
  date = models.DateField('Date of last oil change')
  mileage = models.IntegerField()
  oil_brand = models.CharField(max_length=25)
  filter_brand = models.CharField(max_length=25)
  air_filter = models.CharField('Air filter changed?', max_length=1, choices=YESNO, default='N')
  car = models.ForeignKey(Car, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.date}'

  class Meta:
    ordering = ['-mileage']


class Photo(models.Model):
  url = models.CharField(max_length=200)
  car = models.ForeignKey(Car, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for car_id: {self.car_id} @{self.url}"
