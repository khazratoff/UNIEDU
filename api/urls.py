from django.urls import path
from api import views
urlpatterns=[
    path('',views.GetRoutes),
    path('courses/',views.getCourses),
    path('courses/<str:pk>/',views.getCourse)
]