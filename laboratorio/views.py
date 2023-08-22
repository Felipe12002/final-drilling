from django.shortcuts import render
from .forms import LaboratorioForm
from .models import Laboratorio

# Create your views here.
def v_list(request):
    context = {}
    return render(request, 'list.html', context)

def v_create(request):
    context = {
        'formulario': LaboratorioForm()
    }
    return render(request, 'create.html', context)

def v_update(request, laboratorio_id):
    lab = Laboratorio.objects.get(id = laboratorio_id)

    if request.method == 'POST':
        pass # Aqui invluir mas codigo
    else:
        context = {
            'formedicion': LaboratorioForm(instance = lab)
        }
        return render(request, 'update.html', context)

def v_delete(request, laboratorio_id):
    context = {}
    return render(request, 'delete.html', context)
