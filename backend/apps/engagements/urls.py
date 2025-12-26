from django.urls import path
from . import api
urlpatterns = [
   path('<uuid:photo_id>/add_like/',api.add_like),
   path('<uuid:photo_id>/remove_like/',api.remove_like),
   path('<uuid:photo_id>/add_favourite/',api.add_favourite),
   path('<uuid:photo_id>/remove_favourite/',api.remove_favourite),
   path('favourites/',api.list_favourites),
   path('tagged/',api.list_tagged_in),
]
