from django.db import models



# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stocks = models.IntegerField()
    image_url = models.CharField(max_length=2083)


class offers(models.Model):
    offer_code = models.CharField(max_length=150)
    description = models.CharField(max_length=250)
    discount = models.FloatField() # 0.2 means 20% discount 

