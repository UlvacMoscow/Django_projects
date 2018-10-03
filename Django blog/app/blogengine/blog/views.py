from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def posts_list(request):
    name = 'sen'
    return render(request, 'blog/index.html', context={'name' : name})
