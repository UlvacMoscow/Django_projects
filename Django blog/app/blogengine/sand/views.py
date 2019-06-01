from django.shortcuts import render
from .models import Ghost
from django.views import generic

# Create your views here.

class GhostListView(generic.ListView):
    model = Ghost
    template = 'Ghost_list.html'
