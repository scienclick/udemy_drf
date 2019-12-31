from rest_framework import serializers
from propertypost.models import PropertyPost
from propertypost.models import Image

class ImageSerializer(serializers.HyperlinkedModelSerializer):
    prop_post = serializers.SlugRelatedField(
        queryset=PropertyPost.objects.all(),
        slug_field='pk',
    )
    prop_post_owner = serializers.ReadOnlyField(source='prop_post.owner.username')

    class Meta:
        model = Image
        fields = (
            'url',
            'photo',
            'prop_post',
            'prop_post_owner'
        )

class PropPostSerializer(serializers.HyperlinkedModelSerializer):
    images4thisproperty = ImageSerializer(many=True, required=False)
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = PropertyPost
        fields = (
            'id',
            'owner',


            'type',
            'square',
            'buyingprice',
            'description',

            'viewnum',
            'pricepermeter',
            'lat',
            'lon',
            'location',

            'images4thisproperty',

            'timestamp',
            'updated',
        )

        read_only_fields = [
            'viewnum',
            'pricepermeter',
            'location',
        ]



