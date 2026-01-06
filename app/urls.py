from django.urls import path
from .views import dashboard, ver_practica

urlpatterns = [
    path("", dashboard, name="dashboard"),   # 👈 RUTA RAÍZ
    path("ver/<int:numero>/", ver_practica, name="ver_practica"),
]
