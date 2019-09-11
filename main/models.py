from django.db import models
from django.urls import reverse

# Create your models here.

YESNO = (
  ('y', 'Yes'),
  ('n', 'No'),
)


class Car(models.Model):
  model = models.CharField(max_length=50)
  make = models.CharField(max_length=50)
  year = models.IntegerField()
  description = models.TextField() 

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
