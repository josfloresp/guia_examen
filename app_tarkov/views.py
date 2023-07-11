from django.shortcuts import render

def vista_index(request):
    return render(request, 'index.html')

def vista_Mapas(request):
    return render(request, 'Mapas.html')

def vista_login(request):
    return render(request, 'login.html')

def vista_Ammo(request):
    return render(request, 'Ammo.html')

def vista_api(request):
    return render(request, 'api.html')

def vista_Armor(request):
    return render(request, 'Armor.html')

def vista_formulario(request):
    return render(request, 'formulario.html')

def vista_Bosses(request):
    return render(request, 'Bosses.html')


from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Registro
from .forms import RegistroForm


class RegistroListView(ListView):
    model = Registro
    template_name = 'registro_list.html'
    context_object_name = 'registros'

class RegistroCreateView(CreateView):
    model = Registro
    form_class = RegistroForm
    template_name = 'registro_create.html'
    success_url = reverse_lazy('registro_list')

class RegistroUpdateView(UpdateView):
    model = Registro
    form_class = RegistroForm
    template_name = 'registro_edit.html'
    success_url = reverse_lazy('registro_list')


class RegistroDeleteView(DeleteView):
    model = Registro
    template_name = 'registro_delete.html'
    success_url = reverse_lazy('registro_list')


