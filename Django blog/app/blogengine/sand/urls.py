from django.urls import path
from .views import *



urlpatterns = [
    path('', GhostListView.as_view(), name='ghosts_list_url')
]
