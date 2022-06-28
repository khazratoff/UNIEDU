import re
from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from .models import Profile,Message
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm, ProfileForm,MessageForm
from courses.models import Courses 
from .utils import searchProfiles,paginateProfiles
# Create your views here.
def loginUser(request):
    
    page='login'
    context={'page':page}
    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method=='POST':
        username=request.POST['username'].lower()
        password=request.POST['password']

        try:
            user=User.objects.get(username=username)
        except:
            messages.error(request,'User does not exist')

        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'profiles')
        else:
            messages.error(request,'username or passwors is incorrect')

    return render(request,'users/login_register.html',context)


def logoutUser(request):
        logout(request)
        messages.info(request,'You have succesfully logged out!')
        return redirect('login')


def registerUser(request):
    page='register'
    form=CustomUserCreationForm()

    if request.method=='POST':
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username=user.username.lower()
            user.save()

            messages.success(request,'User has succesfully registered')

            login(request,user)
            return redirect('edit-profile')
        
        else:
            messages.success(request,'Some error has occured')

    context={'page':page,'form':form}
    return render(request,'users/login_register.html',context)

def profiles(request):

    text,profiles=searchProfiles(request)

    custom_range,profiles=paginateProfiles(request,profiles,3)

    currentUser=None
    if request.user.is_authenticated:
        currentUser=request.user.profile
    context={'profiles':profiles,'current':currentUser,'searchQuery':text,'custom_range':custom_range}
    return render(request,'users/profiles.html',context)

def profile(request,pk):
    profile=Profile.objects.get(id=pk)
    context={'profile':profile}
    return render(request,'users/profile.html',context)



@login_required(login_url='login')
def UserAccount(request):
    
    profile=request.user.profile
    courses=profile.courses_set.all()
    skill=profile.skill.all()

    context={'profile':profile,'skill':skill,'courses':courses}


    return render(request,'users/account.html',context)

@login_required(login_url='login')
def EditProfile(request):
    profile=request.user.profile
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form=ProfileForm(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            form.save()

            return redirect('account')
    context={'form':form}
    return render(request,'users/edit-profile.html',context)


@login_required(login_url='login')
def inbox(request):
    profile=request.user.profile
    messageRequests=profile.messages.all()
    unreadCount=messageRequests.filter(is_read=False).count()
    context={'messageRequests':messageRequests, 'unreadCount':unreadCount}
    return render(request,'users/inbox.html',context)

@login_required(login_url='login')
def inboxMessage(request, primkey):
    profile=request.user.profile
    messageRequest=profile.messages.get(id=primkey)
    if messageRequest.is_read == False:
        messageRequest.is_read=True
        messageRequest.save()
    context={'messageRequest':messageRequest}
    return render(request,'users/message.html',context)


@login_required(login_url='login')
def createMessage(request,primkey):

    form = MessageForm()
    recipient=Profile.objects.get(id=primkey)
    try:
        sender=request.user.profile
    except:
        sender=None
    
    if request.method=='POST':
       form =MessageForm(request.POST)
       if form.is_valid: 
        message=form.save(commit=False)

        message.sender=sender
        message.recipient=recipient
        if sender is not None:
            message.name=sender.name
            message.email=sender.email

        message.save()
        messages.success(request,'Message sent')
        return redirect('profile',pk=recipient.id)


    context={'form':form,'recipient':recipient}
    return render(request,'users/message-form.html',context)

@login_required(login_url='login')
def replyMessage(request, primkey):
    form=MessageForm()
    recipient=Profile.objects.get(id=primkey)
    sender=request.user.profile
    if request.method=='POST':
        form=MessageForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)

            reply.sender=sender
            reply.recipient=recipient
            reply.save()
            messages.success(request,'Message sent')
            return redirect('profile',pk=recipient.id)
    context={'form':form,'recipient':recipient}
    return render(request,'users/reply-form.html',context)