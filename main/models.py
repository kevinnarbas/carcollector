from django.db import models
from django.urls import reverse

# Create your models here.

class Car(models.Model):
  model = models.CharField(max_length=50)
  make = models.CharField(max_length=50)
  year = models.IntegerField()
  description = models.TextField() 

  def __str__(self):
    return f'({self.id}) {self.model}'

  def get_absolute_url(self):
    return reverse('main:detail', kwargs={'car_id': self.id})
