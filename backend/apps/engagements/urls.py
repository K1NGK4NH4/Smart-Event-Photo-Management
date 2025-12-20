from django.urls import path
from . import api
urlpatterns = [
   path('add_like/',api.add_like),
   path('remove_like/',api.remove_like),
   path('add_favourite/',api.add_favourite),
   path('remove_favourite/',api.remove_favourite),
   path('favourites/',api.list_favourites),
   path('tagged/',api.list_tagged_in),
]
