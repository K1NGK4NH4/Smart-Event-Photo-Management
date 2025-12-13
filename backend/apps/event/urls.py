from django.urls import path
from . import admin,eventcoordinator,views

urlpatterns = [
    path('create/' , views.event_create_view),
    path('<slug:slug>/update/' , views.event_details_update),
    path('<slug:slug>/about/' , views.event_details_view),
    path('<slug:slug>/delete/' , views.event_delete_view),
    path('' , views.event_list_view),
]
