from django.db import models


class Data(models.Model):
    title = models.TextField(blank=True, null=True)
    sold_price = models.FloatField(blank=True, null=True)
    bids = models.IntegerField(blank=True, null=True)
    sold_date = models.DateField(blank=True, null=True)
    card_link = models.TextField(blank=True, null=True)
    image_link = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
