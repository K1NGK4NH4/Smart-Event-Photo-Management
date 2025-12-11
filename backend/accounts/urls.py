from django.urls import path,include
from .import views
from . import userlogin

urlpatterns = [
    path('', views.home_view),
    path('public/send-otp/', userlogin.otp_send),
    path('public/verify-otp/', userlogin.otp_verify),
]