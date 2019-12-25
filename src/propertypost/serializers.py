from rest_framework import serializers
from propertypost.models import PropertyPost
from propertypost.models import Image

class ImageSerializer(serializers.HyperlinkedModelSerializer):
    prop_post = serializers.SlugRelatedField(
        queryset=PropertyPost.objects.all(),
        slug_field='pk',
    )

    class Meta:
        model = Image
        fields = (
            'url',
            'photo',
            'prop_post',
        )

class PropPostSerializer(serializers.HyperlinkedModelSerializer):
    images4thisproperty = ImageSerializer(many=True, required=False)
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

            'images4thisproperty',

            'timestamp',
            'updated',
        )

        read_only_fields = [
            'viewnum',
            'pricepermeter',
        ]



