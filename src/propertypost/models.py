# from django.db import models
from django.contrib.gis.db import models
import uuid
import datetime
from django.contrib.auth import get_user_model

class PropertyPost(models.Model):
    owner = models.ForeignKey(
        get_user_model(),
        related_name='posts4thisowner',
        on_delete=models.CASCADE)

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

    lat = models.FloatField(verbose_name="Lat.", default=0, blank=True, null=True)
    lon = models.FloatField(verbose_name="Long.", default=0, blank=True, null=True)
    location = models.PointField(null=True, blank=True)



    class Meta:
        ordering = ('-timestamp',)



def upload_update_image(instance, filename):
    extension = filename.split(".")[-1]
    house = instance.id
    print(house)
    return "myposts/{}/{}.{}".format(datetime.datetime.today().year,
                                     datetime.datetime.now().strftime("%Y%m%d%H%M%S") + "_" +
                                     str(uuid.uuid4()), extension)

class Image(models.Model):
    prop_post = models.ForeignKey(
        PropertyPost,
        related_name='images4thisproperty',
        on_delete=models.CASCADE)

    photo = models.ImageField(upload_to=upload_update_image, null=True, blank=True,default="")
