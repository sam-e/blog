from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class UserProfile(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   description = models.CharField(max_length=100, default='')
   city = models.CharField(max_length=30, default='')
   website = models.URLField(default='')
   phone = models.IntegerField(default='0')

   def __unicode__(self):
      return u"%s" % self.user
