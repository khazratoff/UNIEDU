from enum import unique
from sys import flags
from django.db import models as m
import uuid
from users.models import Profile
# Create your models here.
class Courses(m.Model):
    owner=m.ForeignKey(Profile,null=True,blank=True,on_delete=m.SET_NULL)
    name=m.CharField(max_length=200)
    description=m.TextField(null=True,blank=True)
    featured_image=m.ImageField(null=True,blank=True,default='def.jpg')
    link=m.CharField(max_length=2000,null=True,blank=True)
    date_created=m.DateTimeField(auto_now_add=True)
    tags=m.ManyToManyField('Tags',blank=True)
    id=m.UUIDField(default=uuid.uuid4,primary_key=True,editable=False,unique=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering=['date_created']

    @property
    def commentors(self):
        queryset=self.comments_set.all().values_list('owner__id',flat=True)
        return queryset

class Comments(m.Model):
    owner=m.ForeignKey(Profile,on_delete=m.CASCADE,null=True)
    text=m.TextField(null=True,blank=True)
    course=m.ForeignKey(Courses,on_delete=m.CASCADE)
    date_created=m.DateField(auto_now_add=True)
    id=m.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    class Meta:
        unique_together=[['owner','course']]


    def __str__(self):
        return self.course.name
   


class Tags(m.Model):
    name=m.CharField(max_length=200)
    date_created=m.DateField(auto_now_add=True)
    id=m.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):
        return self.name
