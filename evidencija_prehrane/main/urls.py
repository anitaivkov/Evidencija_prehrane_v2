from django.urls import path
from main.views import NamirnicaLista

app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
    path('namirnice/', NamirnicaLista.as_view()),
]