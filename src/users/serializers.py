from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts4thisowner = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='propertypost-detail',
    )

    class Meta:
        model = CustomUser
        fields = (
            'url',
            'id',
            'pk',
            'username',
            'email',
            'first_name',
            'last_name',
            'phone',
            'posts4thisowner',

        )

