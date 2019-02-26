from django.db import models

# Create your models here.


class user(models.Model):
    name = models.CharField(max_length=100, default='')
    username = models.CharField(max_length=100, default='')
    email = models.EmailField()
    password = models.CharField(max_length=100 , default='')
    error = models.BooleanField(default='False')


class DocumentCategory(models.Model):
    doc_category = models.CharField(max_length=200, default='')


class Category(models.Model):
    new_category = models.CharField(max_length=200, default='')


class Documentation(models.Model):
    doc_category = models.CharField(max_length=100, default='')
    title = models.CharField(max_length=100, default='')
    date = models.DateField()
    category = models.CharField(max_length=100, default='')
    document = models.FileField(upload_to='documents', default='', blank=True)
    description = models.TextField(max_length=500, default='')
    information = models.TextField(max_length=5000, default='', blank=True)




