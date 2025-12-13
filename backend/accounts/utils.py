from django.core.mail import send_mail
from django.core.cache import cache
from django.conf import settings
import random,string,secrets
from django.utils.crypto import get_random_string

def generate_unique_username(base_username):
        username = base_username
        from .models import User
        while User.objects.filter(username=username).exists():
            username = f"{base_username}_{get_random_string(4).lower()}"
        return username

def send_otp(email):
    subject = "Your OTP for Login in Smart Event Photo Management"
    email_sender = settings.EMAIL_HOST_USER
    otp = random.randint(100000,999999)
    if cache.get(email) is not None:
        otp = cache.get(email)
    else:
        cache.set(email,otp,60)
    message = f"Your OTP is {otp}"
    send_mail(subject,message,email_sender,[email])


def passwordgenerator():
    allowed_special = "!@#$%&*^|?"
    chars = string.ascii_letters+string.digits+allowed_special
    return ''.join(secrets.choice(chars) for _ in range(8))

def verify_otp(email,otp):
    if cache.get(email) == int(otp):
        cache.delete(email)
        return True
    return False

def send_password(email,password=None):
    if password is None:
        password = passwordgenerator()
    subject="Your Password for Login into Smart-Event-Photo-Management App"
    message=f"Your Password is {password}.If you want You can Change it later after joining."
    from_email=settings.EMAIL_HOST_USER
    send_mail(subject,message,from_email,[email])
                
