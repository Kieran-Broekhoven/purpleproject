from django.db import models


class Shelter(models.Model):
    name = models.TextField()
    poc = models.TextField(blank=True, null=True)
    username = models.CharField(max_length=50)


class ItemRequest(models.Model):
    name = models.TextField()
    wishlist_link = models.TextField(blank=True, null=True)
    requesting_shelter = models.IntegerField()
    approved = models.BooleanField(default=False)
    ordered = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)


class HousingRequest(models.Model):
    bedrooms = models.IntegerField()
    stay_duration = models.IntegerField()
    moved_in = models.BooleanField()
    checked_out = models.BooleanField()
    requesting_shelter = models.IntegerField()


class House(models.Model):
    ready = models.BooleanField()
    occupied = models.BooleanField()
    address = models.TextField()
    bedrooms = models.IntegerField()
