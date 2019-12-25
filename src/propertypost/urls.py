from django.urls import path
from propertypost import views

urlpatterns = [

    path('prop-posts/', views.PropertyPostList.as_view(), name=views.PropertyPostList.name),
    path('prop-posts/<int:pk>', views.PropertyPostDetail.as_view(), name=views.PropertyPostDetail.name),

    path('images/', views.ImageList.as_view(), name=views.ImageList.name),
    path('images/<int:pk>', views.ImageDetail.as_view(), name=views.ImageDetail.name),

]