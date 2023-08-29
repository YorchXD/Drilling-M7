from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from .models import Laboratorio
from .forms import LaboratorioForm

def laboratorio_list(request):
    laboratorios = Laboratorio.objects.all()
    return render(request, 'lista_laboratorio.html', {'laboratorios': laboratorios})

def editar_laboratorio(request, laboratorio_id):
    laboratorio = Laboratorio.objects.get(pk=laboratorio_id)
    if request.method == 'POST':
        form = LaboratorioForm(request.POST, instance=laboratorio)
        if form.is_valid():
            form.save()
            return redirect('laboratorios')
    else:
        form = LaboratorioForm(instance=laboratorio)
    return render(request, 'editar_laboratorio.html', {'form': form, 'laboratorio': laboratorio})

def confirmar_eliminar_laboratorio(request, laboratorio_id):
    laboratorio = Laboratorio.objects.get(pk=laboratorio_id)
    return render(request, 'confirmar_eliminar_laboratorio.html', {'laboratorio': laboratorio})

def eliminar_laboratorio(request, laboratorio_id):
    laboratorio = Laboratorio.objects.get(pk=laboratorio_id)
    if request.method == 'POST':
        laboratorio.delete()
        return redirect('laboratorios')
    return redirect('confirmar_eliminar_laboratorio', laboratorio_id=laboratorio_id)

def crear_laboratorio(request):
    if request.method == 'POST':
        form = LaboratorioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('laboratorios')
    else:
        form = LaboratorioForm()
    return render(request, 'crear_laboratorio.html', {'form': form})
