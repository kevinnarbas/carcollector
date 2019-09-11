from django.forms import ModelForm
from .models import Oilchange

class OilchangeForm(ModelForm):
  class Meta:
    model = Oilchange
    fields = ['date','mileage','oil_brand','filter_brand','air_filter']
