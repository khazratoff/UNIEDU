from django.urls import path
from . import views


urlpatterns=[
    path('login/',views.loginUser,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('register/',views.registerUser,name='register'),

    path('',views.profiles,name='profiles'),
    path('profile/<str:pk>/',views.profile,name='profile'),
    path('account/',views.UserAccount,name='account'),

    path('edit-profile/',views.EditProfile,name='edit-profile'),


    path('inbox/',views.inbox,name='inbox'),
    path('message/<str:primkey>/',views.inboxMessage,name='message'),
    path('create-message/<str:primkey>/',views.createMessage,name='create-message'),
    path('reply-message/<str:primkey>/', views.replyMessage,name='reply-message'),

]