from django.contrib import admin
from .models import *

model_list = [Namirnica, Napomena, Osoba, Obrok, Datum]
admin.site.register(model_list)
