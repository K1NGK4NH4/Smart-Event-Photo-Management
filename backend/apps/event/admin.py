from django.contrib import admin
from rest_framework import permissions,generics,authentication
from .models import Event
from .serializers import EventSerializer
from accounts.permissions import IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework.views  import APIView

# Register your models here.
admin.site.register(Event)

#create a new event and assign event co-ordinator
