from django.db import models


class PropertyPost(models.Model):

    condoorhouse_choices = [('APARTMENT', 'Apartment'), ('HOUSE', 'House'), ('COMMERCIAL', 'Commercial'),
                            ('LAND', 'Land')]
    type = models.CharField(choices=condoorhouse_choices, default='APARTMENT', max_length=150)

    square = models.FloatField(verbose_name="Area in square meter?", blank=False, null=False,default=1)
    buyingprice = models.FloatField(verbose_name="Buying Price?", default=0, blank=True, null=True)
    description = models.TextField(verbose_name="Description", max_length=500, blank=True, null=True, default="")

    viewnum = models.IntegerField(verbose_name="view num", default=0,)
    pricepermeter = models.FloatField(verbose_name="Pricepermeter", default=0,)

    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-timestamp',)