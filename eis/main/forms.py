from django.db.models import fields
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class questionForm(ModelForm):
    class Meta:
        model = Report
        fields = [
            "title",
            "buildingUsageClass",
            "buildingConstrucionYear",
            "buildingFloorNumber",
            "areaOfFloor",
            "buildingType",
        ]

class createUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2"
            ]

class mapForm(ModelForm):
    class Meta:
        model = Report
        fields = [
            "latitude",
            "longitude",
            "user",
            "vs30",
        ]