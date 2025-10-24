from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Equipo
from django.utils import timezone

def lista_equipos(request):
    equipos = Equipo.objects.all()
    return render(request, 'equipos/lista_equipos.html', {'equipos': equipos})

def detalle_equipo(request, id):
    equipo = get_object_or_404(Equipo, id=id)
    return render(request, 'equipos/detalle_equipo.html', {'equipo': equipo})

def crear_equipo(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        categoria = request.POST['categoria']
        estado = request.POST['estado']
        fecha_ingreso = request.POST['fecha_ingreso']
        ubicacion = request.POST['ubicacion']
        Equipo.objects.create(
            nombre=nombre,
            categoria=categoria,
            estado=estado,
            fecha_ingreso=fecha_ingreso,
            ubicacion=ubicacion
        )
        return redirect('lista_equipos')
    return render(request, 'equipos/crear_equipo.html')

def editar_equipo(request, id):
    equipo = get_object_or_404(Equipo, id=id)
    if request.method == 'POST':
        equipo.nombre = request.POST['nombre']
        equipo.categoria = request.POST['categoria']
        equipo.estado = request.POST['estado']
        equipo.fecha_ingreso = request.POST['fecha_ingreso']
        equipo.ubicacion = request.POST['ubicacion']
        equipo.save()
        return redirect('lista_equipos')
    return render(request, 'equipos/editar_equipo.html', {'equipo': equipo})

def eliminar_equipo(request, id):
    equipo = get_object_or_404(Equipo, id=id)
    equipo.delete()
    return redirect('lista_equipos')
