from django.db import models as m
from django.contrib.auth.models import User
import uuid


class Profile(m.Model):
    user=m.OneToOneField(User,null=True,blank=True,on_delete=m.CASCADE)
    username=m.CharField(max_length=200,null=True,blank=True)
    name=m.CharField(max_length=200,null=True,blank=True)
    email=m.CharField(max_length=500,null=True,blank=True)
    short_intro=m.CharField(max_length=400,null=True,blank=True)
    bio=m.TextField(null=True,blank=True)
    profile_image=m.ImageField(null=True,blank=True,upload_to='profiles/',default='user-default.png')
    link=m.CharField(max_length=200,blank=True,null=True)
    skill=m.ManyToManyField('Skill',blank=True)
    date_created=m.DateTimeField(auto_now_add=True)
    id=m.UUIDField(default=uuid.uuid4,primary_key=True,editable=False,unique=True)
 

    def __str__(self):
        return str(self.username)
    class Meta:
        ordering=['date_created']
    @property
    def PimageURL(self):
        try:
            url=self.profile_image.url
        except:
            url=None
        return url


class Skill(m.Model):
    name=m.CharField(max_length=200,null=True,blank=True)
    description=m.TextField(null=True,blank=True)
    date_created=m.DateTimeField(auto_now_add=True)
    id=m.UUIDField(default=uuid.uuid4,primary_key=True,editable=False,unique=True)

    def __str__(self):
        return self.name


class Message(m.Model):
    sender=m.ForeignKey(Profile,null=True,on_delete=m.SET_NULL)
    recipient=m.ForeignKey(Profile,null=True,related_name='messages',on_delete=m.SET_NULL)
    name=m.CharField(max_length=200,null=True,blank=True)
    email=m.EmailField(blank=True,null=True,max_length=200)
    subject=m.CharField(max_length=200,null=True,blank=True)
    body=m.TextField()
    is_read=m.BooleanField(default=False)
    date_created=m.DateTimeField(auto_now_add=True)
    id=m.UUIDField(default=uuid.uuid4,primary_key=True,editable=False,unique=True)


    def __str__(self):
        return self.subject

    class Meta:
        ordering =['is_read','-date_created']