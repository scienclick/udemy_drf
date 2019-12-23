from rest_framework import serializers
from propertypost.models import PropertyPost


class PropPostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PropertyPost
        fields = (
            'id',

            'type',
            'square',
            'buyingprice',
            'description',

            'viewnum',
            'pricepermeter',

            'timestamp',
            'updated',
        )

        read_only_fields = [
            'viewnum',
            'pricepermeter',
        ]
