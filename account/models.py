from django.db import models
# from multiselectfield import MultiSelectField

# Create your models here.


class user(models.Model):
    name = models.CharField(max_length=100, default='')
    username = models.CharField(max_length=100, default='')
    email = models.EmailField()
    password = models.CharField(max_length=100 , default='')
    error = models.BooleanField(default='False')


class DocumentCategory(models.Model):
    doc_category = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.doc_category

class Category(models.Model):
    new_category = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.new_category


class Documentation(models.Model):
    # MY_CHOICES = (
    #     ('a', "A good choice"),
    #     ('b', "A bad choice"),
    #     ('c', "A noice choice"),
    #     ('d', "A Tori choice"),
    # )
    doc_category = models.CharField(max_length=100, default='')
    title = models.CharField(max_length=100, default='')
    date = models.DateField()
    category = models.ManyToManyField(Category)
    document = models.FileField(upload_to='documents', default='', blank=True)
    description = models.TextField(max_length=500, default='')
    information = models.TextField(max_length=5000, default='', blank=True)
    info_file = models.FileField(upload_to='files', default='', blank=True)




