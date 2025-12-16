from django.db import models
from django.utils import timezone

# Create your models here.
class Photo(models.Model):
    photo = models.ImageField()
    is_private = models.BooleanField(default=False)
    upload_time_stamp = models.DateTimeField(default=timezone.now)
    gps_latitude = models.FloatField(null=True,blank=True)
    gps_longitude = models.FloatField(null=True,blank=True)
    camera_model = models.CharField(max_length=100,null=True,blank=True)
    aperture = models.CharField(max_length=100,null=True,blank=True)
    shutter_speed = models.CharField(max_length=100,null=True,blank=True)