from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.response import Response
from propertypost.views import PropertyPostList
from news.views import NewsList

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'news': reverse(NewsList.name, request=request),
            'prop-posts': reverse(PropertyPostList.name, request=request),
        })