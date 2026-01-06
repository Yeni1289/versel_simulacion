from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    # CON slash
    path('ver/<int:numero>/', views.ver_practica, name='ver_practica'),

    # SIN slash (🔥 CLAVE PARA RAILWAY 🔥)
    path('ver/<int:numero>', views.ver_practica),
]
