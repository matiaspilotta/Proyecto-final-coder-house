from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def view_inicio(request):
    #return HttpResponse("Bienvenidos")
    return render(request, "AppCoder/padre.html")

def view_cuentas(request):
    return HttpResponse("Aqui va a estar el perfil de la cuenta")
    




