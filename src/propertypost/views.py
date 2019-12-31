from rest_framework import generics
from propertypost.models import PropertyPost
from propertypost.serializers import PropPostSerializer
from django.utils import timezone

from django_filters import rest_framework as filters
from django_filters import DateTimeFilter, NumberFilter

from propertypost.serializers import ImageSerializer
from propertypost.models import Image

from propertypost import custompermission
from rest_framework import permissions

from django.contrib.gis.geos import GEOSGeometry,Point
from django.contrib.gis.measure import Distance

class IntegerListFilter(filters.Filter):
    def filter(self,qs,value):
        if value not in (None,''):
            integers = [int(v) for v in value.split(',')]
            return qs.filter(**{'%s__%s'%(self.field_name, self.lookup_expr):integers})
        return qs

class PropertyPostFilter(filters.FilterSet):
    ids = IntegerListFilter(field_name='id', lookup_expr='in')

    from_timestamp_date = DateTimeFilter(
        field_name='timestamp', lookup_expr='gte')
    to_timestamp_date = DateTimeFilter(
        field_name='timestamp', lookup_expr='lte')

    min_buyingprice = NumberFilter(
        field_name='buyingprice', lookup_expr='gte')
    max_buyingprice = NumberFilter(
        field_name='buyingprice', lookup_expr='lte')

    class Meta:
        model = PropertyPost
        fields = (
            'type',
        )


class PropertyPostList(generics.ListCreateAPIView):
    queryset = PropertyPost.objects.all()
    serializer_class = PropPostSerializer
    name = 'propertypost-list'

    filter_class = PropertyPostFilter
    ordering_fields = (
        'square',
        'buyingprice',
        'timestamp',
        'pricepermeter',
    )
    search_fields = (
        'description',
    )
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        custompermission.IsCurrentUserOwnerOrReadOnly,
    )

    def perform_create(self, serializer):
        lat = serializer.initial_data['lat']
        long = serializer.initial_data['lon']
        pnt = 'POINT(' + str(long) + ' ' + str(lat) + ')'
        try:
            price = serializer.initial_data['buyingprice']
            square = serializer.initial_data['square']
            priceperarea = round(float(price) / float(square), 2)


        except:
            priceperarea = 0
            pass
        serializer.save(owner=self.request.user, pricepermeter=priceperarea, location=pnt)

    def get_queryset(self):
        polystr = self.request.query_params.get('poly', None)
        diststr = self.request.query_params.get('dist', None)
        if polystr:
            poly = GEOSGeometry('SRID=4326;' + polystr)
            qs = PropertyPost.objects.filter(location__contained=poly)
            return qs
        if diststr:
            long=float(diststr.split(',')[1])
            lat=float(diststr.split(',')[0])
            rad=float(diststr.split(',')[2])
            pnt = Point(long, lat)
            qs = PropertyPost.objects.filter(location__distance_lt=(pnt,Distance(km=rad)))
            return qs

class PropertyPostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PropertyPost.objects.all()
    serializer_class = PropPostSerializer
    name = 'propertypost-detail'
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        custompermission.IsCurrentUserOwnerOrReadOnly,
    )

    def get(self, request, *args, **kwargs):
        propertypost_object = self.get_object()
        propertypost_object.viewnum += 1
        propertypost_object.save()
        return super().get(request, *args, **kwargs)

    def perform_update(self, serializer):
        lat = serializer.initial_data['lat']
        long = serializer.initial_data['lon']
        pnt = 'POINT(' + str(long) + ' ' + str(lat) + ')'

        try:
            price = serializer.initial_data['buyingprice']
            square = serializer.initial_data['square']
            priceperarea = round(float(price) / float(square), 2)
        except:
            priceperarea = 0
            pass
        serializer.save(pricepermeter=priceperarea, updated=timezone.now(), location=pnt)


class ImageList(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    name = 'image-list'
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        custompermission.ImagePermission,
    )


class ImageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    name = 'image-detail'
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        custompermission.ImagePermission,
    )