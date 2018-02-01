from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   description = models.CharField(max_length=100, default='DEFAULT VALUE')
   city = models.CharField(max_length=30, default='DEFAULT VALUE')
   website = models.URLField(default='DEFAULT VALUE')
   phone = models.IntegerField(default='0')
