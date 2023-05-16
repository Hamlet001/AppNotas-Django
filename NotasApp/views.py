from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from .forms import createForm
from .models import Nota

# Create your views here.

def index(request):
    Notas = Nota.objects.all()

    return render (request, "NotasApp/index.html", {'Notas': Notas})

def create(request):
    if request.method == 'GET':
        return render (request, "NotasApp/create.html", {
        'form': createForm
    })
    else:
        try:
            form = createForm(request.POST)
            newNote = form.save()
            print(newNote)
            return redirect('index')
        except ValueError:
            return render(request, 'index', {
                'form': createForm,
                'error': 'Error al crear la nota'
            })
        
def details(request, id_nota):
    if request.method == 'GET':
        NotaD = get_object_or_404(Nota, id=id_nota)
        formLleno = createForm(instance=NotaD) 
        return render(request, "NotasApp/notaDetails.html", 
                      {'Nota': NotaD, 'formLleno': formLleno})
    else:
        try:
            NotaD = get_object_or_404(Nota, id=id_nota)
            formLleno = createForm(request.POST, instance=NotaD)
            formLleno.save()
            return render(request, "NotasApp/notaDetails.html", 
                      {'Nota': NotaD, 'formLleno': formLleno})
        except ValueError:
            return render(request, 'NotasApp/notaDetails.html', {
                'formLleno': formLleno,
                'error': 'Error al editar la nota'
            })

def deleteNota(request, id_nota):
    NotaD = get_object_or_404(Nota, id=id_nota)
    NotaD.delete()
    return redirect('index')