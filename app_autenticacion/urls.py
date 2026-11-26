from django.urls import path
from . import views

urlpatterns = [
    path('', views.autenticacion, name='autenticacion'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('cerrar-sesion/', views.cerrar_sesion, name='cerrar_sesion'),
]