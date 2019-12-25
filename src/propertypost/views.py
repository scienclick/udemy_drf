from rest_framework import generics
from propertypost.models import PropertyPost
from propertypost.serializers import PropPostSerializer
from django.utils import timezone

from django_filters import rest_framework as filters
from django_filters import DateTimeFilter, NumberFilter

from propertypost.serializers import ImageSerializer
from propertypost.models import Image

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

    def perform_create(self, serializer):
        try:
            price = serializer.initial_data['buyingprice']
            square = serializer.initial_data['square']
            priceperarea = round(float(price) / float(square), 2)
        except:
            priceperarea = 0
            pass
        serializer.save(pricepermeter=priceperarea)


class PropertyPostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PropertyPost.objects.all()
    serializer_class = PropPostSerializer
    name = 'propertypost-detail'

    def get(self, request, *args, **kwargs):
        propertypost_object = self.get_object()
        propertypost_object.viewnum += 1
        propertypost_object.save()
        return super().get(request, *args, **kwargs)

    def perform_update(self, serializer):
        try:
            price = serializer.initial_data['buyingprice']
            square = serializer.initial_data['square']
            priceperarea = round(float(price) / float(square), 2)
        except:
            priceperarea = 0
            pass
        serializer.save(pricepermeter=priceperarea, updated=timezone.now())


class ImageList(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    name = 'image-list'


class ImageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    name = 'image-detail'