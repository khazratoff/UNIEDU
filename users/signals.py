from doctest import FAIL_FAST
import email
from re import T, U
from urllib import request
from .models import Profile
from django.contrib.auth.models import User
from django.db.models.signals import post_save,post_delete

def createProfile(sender,instance,created,**kwargs):
    if created:
        user=instance
        profile=Profile.objects.create(
        user=user,
        username=user.username,
        email=user.email,
        name=user.first_name,)

def updateUser(sender,instance,created,**kwargs):
    profile= instance
    user = profile.user
    if created==False:
        user.first_name=profile.name
        user.username=profile.username
        user.save()

def deleteUser(sender,instance,**kwargs):
  try:
    user=instance.user
    user.delete()
  except:
    pass

post_save.connect(createProfile,sender=User)  
post_save.connect(updateUser,sender=Profile)
post_delete.connect(deleteUser,sender=Profile)  