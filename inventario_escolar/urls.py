from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Bienvenido al Sistema de Inventario Escolar</h1><p>Ir a <a href="/equipos/">Equipos</a> o <a href="/admin/">Admin</a></p>')

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('equipos/', include('equipos.urls')),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_equipos, name='lista_equipos'),
    path('crear/', views.crear_equipo, name='crear_equipo'),
    path('<int:id>/', views.detalle_equipo, name='detalle_equipo'),
    path('<int:id>/editar/', views.editar_equipo, name='editar_equipo'),
    path('<int:id>/eliminar/', views.eliminar_equipo, name='eliminar_equipo'),
]
