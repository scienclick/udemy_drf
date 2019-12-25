from django.contrib import admin
from django.urls import path
from users import views

urlpatterns = [

    path('', views.UserList.as_view(), name=views.UserList.name),
    path('<int:pk>', views.UserDetail.as_view(), name=views.UserDetail.name),
]