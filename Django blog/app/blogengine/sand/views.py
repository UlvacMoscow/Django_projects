from django.shortcuts import render
from .models import Ghost, Vampire, Zombie, GroupVampire
from django.views.generic import ListView, TemplateView
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, JsonResponse, response
import json

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
    print(request.body)
    temp_data = request.body.decode('utf-8')
    data = json.loads(temp_data)
    print(data)
    data = {
        'name': data['name'],
        'damage': data['damage'],
        'health': data['health'],
        'groups': [data['groups']],
    }
    groups = GroupVampire.objects.last()
    if request.method == 'POST':
        print('call request')
        print(dir(request.body))
        form = VampireCreateForm(data)

        if form.is_valid():
            print('form is valid');
            # obj = Vampire.objects.create(
            #     name = form.cleaned_data.get('name'),
            #     damage = form.cleaned_data.get('damage'),
            #     health = form.cleaned_data.get('health'),
            #     # groups = groups
            # )
            print(dir(form))
            vam = form.save()
            print('vampire created')
            return redirect(vam)
        print(form.errors)
        # return HttpResponseRedirect("sand/vampires")
    # template_name = 'sand/create_vampire.html'
    context = {}
    return JsonResponse({'text':'ok'})



def test_redirect(request):
    return render(request, 'sand/test_redirect.html')
