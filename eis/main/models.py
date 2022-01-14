from django.db import models
from django import forms
from django.db.models.deletion import SET_NULL
from django.contrib.auth.models import User
# Create your models here.

class Report(models.Model):
    BKS = (
        ("BKS1", "BKS1"),
        ("BKS2", "BKS2"),
        ("BKS3", "BKS3"),
    )
    TYPE = (
        ("Betonarme", "Betonarme"),
        ("Yığma", "Yığma"),
        ("Çelik", "Çelik"),
    )
    areaOfFloor = models.IntegerField(null=True)
    buildingConstrucionYear = models.IntegerField(null=True)
    buildingFloorNumber = models.IntegerField(null=True)
    buildingType = models.CharField(max_length=255, null=True, choices=TYPE)
    buildingUsageClass = models.CharField(max_length=255, null=True, choices=BKS)
    latitude = models.CharField(max_length=20, null=True)
    longitude = models.CharField(max_length=20, null=True)
    vs30 = models.CharField(max_length=255, null=True)
    title = models.CharField(max_length=255, null=True)
    user = models.CharField(max_length=255)

    def __str__(self):
        if self.title is not None:
            return self.title
        else:
            return str(self.id)
