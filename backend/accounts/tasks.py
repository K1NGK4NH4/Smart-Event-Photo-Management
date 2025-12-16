from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
import random
from django.core.cache import cache

@shared_task(
    bind=True,
    autoretry_for=(Exception,),
    retry_kwargs={'max_retries': 3, 'countdown': 5},
)
def send_otp_email(self, email, otp):
    send_mail(
        subject="Your OTP for Smart Event Photo Management",
        message=f"Your OTP is {otp}",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email],
        fail_silently=False,
    )

