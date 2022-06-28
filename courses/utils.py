from django.db.models import Q
from .models import Courses, Tags
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

def paginateCourses(request,coursesObject,results):
    page=request.GET.get('page')
    results=6
    paginator=Paginator(coursesObject,results)

    try:
        coursesObject=paginator.page(page)
    except PageNotAnInteger:
        page=1
        coursesObject=paginator.page(page)
    except EmptyPage:
        page=paginator.num_pages
        coursesObject=paginator.page(page)
    
    left_index=int(page)-1
    if left_index<1:
        left_index=1
    right_index=int(page)+2
    if right_index>paginator.num_pages:
        right_index=paginator.num_pages+1
    custom_range=range(left_index,right_index)

    return custom_range,coursesObject


def searchCourses(request):
    
    text=''

    if request.GET.get('text'):
        text=request.GET.get('text')

    Tag=Tags.objects.filter(name__iexact=text)

    coursesObject=Courses.objects.distinct().filter(
        Q(name__icontains=text)|
        Q(owner__name__icontains=text)|
        Q(tags__in=Tag)

    )
    return coursesObject, text
