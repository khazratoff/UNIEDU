from .models import Profile, Skill
from django.db.models import Q
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

def paginateProfiles(request,profiles,results):
    page=request.GET.get('page')
    results=6
    paginator=Paginator(profiles,results)

    try:
        profiles=paginator.page(page)
    except PageNotAnInteger:
        page=1
        profiles=paginator.page(page)
    except EmptyPage:
        page=paginator.num_pages
        profiles=paginator.page(page)
    
    left_index=int(page)-1
    if left_index<1:
        left_index=1
    right_index=int(page)+2
    if right_index>paginator.num_pages:
        right_index=paginator.num_pages+1
    custom_range=range(left_index,right_index)

    return custom_range,profiles

def searchProfiles(request):

    text=''
    if request.GET.get('text'):
        text=request.GET.get('text')
    skills=Skill.objects.filter(name__icontains=text)
    profiles=Profile.objects.distinct().filter(
        Q(name__icontains=text)|
        Q(short_intro__icontains=text)|
        Q(skill__in=skills)
    )

    return text,profiles
    