from django.shortcuts import render
from django.http import Http404
from django.conf import settings
import os

ARCHIVOS = [
    {'numero': 5, 'titulo': 'Regresión Logística',
     'file': '05_Regrecion_Loguistica2.html',
     'original': '05_Regrecion_Loguistica.html'},

    {'numero': 6, 'titulo': 'Visualización del DataSet',
     'file': '06_Visualizacion_DtaSet2.html',
     'original': '06_Visualizacion_DtaSet.html'},

    {'numero': 7, 'titulo': 'División del DataSet',
     'file': '07_Divicion_del_DataSet2.html',
     'original': '07_Divicion_del_DataSet.html'},

    {'numero': 8, 'titulo': 'Preparación del DataSet',
     'file': '08_Preparacion_del_DataSet2.html',
     'original': '08_Preparacion_del_DataSet.html'},

    {'numero': 9, 'titulo': 'Transformadores y Pipeline',
     'file': '09_Creacion-de-Transformadores-y-Pipeline-Personalizados2.html',
     'original': '09_Creacion-de-Transformadores-y-Pipeline-Personalizados.html'},

    {'numero': 10, 'titulo': 'Evaluación de Resultados',
     'file': '10_Evalucion-de-Resultados2.html',
     'original': '10_Evalucion-de-Resultados.html'},
]




# Información específica para cada práctica, usada para el menú lateral
PRACTICAS_INFO = {
    5: {'mini': 'Detección de SPAM con Regresión Logística', 'btn_label': 'Ver resumen', 'btn_action': 'open_tab', 'btn_href': 'notebooks/05_Regrecion_Loguistica.html'},
    6: {'mini': 'Exploración y gráficos del conjunto', 'btn_label': 'Ver gráficos', 'btn_action': 'open_tab', 'btn_href': 'notebooks/06_Visualizacion_DtaSet.html'},
    7: {'mini': 'Dividir datos para entrenamiento y prueba', 'btn_label': 'Ver división', 'btn_action': 'open_tab', 'btn_href': 'notebooks/07_Divicion_del_DataSet.html'},
    8: {'mini': 'Preparar datos y transformaciones', 'btn_label': 'Ver preparación', 'btn_action': 'open_tab', 'btn_href': 'notebooks/08_Preparacion_del_DataSet.html'},
    9: {'mini': 'Crear transformadores y pipeline', 'btn_label': 'Ver transformadores', 'btn_action': 'open_tab', 'btn_href': 'notebooks/09_Creacion-de-Transformadores-y-Pipeline-Personalizados.html'},
    10: {'mini': 'Evaluación y métricas de desempeño', 'btn_label': 'Ver métricas', 'btn_action': 'open_tab', 'btn_href': 'notebooks/10_Evalucion-de-Resultados.html'},
}


def dashboard(request):
    """Muestra la lista de prácticas en el dashboard."""
    practicas = [{'numero': a['numero'], 'titulo': a['titulo']} for a in ARCHIVOS]
    return render(request, 'dashboard.html', {'practicas': practicas})


def ver_practica(request, numero):
    """Renderiza la práctica dentro del `visor.html` para que se muestre el menú y estilos."""
    archivo_obj = next((a for a in ARCHIVOS if a['numero'] == numero), None)
    if not archivo_obj:
        raise Http404("Práctica no encontrada")

    ruta = os.path.join(settings.BASE_DIR, 'static', 'notebooks', archivo_obj['file'])
    if not os.path.exists(ruta):
        raise Http404("Archivo de la práctica no encontrado")

    indices = [a['numero'] for a in ARCHIVOS]
    idx = indices.index(numero)
    prev_num = indices[idx - 1] if idx > 0 else None
    next_num = indices[idx + 1] if idx < len(indices) - 1 else None

    practicas = [{'numero': a['numero'], 'titulo': a['titulo']} for a in ARCHIVOS]

    # Información específica de la práctica activa (etiqueta de botón, mini descripción, etc.)
    practica_info = PRACTICAS_INFO.get(numero, {
        'mini': '',
        'btn_label': 'Abrir',
        'btn_action': 'open_tab',
        'btn_href': 'notebooks/' + archivo_obj['file']
    })

    context = {
    'archivo': f"notebooks/{archivo_obj['file']}",              # visor
    'archivo_original': f"notebooks/{archivo_obj['original']}", # botón Abrir
    'numero': numero,
    'titulo': archivo_obj['titulo'],
    'practica_info': practica_info,
    'practicas': practicas,
    'prev_num': prev_num,
    'next_num': next_num,
}


    return render(request, 'visor.html', context)
