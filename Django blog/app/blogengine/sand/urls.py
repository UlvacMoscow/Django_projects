from django.urls import path
from .views import *
from django.views.generic import RedirectView



urlpatterns = [
    path('', GhostListView.as_view(), name='ghosts_list_url'),
    path('vampires/create/', vampire_create_view, name='create_vampire'),
    path('vampires/', VampireListView.as_view(), name='vampire_list_url'),
    path('zombies/', ZombieListView.as_view(), name='zombie_list_url'),
    path('elements/', show_elem, name='show_elem_url'),
    path('/sand/vampires/create/test_redirect/',test_redirect),

]
