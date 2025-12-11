from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HomeView(APIView):
    def get(self,request):
        return Response({
            "message":"This is your Home Page Buddy",
        })

home_view = HomeView.as_view()