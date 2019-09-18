from django.contrib import admin
from .models import Car, Oilchange, Driver, Photo

# Register your models here.

admin.site.register(Car)
admin.site.register(Oilchange)
admin.site.register(Driver)
admin.site.register(Photo)