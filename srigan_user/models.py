from django.db import models
from django.contrib.auth.models import User

class users(models.Model):
    email=models.CharField(max_length=100,null=False,blank=False)
    password=models.CharField(max_length=100,null=False,blank=False)
# Create your models here.
