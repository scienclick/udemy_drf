from django.db import models

class News(models.Model):
    title = models.TextField(verbose_name="title", max_length=1500)
    sentiment_choices=[
        ("p","positive"),
        ("n", "negative"),
        ("pn", "neutral"),
    ]
    sentiment = models.CharField(verbose_name="Sentiment", choices=sentiment_choices, default='pn', max_length=150, null=True,
                                blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)


class Entity(models.Model):
    releventnews = models.ForeignKey(News, related_name='entities4thisnews', on_delete=models.CASCADE, null=True, blank=True)
    entity = models.TextField(verbose_name="Entity", max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)