from django.urls import path
from propertypost import views

urlpatterns = [

    path('prop-posts/', views.PropertyPostList.as_view(), name=views.PropertyPostList.name),
    path('prop-posts/<int:pk>', views.PropertyPostDetail.as_view(), name=views.PropertyPostDetail.name),

]