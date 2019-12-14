from news.models import *
from rest_framework import serializers

class EntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entity
        fields = (
            'id',
            'releventnews',
            'entity',
            'timestamp',
        )

class NewsSerializer(serializers.ModelSerializer):
    entities4thisnews = EntitySerializer(many=True, required=False)
    class Meta:
        model = News
        fields = (
            "id",
            "title",
            "sentiment",
            'timestamp',
            "entities4thisnews",
        )

    def create(self, validated_data):
        entity_data = validated_data.pop('entities4thisnews')
        news = News.objects.create(**validated_data)
        for an_entity in entity_data:
            Entity.objects.create(releventnews=news, **an_entity)
        return news

