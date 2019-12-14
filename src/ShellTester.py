# <editor-fold desc="These needs to be run from shell">

# python manage.py shell #activate the shell using this
from news.serializers import NewsSerializer
from news.models import News

data = {"title": "This is Title1", "sentiment": "pn"}
serializer = NewsSerializer(data=data)
serializer.is_valid()
serializer.save()
serializer.validated_data


data = {
    "title": "London is great city,but is not as good as Newyork",
    "sentiment": "pn",
    "entities4thisnews": [

        {
            "entity": "London",
        },
        {
            "entity": "Newyork",
        }
    ]
}

serializer = NewsSerializer(data=data)
serializer.is_valid()
serializer.save()
serializer.validated_data

# </editor-fold>
