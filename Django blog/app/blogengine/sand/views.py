from django.shortcuts import render
from .models import Ghost, Vampire, Zombie, GroupVampire
from django.views.generic import ListView, TemplateView
from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse

from .forms import VampireCreateForm
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

def vampire_create_view(request, *args, **kwargs):
    print('call form')
    groups = GroupVampire.objects.last()
    if request.method == 'POST':
        print('call request')
        print(request.data)
        form = VampireCreateForm()

        if form.is_valid():
            print('form is valid');
            print(form.is_valid())
            obj = Vampire.objects.create(
                name = form.cleaned_data.get('name'),
                damage = form.cleaned_data.get('damage'),
                health = form.cleaned_data.get('health'),
                groups = groups

            )
        # return HttpResponseRedirect("sand/vampires")
    # template_name = 'sand/create_vampire.html'
    context = {}
    return JsonResponse({'text':'ok'})
