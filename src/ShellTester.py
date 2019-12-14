# <editor-fold desc="These needs to be run from shell">

# python manage.py shell #activate the shell using this
from news.serializers import NewsSerializer,EntitySerializer
from news.models import News

data = {"title": "This is Title1", "sentiment": "pn"}
serializer = NewsSerializer(data=data)
serializer.is_valid()
serializer.save()
serializer.validated_data



serializer = NewsSerializer(data=data)
serializer.is_valid()
serializer.save()
serializer.validated_data

# </editor-fold>
