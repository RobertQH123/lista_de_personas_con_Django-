from django.shortcuts import render
from .models import Persona
from .forms import PersonaForm
from django.shortcuts import render
from django.views.generic import (
  ListView,
  DetailView,
  CreateView,
  )
class PersonaCreateView(CreateView):
  model = Persona
  fields = [
    'nombres',
    'apellidos',
    'edad',
    'donador',
  ]

class PersonaListView(ListView):
  model = Persona

class PersonaDetailView(DetailView):
  model = Persona

def personaTestView(request):
  obj = Persona.objects.get(id = 1)
  context = {
      'objeto': obj,
      }
  return render(request, 'personas/descripcion.html', context)

def personaCreateView(request):
  print(request)
  if request.method == 'POST':
    nombre = request.POST.get('q')
    print(nombre)
  context = {}
  return render(request, 'personas/personasCreate.html', context)

def searchForHelp(request):
  return render(request, 'personas/search.html', {})

