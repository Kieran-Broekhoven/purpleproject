from django.db import models


class Shelter(models.Model):
    name = models.TextField()
    poc = models.TextField()
