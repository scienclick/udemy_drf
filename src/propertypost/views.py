from rest_framework import generics
from propertypost.models import PropertyPost
from propertypost.serializers import PropPostSerializer
from django.utils import timezone

class PropertyPostList(generics.ListCreateAPIView):
    queryset = PropertyPost.objects.all()
    serializer_class = PropPostSerializer
    name = 'propertypost-list'

    def perform_create(self, serializer):
        try:
            price = serializer.initial_data['buyingprice']
            square = serializer.initial_data['square']
            priceperarea=round(float(price)/float(square),2)
        except:
            priceperarea=0
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
            priceperarea=round(float(price)/float(square),2)
        except:
            priceperarea=0
            pass
        serializer.save(pricepermeter=priceperarea,updated=timezone.now())




