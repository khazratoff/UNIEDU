from turtle import right
from unittest import result
from django.shortcuts import render,redirect
from django.http import HttpResponse
from users.views import profile
from .forms import CourseForm,CommentForm
from django.contrib.auth.decorators import login_required
from .models import Courses,Tags
from .utils import searchCourses,paginateCourses
from django.contrib import messages



def courses(request):

    coursesObject, text= searchCourses(request)

    custom_range,coursesObject=paginateCourses(request,coursesObject,2)

    context={'courses':coursesObject,'searchQuery':text,'custom_range':custom_range}
    return render(request,'courses/courses.html',context)


def course(request,primkey):
    courseObject=Courses.objects.get(id=primkey)
    tags=courseObject.tags.all()

    commentForm=CommentForm()

    if request.method=='POST':
        commentForm=CommentForm(request.POST)
        if commentForm.is_valid():
            comment=commentForm.save(commit=False)
            comment.course=courseObject
            comment.owner=request.user.profile
            comment.save()

            messages.success(request,'Your comment has succesfully added!')

            return redirect('course', primkey=courseObject.id)
    context={'primkey':primkey,'course':courseObject,'tags':tags,'form':commentForm}
    return render(request,'courses/course.html',context)

@login_required(login_url='login')
def courseCreate(request):
    form=CourseForm()
    profile=request.user.profile
    if request.method=='POST':
        form=CourseForm(request.POST,request.FILES)
        if form.is_valid():
            course=form.save(commit=False)
            course.owner=profile
            course.save()
            return redirect('courses')
    context={'form':form}
    return render(request,'courses/course-form.html',context)


@login_required(login_url='login')
def courseUpdate(request,primkey):
    profile=request.user.profile
    CourseObj=Courses.objects.get(id=primkey)
    if CourseObj.owner.id==profile.id:
        form=CourseForm(instance=CourseObj)
        if request.method=='POST':
            form=CourseForm(request.POST,request.FILES,instance=CourseObj)
            if form.is_valid():
                form.save()
                return redirect('account')
        context={'form':form}
        return render(request,'courses/course-form.html',context)

    else:
        return HttpResponse('Something went wrong...')
@login_required(login_url='login')
def courseDelete(request,primkey):
    profile=request.user.profile
    course=Courses.objects.get(id=primkey)
    if course.owner.id==profile.id:
        if request.method=='POST':
            course.delete()
            return redirect('courses')
        context={'course':course}
        return render(request,'courses/del-confirm.html',context)

    else:
        return HttpResponse('Something went wrong...')
