from django.urls import path
from django.http import HttpResponse



def view_inicio(request):
    return HttpResponse("Bienvenidos")


urlpatterns = [
    path('home/', view_inicio),
]
