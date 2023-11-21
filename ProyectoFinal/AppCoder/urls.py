from django.urls import path
from AppCoder.views import view_cuentas, view_inicio




urlpatterns = [
    path('home/', view_inicio),
    path('cuentas/', view_cuentas),
]
