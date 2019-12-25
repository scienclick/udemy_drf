from rest_framework import generics
from .models import CustomUser
from .serializers import UserSerializer


class UserList(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    name = 'customuser-list'


class UserDetail(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    name = 'customuser-detail'

