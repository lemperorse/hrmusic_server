from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserProfile(AbstractUser):
    bitrhday = models.DateField(blank=True,null=True)
    weight = models.FloatField(default=0)
    height = models.FloatField(default=0)
    social_register = models.BooleanField(default=False)
    my_place_race = models.FloatField(default=0)
    my_place_zone1 = models.FloatField(default=0)
    my_place_zone2 = models.FloatField(default=0)
    my_place_zone3 = models.FloatField(default=0)
    my_place_zone4 = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
