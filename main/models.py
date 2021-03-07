from django.db import models

# Create your models here.


class People(models.Model):

    Pid = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.CharField(max_length=100)
    mobile = models.BigIntegerField(null=True)
    gender = models.CharField(max_length=100)
    passwd = models.CharField(max_length=100)
    state = models.CharField(max_length=50, default='Happy')
    bio = models.TextField(default="Hello There")
