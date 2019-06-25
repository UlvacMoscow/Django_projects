from django.shortcuts import render
from .models import Ghost, Vampire, Zombie
from django.views.generic import ListView, TemplateView
from django.shortcuts import render

# Create your views here.

class GhostListView(ListView):
    model = Ghost
    template = 'ghost_list.html'
    queryset = Ghost.objects.all()


class ZombieListView(ListView):
    model = Zombie
    template = 'zombie_list.html'
    queryset = Zombie.objects.all()


class VampireListView(ListView):
    model = Vampire
    template = 'vampire_list.html'
    queryset = Vampire.objects.all()


def show_elem(request):
    context = { 'my_elem' :Ghost.my_elements()}
    return render(request, 'ghost_list.html', context)
