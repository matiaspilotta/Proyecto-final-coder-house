from django.urls import path
from AppCoder.views import view_cuentas, view_inicio, view_task




urlpatterns = [
    path('home/', view_inicio),
    path('cuentas/', view_cuentas),
    path('task/', view_task),
]
