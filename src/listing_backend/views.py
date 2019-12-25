from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.response import Response
from propertypost.views import PropertyPostList,ImageList
from news.views import NewsList
from users.views import UserList

from rest_framework.permissions import IsAdminUser

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    permission_classes = (
        IsAdminUser,
    )

    def get(self, request, *args, **kwargs):
        return Response({
            'news': reverse(NewsList.name, request=request),
            'prop-posts': reverse(PropertyPostList.name, request=request),
            'images': reverse(ImageList.name, request=request),
            'users': reverse(UserList.name, request=request),
        })