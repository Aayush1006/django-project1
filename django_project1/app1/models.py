from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    user = models.OneToOneField(User, null=True,blank=True,on_delete=models.SET_NULL)
    firstname = models.CharField(max_length=25)
    lastname  = models.CharField(max_length=25)
    username  = models.CharField(max_length=50)
    email     = models.CharField(max_length=100)
    gender    = models.CharField(max_length=10)
    mobile = models.BigIntegerField(default=0)
    address   = models.CharField(max_length=100)
    state     = models.CharField(max_length=100)
    dob  = models.DateField(null=True,blank=True)
    def __str__(self):
        return str(self.username) + "-"
