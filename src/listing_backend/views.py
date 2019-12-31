from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.response import Response
from propertypost.views import PropertyPostList,ImageList
from news.views import NewsList
from users.views import UserList

from rest_framework.permissions import IsAdminUser

from rest_framework.decorators import APIView
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_auth.registration.serializers import VerifyEmailSerializer
from allauth.account.models import EmailConfirmation, EmailConfirmationHMAC
from django.utils.translation import ugettext_lazy as _




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

class VerifyEmailView(APIView):
    permission_classes = (AllowAny,)
    allowed_methods = ('POST','GET', 'OPTIONS', 'HEAD')

    def get_serializer(self, *args, **kwargs):
        return VerifyEmailSerializer(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        print('salam')
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.kwargs['key'] = serializer.validated_data['key']
        try:
            confirmation = self.get_object()
            confirmation.confirm(self.request)
            return Response({'detail': _('Successfully confirmed email.')}, status=status.HTTP_200_OK)
        except EmailConfirmation.DoesNotExist:
            return Response({'detail': _('Error. Incorrect key.')}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, *args, **kwargs):
        path = request.path
        path_vals = path.split('/')
        key = path_vals[-2]
        self.key=key
        request.data['key']=key
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.kwargs['key'] = serializer.validated_data['key']
        try:
            confirmation = self.get_object()
            confirmation.confirm(self.request)
            return Response({'detail': _('Successfully confirmed email.')}, status=status.HTTP_200_OK)
        except EmailConfirmation.DoesNotExist:
            return Response({'detail': _('Error. Incorrect key.')}, status=status.HTTP_404_NOT_FOUND)


    def get_object(self, queryset=None):
        key = self.kwargs['key']
        emailconfirmation = EmailConfirmationHMAC.from_key(key)
        if not emailconfirmation:
            if queryset is None:
                queryset = self.get_queryset()
            try:
                emailconfirmation = queryset.get(key=key.lower())
            except EmailConfirmation.DoesNotExist:
                raise EmailConfirmation.DoesNotExist
        return emailconfirmation

    def get_queryset(self):
        qs = EmailConfirmation.objects.all_valid()
        qs = qs.select_related("email_address__user")
        return qs

