from django.shortcuts import render
from .models import Ghost
from django.views import generic
from django.shortcuts import render 

# Create your views here.

class GhostListView(generic.ListView):
    model = Ghost
    template = 'ghost_list.html'


def show_elem(request):
    context = { 'my_elem' :Ghost.my_elements}
    return render(request, 'ghost_list.html', context)