from django.urls import path
from .views import *



urlpatterns = [
    path('', GhostListView.as_view(), name='ghosts_list_url'),
    path('vampires/', VampireListView.as_view(), name='vampire_list_url'),
    path('zombies/', ZombieListView.as_view(), name='zombie_list_url'),
    path('elements/', show_elem, name='show_elem_url')
]
