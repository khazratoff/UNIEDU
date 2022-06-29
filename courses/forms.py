from dataclasses import field
from django.forms import ModelForm
from django import forms
from .models import Courses, Comments

class CourseForm(ModelForm):
    class Meta:
        model=Courses

        fields=[
            'name',
            'description',
            'featured_image',
            'link',
            'tags',
        ]

        widgets={
            'tags':forms.CheckboxSelectMultiple()
        }


    def __init__(self,*args,**kwargs):
        super(CourseForm,self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})


class CommentForm(ModelForm):
    class Meta:
        model=Comments
        fields=['text']
        label={
            'text':'Add your comment here'
        }


    def __init__(self,*args,**kwargs):
        super(CommentForm,self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})
