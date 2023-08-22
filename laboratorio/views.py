from django.shortcuts import render

# Create your views here.
def v_list(request):
    context = {}
    return render(request, 'list.html', context)
use "git push" to publish your local commits
def v_create(request):
    context = {}
    return render(request, 'create.html', context)

def v_update(request, laboratorio_id):
    context = {}
    return render(request, 'update.html', context)

def v_delete(request, laboratorio_id):
    context = {}
    return render(request, 'delete.html', context)