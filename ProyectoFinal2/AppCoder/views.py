from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context



# Create your views here.

def view_inicio(request):
    #return HttpResponse("Bienvenidos")
    return render(request, "AppCoder/padre.html")

def view_cuentas(request):
    return HttpResponse("Aqui va a estar el perfil de la cuenta")
    
def view_task(xx):
    
     nombre = 'Matias Alejadro'
     apellido = 'Pilotta'
     diccionario = {
         'nombre': nombre,
         'apellido': apellido,
         'nacionalidad': 'argentino'
     }  # Para enviar al contexto

     #ruta = "C:/Users/pkcle/OneDrive/Escritorio/Proyecto-final-coder-house/ProyectoFinal2/AppCoder/Templates/AppCoder/index.html"
     ruta = "C:/Users/pkcle/OneDrive/Escritorio/Proyecto-final-coder-house/ProyectoFinal2/AppCoder/Templates/AppCoder/padre.html"
     mi_archivo = open(ruta, "r")

     "Método django - versión 1"
     plantilla = Template(mi_archivo.read())  # Se carga en memoria nuestro documento, template1
     contexto = Context(diccionario)  # Le doy al contexto mi nombre y apellido
     documento = plantilla.render(contexto)  # Aqui renderizamos la plantilla en documento

     return HttpResponse(documento)





