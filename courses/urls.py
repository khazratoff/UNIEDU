from django.urls import path
from . import views 

urlpatterns=[
    path('',views.courses,name='courses'),
    path('course/<str:primkey>/',views.course,name='course'),
    path('add-course',views.courseCreate,name='add-course'),
    path('update-course/<str:primkey>/',views.courseUpdate,name='update-course'),
    path('delete-course/<str:primkey>/',views.courseDelete,name='delete-course')
]
