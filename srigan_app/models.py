from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Admin(models.Model):
    name=models.CharField(max_length=100,null=False,blank=False)
    email=models.CharField(max_length=100,null=False,blank=False)
    phone_no=models.CharField(max_length=13,null=False,blank=False)
    password=models.CharField(max_length=100,null=False,blank=False)
    def __str__(self):
        return self.email