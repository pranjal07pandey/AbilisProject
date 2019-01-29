from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.



class Documentation(models.Model):

    title = models.CharField(max_length=100, default='')
    date = models.DateField()
    category = models.CharField(max_length=250, default='')
    document = models.FileField(upload_to='documents', default='')

