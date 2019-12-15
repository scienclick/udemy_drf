from django.urls import path
from . import views

urlpatterns = [
    path('api/news/', views.NewsList.as_view(), name=views.NewsList.name),
    path('api/news/<int:pk>', views.NewsDetail.as_view(), name=views.NewsDetail.name),
    path('api/entity/', views.EntityList.as_view(), name=views.EntityList.name),
    path('api/entity/<int:pk>', views.EntityDetail.as_view(), name=views.EntityDetail.name),
]