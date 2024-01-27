from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class listing(models.Model):
    seller = models.CharField(max_length=64)
    title = models.CharField(max_length=32)
    listingid = models.IntegerField()
    description = models.TextField(max_length=640)
    category = models.CharField(max_length=64)
    image_link = models.CharField(max_length=200,default=None, blank=True, null= True)
    start = models.IntegerField()
    current = models.IntegerField()
    status = models.BooleanField()


class bid(models.Model):
    user = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    listingid = models.IntegerField()
    bid = models.IntegerField()


class comment(models.Model):
   user = models.CharField(max_length=64) 
   comment = models.CharField(max_length=64)
   listingid = models.IntegerField()
   timestamp = models.DateTimeField(auto_now_add=True)

class watchlist(models.Model):
    user = models.CharField(max_length=64)
    listingid = models.IntegerField()

class winner(models.Model):
    owner = models.CharField(max_length=64)
    winner = models.CharField(max_length=64)
    listingid = models.IntegerField()
    winprice = models.IntegerField()
    title = models.CharField(max_length=64) 